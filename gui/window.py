import sys
import re
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout,
                             QWidget, QPushButton, QTabWidget, QLabel, QScrollArea,
                             QGroupBox, QHBoxLayout, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QFont, QColor, QPalette, QBrush
from PyQt5.QtCore import Qt


import sys
import re
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout,
                             QWidget, QPushButton, QTabWidget, QLabel, QScrollArea,
                             QGroupBox, QHBoxLayout, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QFont, QColor, QPalette, QLinearGradient
from PyQt5.QtCore import Qt


class PyqtMainWindow(QMainWindow):
    def __init__(self, homework_list, display_elements=None):
        super().__init__()
        self.homework_list = self.preprocess_homework_list(homework_list)
        self.display_elements = display_elements or {
            "course_name": "课程名称",
            "title": "作业标题",
            "content": "作业说明",
            "submitCount": "已提交人数",
            "allCount": "总人数",
            "open_date": "发布日期",
            "end_time": "截止日期",
            "subStatus": "提交状态"
        }
        self.initUI()

    def preprocess_homework_list(self, homework_list):
        def remove_html_tags(text):
            clean_text = re.sub(r'<.*?>', '', str(text))
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()
            return clean_text

        processed_list = []
        for homework in homework_list:
            processed_homework = {}
            for key, value in homework.items():
                processed_homework[key] = remove_html_tags(value)
            processed_list.append(processed_homework)

        return processed_list

    def initUI(self):
        # 设置窗口基本属性
        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle('作业信息中心')

        # 设置全局背景渐变
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(240, 244, 250))
        gradient.setColorAt(1, QColor(220, 230, 240))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        # 创建中央窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建垂直布局
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # 创建选项卡控件
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabBar::tab {
                background-color: #4A90E2;
                color: white;
                padding: 12px 20px;
                font-size: 16px;
                font-weight: bold;
                border-top-left-radius: 15px;
                border-top-right-radius: 15px;
                min-width: 120px;
                margin-right: 5px;
            }
            QTabBar::tab:selected {
                background-color: #357ABD;
                color: white;
            }
            QTabBar::tab:hover {
                background-color: #6AB0FF;
            }
        """)

        # 按课程名称分组作业
        grouped_homework = self.group_homework_by_course()

        # 为每个课程创建一个标签页
        for course_name, homeworks in grouped_homework.items():
            # 创建滚动区域
            scroll_area = QScrollArea()
            scroll_content = QWidget()
            scroll_layout = QVBoxLayout()
            scroll_layout.setSpacing(15)

            for homework in homeworks:
                group_box = self.create_homework_group_box(homework)
                scroll_layout.addWidget(group_box)

            scroll_layout.addStretch(1)
            scroll_content.setLayout(scroll_layout)
            scroll_area.setWidget(scroll_content)
            scroll_area.setWidgetResizable(True)

            # 将滚动区域添加到标签页
            self.tab_widget.addTab(scroll_area, course_name)

        # 创建关闭按钮
        close_button = QPushButton('关闭')
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #FF6B6B;
                color: white;
                padding: 12px 20px;
                font-size: 16px;
                border: none;
                border-radius: 10px;
                font-weight: bold;
                transition: all 0.3s ease;
            }
            QPushButton:hover {
                background-color: #FF4757;
                transform: scale(1.05);
            }
        """)
        close_button.clicked.connect(self.close)

        # 添加控件到布局
        main_layout.addWidget(self.tab_widget)
        main_layout.addWidget(close_button)
        main_layout.setContentsMargins(20, 20, 20, 20)

    def group_homework_by_course(self):
        # 按课程名称分组作业
        grouped = {}
        for homework in self.homework_list:
            course_name = homework.get('course_name', '其他')
            if course_name not in grouped:
                grouped[course_name] = []
            grouped[course_name].append(homework)
        return grouped

    def create_homework_group_box(self, homework):
        # 创建带阴影的分组框
        group_box = QGroupBox()
        group_box.setStyleSheet("""
            QGroupBox {
                border: none;
                border-radius: 15px;
                background-color: white;
                margin-top: 10px;
                padding: 15px;
            }
        """)

        # 为 group_box 添加阴影效果
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 50))
        shadow.setOffset(0, 5)
        group_box.setGraphicsEffect(shadow)

        layout = QVBoxLayout()
        layout.setSpacing(10)

        # 遍历display_elements中的字段
        for key, display_name in self.display_elements.items():
            value = homework.get(key, '')
            if value:  # 只显示非空的信息
                label = QLabel(f"{display_name}: {value}")
                label.setFont(QFont('微软雅黑', 10))
                label.setStyleSheet("""
                    color: #333333;
                    padding: 5px;
                    border-bottom: 1px solid #E0E0E0;
                """)
                label.setWordWrap(True)
                layout.addWidget(label)

        group_box.setLayout(layout)
        return group_box


def show_homework_window(homework_list, display_elements=None):
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # 使用更现代的界面风格
    main_window = PyqtMainWindow(homework_list, display_elements)
    main_window.show()
    sys.exit(app.exec_())


# 使用示例
# if __name__ == '__main__':
#     # 示例数据
#     homework_list = [
#         {"title": "数学作业", "deadline": "2024-02-15", "content": "解答习题1-10"},
#         {"title": "英语作业", "deadline": "", "content": "阅读理解"}
#     ]
#
#     display_elements = {
#         "title": "作业标题",
#         "deadline": "截止日期",
#         "content": "作业内容"
#     }
#
#     show_homework_window(homework_list, display_elements)