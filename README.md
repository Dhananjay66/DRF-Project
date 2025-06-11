# 🚀 DRF Basics Project

[![Stars](https://img.shields.io/github/stars/Dhananjay66/DRF-Project)](https://github.com/Dhananjay66/DRF-Project/stargazers)
[![Forks](https://img.shields.io/github/forks/Dhananjay66/DRF-Project)](https://github.com/Dhananjay66/DRF-Project/fork)

A beginner-friendly project to help you learn and understand the fundamentals of **Django REST Framework (DRF)** — covering everything from basic APIs to serializers, views, authentication, and more.

---

## 📚 What You'll Learn

- 🔹 Django REST Framework setup & configuration  
- 🔹 API views: `APIView`, `ViewSet`, `GenericAPIView`  
- 🔹 Serializers & ModelSerializers  
- 🔹 CRUD operations (Create, Read, Update, Delete)  
- 🔹 Authentication (Token/JWT)  
- 🔹 Permissions & throttling  
- 🔹 Pagination & filtering

---

## 🌍 Live Demo

🔗 **Live URL** : [Click Here](https://your-render-app-name.onrender.com)


## ⚙️ Setup Instructions

Follow these steps to get the project up and running locally:

---

### 🧾 1. Clone the Repository

```bash
git clone https://github.com/Dhananjay66/DRF-Project.git
cd DRF-Project
````

---

### 🧪 2. Create & Activate Virtual Environment

```bash
python -m venv venv
# For Linux/Mac
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

---

### 📦 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔧 4. Apply Migrations & Run Server

```bash
python manage.py migrate
python manage.py runserver
```

---

🎉 You're all set! Open your browser and go to `http://127.0.0.1:8000/` to see it live.



---

## 📦 API Endpoints

| Method | Endpoint                  | Description                 |
| ------ | ------------------------- | --------------------------- |
| GET    | `/api/v1/employees/`      | List all employees          |
| POST   | `/api/v1/employees/`      | Create a new employee       |
| GET    | `/api/v1/employees/{id}/` | Retrieve a single employee  |
| PUT    | `/api/v1/employees/{id}/` | Update an existing employee |
| DELETE | `/api/v1/employees/{id}/` | Delete an employee          |

> 🔐 **Authentication required** for certain routes (if implemented).

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 📁 Project Structure

```DRF-Project/
│
├── manage.py
├── db.sqlite3
├── requirements.txt # List of all Python dependencies
│
├── Django_Rest_Main/ # Main project configuration
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
│
├── api/ # Shared logic or general APIs
│ ├── admin.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│ └── migrations/
│
├── students/ # App for managing student data
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ └── migrations/
│
└── employees/ # App for managing employee data
├── models.py
├── views.py
├── admin.py
└── migrations/
```

---

## ✨ Useful Commands

```bash
# Create superuser for admin access
python manage.py createsuperuser

# Create migrations
python manage.py makemigrations
python manage.py migrate
```

---

## ❤️ Contributing

Contributions, issues and feature requests are welcome!
Feel free to check the [issues page](https://github.com/Dhananjay66/DRF-Project/issues).

---

## 🧑‍💻 Author

**[@Dhananjay66](https://github.com/Dhananjay66)**

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

