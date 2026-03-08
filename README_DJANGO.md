# Smokey Peeks - Django Integration

Your Smokey Peeks website is now integrated with Django.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run migrations (creates database):**
   ```bash
   python manage.py migrate
   ```

3. **Collect static files (for production):**
   ```bash
   python manage.py collectstatic
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. Open **http://127.0.0.1:8000/** in your browser.

## URL Structure

| Page | URL |
|------|-----|
| Home | `/` |
| Menu | `/menu/` |
| Location | `/location/` |
| Reservation | `/reservation/` |
| Events / Promos & Merch | `/events/` |
| About Us | `/about/` |
| Admin Dashboard | `/admin-dashboard/` |
| Log Admin | `/logadmin/` |
| BBQ & Beer | `/bbq-beer/` |
| Live Music | `/live-music/` |
| Live Sports | `/live-sports/` |
| Merch | `/merch/` |
| Django Admin | `/admin/` |

## Project Structure

```
Smokey Peeks Web/
├── manage.py              # Django CLI
├── smokey_peeks/          # Project config (settings, urls)
├── main/                  # Main app
│   ├── templates/main/    # HTML templates
│   ├── static/main/       # CSS, images
│   │   ├── css/
│   │   └── img/
│   ├── views.py           # Page views
│   └── urls.py            # URL routing
├── requirements.txt
└── db.sqlite3             # Database (after migrate)
```

## Images

Ensure your `img/` folder contents are copied to `main/static/main/img/`. If you have images in the root `img/` folder, run:

```powershell
Copy-Item -Path img\* -Destination main\static\main\img\ -Recurse -Force
```

## Next Steps

- **Django Admin**: Create a superuser with `python manage.py createsuperuser` to access `/admin/`
- **Reservations**: Add a `Reservation` model and connect the reservation form to save to the database
- **Authentication**: Add login protection for the admin dashboard
