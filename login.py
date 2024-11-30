from typing import Callable

import webview

__login_callback: Callable[[str], None] | None = None

def set_login_callback(callback):
    global __login_callback
    __login_callback = callback

def make_on_login(jump_page):
    def on_login(window):
        url = window.get_current_url()
        if url.find('bksy.bjtu.edu.cn/login_introduce_t.html') != -1:
            window.load_url(jump_page)
        elif url.find('123.121.147.7:88') != -1:
            cookies = window.get_cookies()
            if len(cookies) == 0:
                return
            else:
                jsessionid = cookies[0]['JSESSIONID'].value
            window.destroy()
            if __login_callback:
                __login_callback(jsessionid)
    return on_login

def login_via_mis():
    login_url = 'https://mis.bjtu.edu.cn/module/module/104/'
    jump_page = 'https://bksycenter.bjtu.edu.cn/NoMasterJumpPage.aspx?URL=jwcZhjx&FPC=page:jwcZhjx'

    window = webview.create_window(title='MIS 登录', url=login_url)

    window.events.loaded += make_on_login(jump_page)