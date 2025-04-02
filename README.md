# Django Summarization App

## Overview
This is a Django-based web application that allows users to input text and receive a summarized version along with extracted keywords. The application also supports user authentication and stores summaries in a database.

## Features
- User authentication (login/logout)
- Text summarization
- Keyword extraction
- Database storage for summaries

## Installation
### Prerequisites
Make sure you have the following installed:
- Python 3
- pip (Python package manager)
- Git
- PostgreSQL or SQLite (for database management)

### Setup Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AshrafJB2/AKAsummary
   cd AKAsummary
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Contributing
Feel free to fork this project and submit pull requests!

## License
This project is licensed under the MIT License.

