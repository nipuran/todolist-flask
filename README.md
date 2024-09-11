# todolist-flask

A simple to-do list application built with Flask. This app demonstrates basic CRUD (Create, Read, Update, Delete) operations.

## Features

- **User Authentication**: Includes login, registration, password reset, and OTP verification.
- **To-Do List**: A dashboard interface that allows users to manage a to-do list, with functionalities for creating, editing, and deleting tasks.


## Getting Started

### Prerequisites

- Python 3.x
- Flask and related dependencies (see `requirements.txt`)


### Installation

1. Clone the repository:
```bash
git clone https://github.com/nipuran/todolist-flask.git
cd todolist-flask
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up environment variables (e.g., secret keys, database URI).
4. Run the application:
```bash
python run.py
```


## Code Structure


```
todolist-flask/
.
├── README.md
├── app
│   ├── __init__.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   └── styles.css
│   │   └── templates
│   │       ├── forget_password.html
│   │       ├── register_user.html
│   │       ├── reset_password.html
│   │       ├── user_login.html
│   │       └── verify_otp.html
│   ├── config.py
│   ├── dashboard
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   └── styles.css
│   │   └── templates
│   │       ├── dashboard.html
│   │       └── edit.html
│   ├── extensions.py
│   ├── home
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── static
│   │   │   └── styles.css
│   │   └── templates
│   │       └── home.html
│   ├── models.py
│   └── utils.py
└── run.py
```
