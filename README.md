# Dynamic_Web_Application
![code coverage badge](https://github.com/d-alfa/Dynamic_Web_Application/actions/workflows/Continuous_Integration.yaml/badge.svg)
![code coverage badge](https://github.com/d-alfa/Dynamic_Web_Application/actions/workflows/Unit_tests.yaml/badge.svg)

## Overwiew

Web application with index, sign up and login page.
Home page currently in progress!!!

## Requirements

- Python
- Django

## Features

- Index page
  - Redirection to signup page
  - Redirection to login page
- Sign up page
  - Show/hide icon for password visability
  - Error handling (Passwords do not match)
  - Error handling (Username already exists)
- Login page
  - User authentication
  - Show/hide icon for password visability
  - Error handling (Invalid login credentials)
- Home page (under construction!!!)

## Installation

**1. Clone repository:**

```bash
git clone https://github.com/d-alfa/Dynamic_Web_Application.git
```
**2. Navigate to the scripts directory:**

```bash
cd Dynamic_Web_Application/scripts
```
**3. Run setup.sh script for quicker project setup:**

```bash
./setup.sh
```

## Usage

**1. Navigate to the Project directory:**

```bash
cd Dynamic_Web_Application/Project
```
**2. Run server:**

```bash
python3 manage.py runserver
```
**3. Access website:**

```bash
localhost:8000
```
