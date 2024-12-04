import time

from login import login_via_mis, LogginStatus


class Bridge:
    def __init__(self):
        self.login_status = LogginStatus.NOT_LOGGED_IN

    def listAllHomework(self):
        time.sleep(1.0)
        return [
            {'courseName': '数字电路基础', 'title': '实验1', 'submitStatus': '1/3'},
            {'courseName': '数字电路进阶', 'title': '实验2', 'submitStatus': '1/6'}
        ]

    def loginViaMis(self):
        def callback(status):
            self.login_status = status
        self.login_status = LogginStatus.LOGGING_IN
        login_via_mis(callback)

    def loginViaCookies(self, cookies):
        self.login_status = LogginStatus.LOGGED_IN

    def loginViaCoursePlatform(self, account, password):
        self.login_status = LogginStatus.LOGGED_IN

    def getLoginStatus(self):
        return self.login_status

    def logout(self):
        self.login_status = LogginStatus.NOT_LOGGED_IN