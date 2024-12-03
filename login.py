from typing import Callable

import webview

_login_callback: Callable[[str], None] | None = None

_DEST_PATTERN = '123.121.147.7:88'

class LogginStatus:
    NOT_LOGGED_IN = 0
    LOGGING_IN = 1
    LOGGED_IN = 2

def set_login_callback(callback):
    global _login_callback
    _login_callback = callback

def make_on_login(jump_page, callback = None):
    def on_login(window):
        url = window.get_current_url()
        if 'bksy.bjtu.edu.cn/login_introduce_t.html' in url:
            window.load_url(jump_page)
        elif _DEST_PATTERN in url:
            cookies = window.get_cookies()
            if len(cookies) == 0:
                return
            else:
                jsessionid = cookies[0]['JSESSIONID'].value
            window.destroy()
            if _login_callback:
                _login_callback(jsessionid)
                if callback is not None:
                    callback()
    return on_login

def login_via_mis(callback):
    login_url = 'https://mis.bjtu.edu.cn/module/module/104/'
    jump_page = 'https://bksycenter.bjtu.edu.cn/NoMasterJumpPage.aspx?URL=jwcZhjx&FPC=page:jwcZhjx'

    window = webview.create_window(title='MIS 登录', url=login_url)

    # because of a strange behavior of pywebview
    called = False
    def _callback(status):
        nonlocal called
        if not called:
            called = True
            callback(status)

    window.events.loaded += make_on_login(jump_page, lambda: _callback(LogginStatus.LOGGED_IN))

    def window_closing():
        _callback(LogginStatus.NOT_LOGGED_IN)


    window.events.closing += window_closing