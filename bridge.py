import time

from login import login_via_mis


class Bridge:
    def listAllHomework(self):
        time.sleep(1.0)
        return [
            {'courseName': '数字电路基础', 'title': '实验1', 'submitStatus': '1/3'},
            {'courseName': '数字电路进阶', 'title': '实验2', 'submitStatus': '1/6'}
        ]

    def loginViaMis(self):
        login_via_mis()