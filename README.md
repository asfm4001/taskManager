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

---
**ToC**
- [🎯 任務管理系統](#-任務管理系統)
  - [📖 Introduction](#-introduction)
  - [📹 Log](#-log)
  - [🚀 Features](#-features)
  - [📂 Project Structure](#-project-structure)
  - [🛠 Tech Stack](#-tech-stack)
  - [📦 Installation \& Run](#-installation--run)
  - [⚙️ Configurations](#️-configurations)
  - [📸 Demo](#-demo)
  - [🗺 API Documentation](#-api-documentation)
  - [📚 References](#-references)

## 📹 Log
* 2025.12.03 新增測試與CI
* 2025.11.28 略過第三方登入跳轉畫面


## 🚀 Features
1. 使用者登入、註冊
2. 任務、分類、標籤 CRUD，模型串連
3. REST API
4. 前端AJAX即時更新任務狀態
5. Signal寄信通知，使用console顯示

## 📂 Project Structure
```plaintext
.
├── .env
├── .github
│   └── workflows
│       └── ci.yml
├── README.md
├── db.sqlite3
├── requirements.txt 
├── pytest.ini
├── manage.py
├── templates
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
    │   ├── urls.py
    │   ├── views.py
    │   ├── static/
    │   ├── templates/
    │   ├── tests
    │       ├── __init__.py
    │       └── test_models.py
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
```
git clone https://github.com/asfm4001/taskManager.git
```

2️⃣ 建立env & 安裝套件
1. 建立虛擬環境
   ```
   python3 venv -m .venv
   ```
2. 進入虛擬環境
   ```
   source .venv/bin/activate
   ```
3. 安裝套件
   ```
   pip install -r requirements.txt
   ```
4. 測試[可選]
   ```
   pytest
   ```

3️⃣ 啟動專案
```
python manage.py runserver
```

🧪 測試帳號
* Test : test99/@WSX3edc
* Admin: admin/admin

## ⚙️ Configurations
略

## 📸 Demo
註冊
![註冊](/doc/register.png)
登入
![登入](/doc/login.png)
使用第三方憑證登入(Google)
![Google憑證登入](/doc/google_auth.png)
登入後轉至任務清單
![登入成功](/doc/login_success.png)
修改狀態後，mail給任務的擁有者
![console](/doc/notify_by_mail(console).png)

## 🗺 API Documentation
| Method | Endpoint                  | Description            | Auth |
|--------|---------------------------|------------------------|------|
| GET    | `v1/task/`                | 取得所有任務             | No   |
| GET    | `v1/task/<int:pk>/`       | 取得指定任務資料          | No   |
| GET    | `v1/category/`            | 取得所有分類             | No   |
| GET    | `v1/tag/`                 | 取得所有標籤             | No   |

## 📚 References
略