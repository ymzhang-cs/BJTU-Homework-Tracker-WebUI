import sys

import webview

from bridge import Bridge
from login import set_login_callback


def main():
    window = webview.create_window("BJTU Homework Tracker", "web/dist/index.html", js_api=Bridge())
    debug = True if sys.gettrace() else False

    set_login_callback(lambda x: print(x))

    webview.start(debug=debug)


if __name__ == '__main__':
    main()
