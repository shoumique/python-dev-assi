# Country API and Web App

A Django-based web application that fetches country data from the REST Countries API, exposes RESTful endpoints, and provides a secure web interface with authentication.
Features include country search, detailed views, region-based filtering, authentication-protected API access, and user login/logout functionality.

## Features

- Fetches data from `https://restcountries.com/v3.1/all`
- Stores country information in a local database
- RESTful API with full CRUD support + search, regional and language-based filters
- Web interface with search and detail views
- User authentication for access control (login required)
- Bootstrap-based responsive UI

## Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- Bootstrap 5

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/shoumique/python-dev-assi.git
cd python-dev-assi
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

> Basic dependencies you need:
>
> * Django >= 5.2
> * djangorestframework >= 3.16.0

---

## Database Setup

1. **Apply Migrations**

```bash
python manage.py migrate
```

2. **Create a Superuser**

```bash
python manage.py createsuperuser
```

Follow the prompts to set up an admin user.

3. **Fetch Country Data**

```bash
python manage.py fetch_countries
```

---

## Running the Application

```bash
python manage.py runserver
```

Visit:

* Web Interface: [http://localhost:8000/web/](http://localhost:8000/web/)
* API Endpoints: [http://localhost:8000/api/countries/](http://localhost:8000/api/countries/)

---

# Authentication Guide

All API endpoints require authentication.

## 1. Methods Supported:

| Method                 | Description                                             |
| :--------------------- | :------------------------------------------------------ |
| Session Authentication | Login via `/accounts/login/` and use session cookies.   |
| Basic Authentication   | Pass username and password via HTTP Basic Auth headers. |

---

## 2. Authenticate via Web Login (SessionAuth)

* URL: [http://localhost:8000/accounts/login/](http://localhost:8000/accounts/login/)
* Use your Django superuser/admin credentials.
* Once logged in, you can browse the Web app and access API endpoints from the same session.

---

## 3. Authenticate via BasicAuth (API Testing)

Example `curl` call:

```bash
curl -u your_username:your_password http://localhost:8000/api/countries/
```

Or configure Basic Auth in Postman for testing.

---

# API Endpoints Documentation

## Country APIs

| Endpoint                                   | Method             | Description                                                         |
| :----------------------------------------- | :----------------- | :------------------------------------------------------------------ |
| `/api/countries/`                          | GET / POST         | List all countries or create a new country.                         |
| `/api/countries/search/?search=term`       | GET                | Search countries by name.                                           |
| `/api/countries/<cca3>/`                   | GET / PUT / DELETE | Retrieve, update, or delete a specific country using its CCA3 code. |
| `/api/countries/region/<region>/`          | GET                | List all countries in the same region.                              |
| `/api/countries/language/<language_code>/` | GET                | List countries speaking a specific language.                        |

---

# Web Pages

| Page           | URL                  | Purpose                                                     |
| :------------- | :------------------- | :---------------------------------------------------------- |
| Country List   | `/web/`              | View all countries in a table, search countries.            |
| Country Detail | `/web/<country_id>/` | View country details, same-region countries, and languages. |
| Login          | `/accounts/login/`   | Login page.                                                 |
| Logout         | `/accounts/logout/`  | Logout and redirect to login.                               |

---



