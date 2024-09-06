from enum import Enum


class Selectors(Enum):
    url_register = 'https://app.kinescope.io/user/create?lang=ru'
    start = '[class="btn orange-color"]'
    name = '[placeholder="Полное имя"]'
    mail = '[placeholder="Рабочая почта"]'
    workplace_name = '[placeholder="Название рабочей зоны"]'
    password = '[placeholder="Пароль (не менее 8 символов)"]'
    politics = 'css=div._1upu3gu_e93ein:nth-child(1) > svg'
    registration = '[type="submit"]'

    url_login = 'https://app.kinescope.io/'
    log_mail = '[placeholder="Почта"]'
    log_pas = '[placeholder="Пароль"]'
    login = '[type="submit"]'
    token_page = 'https://app.kinescope.io/workspace/api_token'
    create_token_button = 'css=._nx1rfy'
    token_name_field = '[placeholder="Введите название токена"]'
    upload_files = 'css=div._1upu3gu_e93ein:nth-child(4) > svg:nth-child(1)'
    submit_creation = '[type="submit"]'
    copy_token_button = 'css=._ijvbga > div:nth-child(2) > button:nth-child(1)'
    videos_page = '[href="/video"]'
    video_name = 'css=._15pe6g4'

