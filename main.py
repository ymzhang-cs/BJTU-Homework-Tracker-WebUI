import webview

from bridge import Bridge


def main():
    window = webview.create_window("BJTU Homework Tracker", "web/dist/index.html", js_api=Bridge())
    webview.start()


if __name__ == '__main__':
    main()
