from __future__ import annotations

import time

from basics.basic_enums import Selectors
from basic_methods import BasicMethods


class LoginPage(BasicMethods):
    def to_login_page(self) -> LoginPage:
        """
        Переход на страницу авторизации
        """
        self.go_to(url=Selectors.url_login.value)
        return self

    def insert_mail(self, mail: str) -> LoginPage:
        """
        Ввод почты в поле почты

        Args:
            mail (str): Почта, на которую регистрировали учетную запись
        """
        self.insert_value(value=mail, selector=Selectors.log_mail.value)
        return self

    def insert_password(self, password: str) -> LoginPage:
        """
        Ввод пароля в поле пароля

        Args:
            password (str): Пароль, который вводили при регистрации
        """
        self.insert_value(value=password, selector=Selectors.log_pas.value)
        return self

    def press_enter_button(self) -> LoginPage:
        """
        Нажатие кнопки Войти
        """
        self.element_presence(selector=Selectors.login.value).click()
        time.sleep(0.5)
        return self
