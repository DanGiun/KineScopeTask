from __future__ import annotations

import time

from basics.basic_enums import Selectors
from basic_methods import BasicMethods


class RegistrationPage(BasicMethods):
    def to_registration_page(self) -> RegistrationPage:
        """
        Переход на страницу регистрации
        """
        self.go_to(url=Selectors.url_register.value)
        return self

    def insert_name(self, name: str) -> RegistrationPage:
        """
        Ввод имени в поле имени

        Args:
            name (str): Имя, которое собираемся вводить
        """
        self.insert_value(value=name, selector=Selectors.name.value)
        return self

    def insert_mail(self, mail: str) -> RegistrationPage:
        """
        Ввод почты в поле почты

        Args:
            mail (str): Почта, через которую будем в дальнейшем авторизовываться
        """
        self.insert_value(value=mail, selector=Selectors.mail.value)
        return self

    def insert_workspace_name(self, workspace_name: str) -> RegistrationPage:
        """
        Ввод название проекта в поле проекта

        Args:
            workspace_name (str): Название проекта, который создастся вместе с учетной записью
        """
        self.insert_value(value=workspace_name, selector=Selectors.workplace_name.value)
        return self

    def insert_password(self, password: str) -> RegistrationPage:
        """
        Ввод пароля в поле пароля

        Args:
            password (str): Пароль, под которым будем авторизовываться
        """
        self.insert_value(value=password, selector=Selectors.password.value)
        return self

    def click_on_politics(self) -> RegistrationPage:
        """
        Нажатие на галочку подтверждения соглашений и политик
        """
        self.element_presence(selector=Selectors.politics.value).click()
        time.sleep(0.5)
        return self

    def finish_registration(self) -> RegistrationPage:
        """
        Нажатие ни кнопку Зарегистрироваться
        """
        self.element_presence(selector=Selectors.registration.value).click()
        time.sleep(0.5)
        return self
