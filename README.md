# MySite - A Django Blog Project

## Overview
MySite is a Django-based blog project that allows users to create, edit, and delete posts. The application includes authentication, a rich text editor, and a user-friendly interface for managing blog content.

## Credits
Jose Portilla, Pierian Training.

## Features
- User authentication (Login, Logout, Signup)
- Create, read, update, and delete (CRUD) blog posts
- Rich text editor for blog content (CKEditor or MediumEditor)
- Static files management
- Bootstrap for responsive design

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.12+
- Django 4+
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps to Install
1. **Clone the repository:**
   ```bash
   git clone https://github.com/denismp/mysite.git
   cd mysite
   ```
2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
7. Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Configuration
### Static Files
Ensure static files are configured properly in `settings.py`:
```python
STATIC_URL = '/static/'
```
Run:
```bash
python manage.py collectstatic
```

### Logout Configuration
Ensure `LOGOUT_REDIRECT_URL` is set in `settings.py` to redirect users after logout:
```python
LOGOUT_REDIRECT_URL = '/'
```

## Usage
- **Creating a Blog Post:** Login and navigate to the dashboard to create a new post.
- **Editing a Blog Post:** Click on the edit button in the post list.
- **Deleting a Blog Post:** Click the delete button next to a post.

## Dependencies
- Django
- Django CKEditor (if using rich text editing)
- Bootstrap (for styling)

## Contributing
Pull requests are welcome. Please ensure new features are tested before submitting.

## License
This project is licensed under the MIT License.

## Contact
For any questions or issues, please reach out to [Denis M. Putnam](mailto:denis@example.com).

