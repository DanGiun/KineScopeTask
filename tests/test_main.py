from playwright.sync_api import Page

from basics.credits import Credits
from page_object.login_page import LoginPage
from page_object.main_page import MainPage


def test_kinescope(page: Page):
    mail = Credits.mail.value
    password = Credits.password.value
    token_name = "TestToken"
    title = 'test'
    yt_url = 'https://www.youtube.com/watch?v=CH50zuS8DD0'
    (LoginPage(page=page)
     .to_login_page()
     .insert_mail(mail=mail)
     .insert_password(password=password)
     .press_enter_button())
    (MainPage(page=page)
     .to_api_keys_page()
     .create_new_key()
     .insert_token_name(name=token_name)
     .choose_permission()
     .submit_token_creating()
     .copy_token()
     .upload_video(title=title, video_url=yt_url)
     .open_video_page()
     .video_upload_check())
