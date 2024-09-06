from __future__ import annotations

import time

from basics.basic_enums import Selectors
from basic_methods import BasicMethods


class MainPage(BasicMethods):
    def to_api_keys_page(self) -> MainPage:
        """
        Переход на страницу с API ключами
        """
        self.go_to(url=Selectors.token_page.value)
        return self

    def create_new_key(self) -> MainPage:
        """
        Нажатие на кнопку создания нового ключа
        """
        self.element_presence(selector=Selectors.create_token_button.value).click()
        time.sleep(0.5)
        return self

    def insert_token_name(self, name: str) -> MainPage:
        """
        Ввод названия токена в поле

        Args:
            name (str): Название токена
        """
        self.insert_value(value=name, selector=Selectors.token_name_field.value)
        return self

    def choose_permission(self) -> MainPage:
        """
        Выбор разрешений для токена, в нашем случае, Загружать файлы
        """
        self.element_presence(selector=Selectors.upload_files.value).click()
        time.sleep(0.5)
        return self

    def submit_token_creating(self) -> MainPage:
        """
        Подтвердить создание токена
        """
        self.element_presence(selector=Selectors.submit_creation.value).click()
        time.sleep(0.5)
        return self

    def copy_token(self) -> MainPage:
        """
        Нажать на кнопку копирования токена
        """
        self.element_presence(selector=Selectors.copy_token_button.value).click()
        time.sleep(0.5)
        return self

    def upload_video(self, title: str, video_url: str) -> MainPage:
        """
        Выполнение запроса для отправки видео

        Args:
            title (str): Название, под которым видео отправляется на загрузку.
            video_url (str): URL к видео на YouTube.
        """
        token = BasicMethods.data_from_buffer()
        parent_id = self.project_id_from_request(token)
        self.post_request(token=token, parent_id=parent_id, title=title, vid_url=video_url)
        time.sleep(0.5)
        return self

    def open_video_page(self) -> MainPage:
        """
        Открытие страницы с загруженными видео
        """
        self.element_presence(selector=Selectors.videos_page.value).click()
        time.sleep(0.5)
        return self

    def video_upload_check(self) -> MainPage:
        """
        Проверка того, что это действительно загруженное нами видео
        """
        self.wait_for_value_in_attribute(selector=Selectors.video_name.value, attribute='title',
                                         expected_value='1 Minute Timer', waiting_time=100)
        print("\nUploaded")
        return self
