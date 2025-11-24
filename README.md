# 🎯 任務管理系統
使用者可登入/註冊，並可新增任務，將任務新增一個分類與多個標籤。同時有API可查詢任務、分類、標籤。
前端修改狀態時，可即時使用API更新後端資料庫。修改狀態的同時亦有mail給任務的建立者。

## 📖 Introduction
測試**當前Django實踐能力**，學習依**概括描述的功能**再**開發並實踐**。
Features為ChatGPT生成內容，開發中除了基礎功能外，額外學習以下內容

📝 初次使用功能
* Javascript從cookies中獲得CSRF Token
* AJAX 串連後台API
* 將mail輸出至console中，避免**真正**寄出信件

## 🚀 Features
1. 使用者登入、註冊
2. 任務、分類、標籤 CRUD，模型串連
3. REST API
4. 前端AJAX即時更新任務狀態
5. Signal寄信通知，使用console顯示

## 📂 Project Structure
```plaintext
.
├── README.md
├── db.sqlite3
├── requirements.txt 
├── manage.py
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── apps
    ├── __init__.py
    ├── api
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   └── migrations/
    ├── task
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── mail.py
    │   ├── signal.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   ├── static/
    │   ├── templates/
    │   ├── migrations/
    │   └── models
    │       ├── __init__.py
    │       ├── category.py
    │       ├── tag.py
    │       └── task.py
    └── users
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── forms.py
        ├── migrations/
        ├── models.py
        ├── templates/
        ├── tests.py
        ├── urls.py
        └── views.py
```

## 🛠 Tech Stack
* 語言: Python
* 框架: Django
* 前端: Bootstrap 4
* DB:  SQLite

## 📦 Installation & Run
1️⃣ 下載專案
`git clone https://github.com/asfm4001/taskManager.git`

2️⃣ 建立env & 安裝套件
1. `python3 venv -m .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`

3️⃣ 啟動專案
`python manage.py runserver`

🧪 測試帳號
* Test : test99/@WSX3edc

## ⚙️ 設定 Configurations
略

## 📸 Demo
略

🗺 API Documentation
| Method | Endpoint                  | Description            | Auth |
|--------|---------------------------|------------------------|------|
| GET    | `v1/task/`                | 取得所有任務             | No   |
| GET    | `v1/task/<int:pk>/`       | 取得指定任務資料          | No   |
| GET    | `v1/category/`            | 取得所有分類             | No   |
| GET    | `v1/tag/`                 | 取得所有標籤             | No   |

## 📚 參考資料 References
略