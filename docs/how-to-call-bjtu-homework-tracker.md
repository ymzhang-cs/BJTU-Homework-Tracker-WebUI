# 如何调用 BJTU-Homework-Tracker 模块

## 说明

BJTU-Homework-Tracker 模块是一个用于查询北京交通大学（BJTU）学生作业信息的 Python 模块，使用 MIT 协议。源代码维护于 [ymzhang-cs/BJTU-Homework-Tracker](https://github.com/ymzhang-cs/BJTU-Homework-Tracker)，并且提供了 PyPI 包 [*尚未发布*]()。

## 安装

你可以选择通过仓库最新的 Release 提供的 `.whl` 文件进行安装 *，也可以通过 PyPI 进行安装* 。

1. 使用 `.whl` 文件进行安装

    从仓库的 Release 页面下载最新的 `.whl` 文件：[Release](https://github.com/ymzhang-cs/BJTU-Homework-Tracker/releases)

    切换到使用的 Python 环境，在 whl 文件路径下使用 `pip` 进行安装：

    ```bash
    pip install BJTU-Homework-Tracker-0.2.0-py3-none-any.whl
    ```

2. 使用 PyPI 进行安装

    *尚未发布*

## 使用

BJTU-Homework-Tracker 模块提供了全流程获取作业信息的子模块，主要包括：

- Login 模块，提供登录智慧课程平台的若干方法，如 Cookie 登录、MIS 登录、智慧课程平台账号密码登录等；
- Search 模块，提供从智慧课程平台获取作业信息的对象和模块，支持筛选，返回 json 形式的作业信息；
- Output 模块，提供将作业信息输出到文件、控制台等的方法。

对于本项目的开发者，一般使用 Login 模块和 Search 模块进行作业信息的获取。Output 模块一般情况下不被使用。

若要了解获取作业信息的全部流程，可以查看 BJTU-Homework-Tracker 模块的 `run.py`  文件。下面介绍实现功能的最小代码片段。

### 使用 Login 模块

下面介绍使用 Login 模块，通过智慧课程平台账号密码登录的方法。

```python
from BJTU_Homework_Tracker.Login import Login

login_method = 'cp'
login_args = {
    'student_id': '23333333',
    'password': 'pass:Bjtu@23333333'
    # or: 'password': 'hash:md5(Bjtu@23333333)'
}

login = Login(login_method)
login.login(**login_args)

# 获取登录后的 cookie
cookie = login.cookie
```

### 使用 Search 模块

下面介绍使用 Search 模块，通过 cookie 获取作业信息并进行筛选的方法。

```python
from BJTU_Homework_Tracker.Search import Search

search = Search(cookie)
search.search()     # 查询所有作业信息

# 筛选作业信息
select_args = {
    'course_positive_keyword': [],
    'course_negative_keyword': [],
    'finish_status': 'unfinished',
    'ignore_expired_n_days': 15,
    'ignore_unexpired_n_days': 90
}
search.select(**select_args)

# 获取作业信息
homework_info = search.homework_list
```

得到的 `homework_info` 是一个列表，每个元素是一个字典，包含了作业的信息。可以通过遍历列表，获取每个作业的信息。具体结构如下：

```python
[
    {
        "id": 90030,
        "create_date": "2024-09-12 12:57:58",
        "course_id": 112261,
        "course_sched_id": 0,
        "course_name": "计算机类专业导论",
        "comment_num": 0,
        "content": "<p>请按照附件要求完成。<\/p><p>不允许重逢提交。<\/p>",
        "title": "期末大作业",
        "user_id": 1491,
        "praise_num": 0,
        "is_fz": 0,
        "content_type": 0,
        "calendar_id": null,
        "end_time": "2024-11-04 00:00",
        "open_date": "2024-10-08 00:00",
        "score": "100",
        "moudel_id": 0,
        "isOpen": 2,
        "status": "1",
        "submitCount": 0,
        "allCount": 98,
        "excellentCount": 0,
        "is_publish_answer": null,
        "review_method": {
            "type": "0"
        },
        "makeup_flag": "0",
        "is_repeat": 0,
        "makeup_time": "",
        "snId": null,
        "scoreId": null,
        "subTime": null,
        "subStatus": "未提交",
        "return_flag": null,
        "return_num": 0,
        "is_excellent": "0",
        "stu_score": "未公布成绩",
        "refAnswer": "未公布答案",
        "pg_user_id": null,
        "pg_user_name": null,
        "returnContent": null,
        "lastScore": "未公布成绩"
    },
    ...
]
```

## 其他事项

未来 BJTU-Homework-Tracker 模块可能会提供更多的封装形式。欢迎关注仓库的 Release 页面，获取最新的版本信息。