from playwright.sync_api import Page

from page_object.registration_page import RegistrationPage
from basics.credits import Credits


def test_registration(page: Page):
    name = Credits.name.value
    mail = Credits.mail.value
    ws_name = Credits.ws_name.value
    password = Credits.password.value
    (RegistrationPage(page=page)
     .to_registration_page()
     .insert_name(name=name)
     .insert_mail(mail=mail)
     .insert_workspace_name(workspace_name=ws_name)
     .insert_password(password=password)
     .click_on_politics()
     .finish_registration())
