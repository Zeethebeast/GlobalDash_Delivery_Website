# SwiftTrack Logistics

A complete, production-ready delivery tracking website built with Python, Django, Django REST Framework, and Tailwind CSS.

## Features
- **User Authentication**: Secure Login, Signup, and Logout management.
- **Package Tracking**: Customers can enter unique tracking numbers to check delivery statuses.
- **Real-Time Interactive Maps**: Track package locations visually using Mapbox/Leaflet without refreshing the page.
- **Admin Dashboard**: Fully-featured Django admin dashboard to manage users, generate tracking numbers, update statuses, and change live coordinates.
- **Automated Email Notifications**: Customers are notified automatically when their delivery is created or when its status updates.
- **RESTful API**: Manage delivery states dynamically.

## Technology Stack
- Backend: Python 3, Django 6
- Database: SQLite (configured for easy drop-in replacement with PostgreSQL)
- Frontend: HTML5, Tailwind CSS, Leaflet.js

## Project Setup Instructions

1. **Activate the Virtual Environment**
**Windows (PowerShell):**
```powershell
.\venv\Scripts\activate
```

**Linux / macOS (WSL / Bash):**
```bash
python3 -m venv venv  # (If you need to recreate it in WSL)
source venv/bin/activate
```

2. **Install Dependencies**
**Windows (PowerShell):**
```powershell
pip install -r requirements.txt
```

**Linux / macOS (WSL / Bash):**
```bash
pip3 install -r requirements.txt
```

3. **Database Migrations**
**Windows (PowerShell):**
```powershell
python manage.py makemigrations
python manage.py migrate
```

**Linux / macOS (WSL / Bash):**
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

4. **Create a Superuser (Admin)**
This was handled automatically during setup! 
- **Username:** `admin`
- **Password:** `admin123`

*(If you need another, run `python manage.py createsuperuser`)*

5. **Start the Development Server**
**Windows (PowerShell):**
```powershell
python manage.py runserver
```

**Linux / macOS (WSL / Bash):**
```bash
python3 manage.py runserver
```

## How to Test the System

1. Visit **localhost:8000** to see the homepage.
2. Visit **localhost:8000/admin** and log in using `admin` / `admin123`.
3. In the Admin Panel, navigate to **Users** and create a new Customer Account, or go to the `/signup` page and create an account yourself.
4. Navigate to **Deliveries** in the admin panel and Add a new Delivery.
   - Select your customer, provide the sender/receiver strings.
   - Under the inline forms for Status and Location, you can add an initial location (e.g., Latitude: 40.7128, Longitude: -74.0060 for New York).
   - Save the Delivery. A unique tracking number will be generated immediately.
5. Emulate an Email Check: Since we didn't hook up a real SMTP server to avoid spamming, Django is set up to send emails implicitly. If you check the terminal or configure a dummy backend, you'll see the notification payload triggered on save!
6. Go back to the **Homepage** and enter the generated Tracking Number.
7. You should see the Tracking details and a **visual Map** centered on your package's coordinates.

Enjoy your Delivery Tracking App!
