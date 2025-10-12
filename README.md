# django-announcements-site

Minimal Django project for a class assignment. Features:
- Home (`/`)
- Announcements list (`/announcements/`)
- Announcement detail with JS Read more / Show less toggle
- Announcement model + Admin panel

## Run locally (Linux/macOS/Windows with Python 3.8+)

1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate    # Windows (PowerShell)
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the server:
   ```bash
   python manage.py runserver
   ```

5. Visit:
   - http://127.0.0.1:8000/ (home)
   - http://127.0.0.1:8000/announcements/ (list)
   - http://127.0.0.1:8000/admin/ (admin panel to add announcements)
