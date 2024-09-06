import time
import pyperclip
from typing import Any

from playwright.sync_api import ElementHandle
from playwright.sync_api import Page


class BasicMethods:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url: str, waiting_time: int = 10000) -> None:
        """
        Осуществляет переход на указанный URL.

        Args:
            url (str): URL, на который необходимо перейти.
            waiting_time (int, optional): Время ожидания загрузки страницы (миллисекунды). По умолчанию 10000.
        """
        self.page.goto(url=url, timeout=waiting_time, wait_until='commit')

    def element_presence(self, selector: str, state: str | None = None, waiting_time: int = 10000) -> ElementHandle:
        """
        Ожидает появление элемента на странице.

        Args:
            selector (str): CSS-селектор элемента.
            state (str, optional): Состояние элемента, которые мы ожидаем
            waiting_time (int, optional): Время ожидания появления элемента (миллисекунды). По умолчанию 1000.

        Returns:
            ElementHandle: Объект ElementHandle, представляющий найденный элемент.
        """
        return self.page.wait_for_selector(selector=selector, state=state, timeout=waiting_time)

    def insert_value(self, value: Any, selector: str | None = None, element: ElementHandle | None = None,
                     waiting_time: int = 10000) -> None:
        """
        Заполняет значение в элементе.

        Args:
            value (Any): Значение, которое необходимо ввести в элемент.
            selector (str, optional): CSS-селектор элемента. Если указан, будет использован для поиска элемента.
            element (ElementHandle, optional): Экземпляр ElementHandle, представляющий элемент.
                ]Если указан, selector будет проигнорирован.
            waiting_time (int, optional): Время ожидания, в течение которого выполняется заполнение (миллисекунды).
                По умолчанию 1000.
        """
        if selector:
            element = self.element_presence(selector=selector, waiting_time=waiting_time)
        else:
            element = element
        element.fill(value=value, timeout=waiting_time)
        return

    def wait_for_value_in_attribute(self, selector: str, attribute: str, expected_value: str,
                                    waiting_time: int = 60) -> None:
        """
        Проверка data-status атрибута для элемента найденного по переданному селектору

        Args:
            selector (str): CSS-селектор элемента.
            attribute (str): Атрибут, значение которого хотим получить.
            expected_value (str): Значение, которое ожидаем получить в атрибуте data-status.
            waiting_time (int, optional): Время ожидания появления элемента (секунды). По умолчанию 60.
        """
        time_end = time.time() + waiting_time
        while time.time() <= time_end:
            element = self.element_presence(selector=selector)
            attribute_value = element.get_attribute(name=attribute)
            if expected_value in attribute_value:
                return
            time.sleep(1)
        raise RuntimeError(f"""Атрибут {attribute} для элемента не изменил свое значение на {expected_value}
         в течение {waiting_time} секунд""")

    def post_request(self, token: str, parent_id: str, title: str, vid_url: str, desc: str | None = None) -> None:
        """
        Выполнение Post запроса на загрузку видео в проект/папку

        Args:
            token (str): Токен, полученный из личного кабинета.
            parent_id (str): ID папки или проекта.
            title (str): Название, под которым видео отправляется на загрузку.
            vid_url (str): URL к видео на YouTube.
            desc (str): Описание видео. Параметр не обязателен
        """
        self.page.request.post(
            url="https://uploader.kinescope.io/v2/video",
            headers={
                "Authorization": f"Bearer {token}",
                "X-Parent-ID": parent_id,
                "X-Video-Title": title,
                "X-Video-Description": desc,
                "X-Video-URL": vid_url
            }
        )

    def project_id_from_request(self, token: str) -> str:
        """
        Выполнение Get запроса для получения ID проекта

        Args:
            token (str): Токен, полученный из личного кабинета.
        """
        response = self.page.request.get(
            url="https://api.kinescope.io/v1/projects?per_page=100",
            headers={
                "Authorization": f"Bearer {token}",
            }
        )
        return response.json()["data"][0]["id"]

    @staticmethod
    def data_from_buffer() -> str:
        """
        Получение данных из буфера обмена
        """
        clipboard_data = pyperclip.paste()
        return clipboard_data
