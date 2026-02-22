# Django Contact Portal

A lightweight web application built with Python and Django.

## About This Project
This project was developed as a technical exercise to demonstrate the rapid transition of skills from **Java Spring** and **.NET** to **Python Django**. It implements a full MVT (Model-View-Template) pattern.

## Features
- **Django ORM**: Managed SQLite database integration.
- **Django Forms**: Implemented server-side validation and CSRF protection.
- **Template Inheritance**: Used a `base.html` architecture for DRY frontend code.
- **Admin Interface**: Fully configured Django Admin for record management.

## How to Run
1. Clone the repo: `git clone <your-url>`
2. Create virtual env: `python -m venv .venv`
3. Activate env: `.venv\Scripts\activate` (Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`
