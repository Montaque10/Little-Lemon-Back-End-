# Little Lemon Restaurant API

## Introduction/Overview
Little Lemon Restaurant API is a comprehensive backend system designed to manage restaurant operations, including menu management, table bookings, and user authentication. This Django-based REST API provides a robust foundation for restaurant management with features like menu item categorization, booking management, and secure user authentication.

## Key Features
- **User Authentication & Authorization**
  - Token-based authentication using Djoser
  - Role-based access control (Admin, Staff, Customer)
  - Secure user registration and login

- **Menu Management**
  - CRUD operations for menu items
  - Category-based organization
  - Price and inventory tracking
  - Featured items highlighting

- **Booking System**
  - Table reservation management
  - Guest information tracking
  - Special requests handling
  - Booking status management

- **Category Management**
  - Menu item categorization
  - Category-based filtering
  - Hierarchical organization

## Local Setup and Running Instructions

### Prerequisites
- Python 3.13 or higher
- Git
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Montaque10/Little-Lemon-Back-End-.git
   cd Little-Lemon-Back-End-
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```
   This creates an admin user for accessing the Django admin interface.

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

### Accessing the Application
- Admin Interface: http://127.0.0.1:8000/admin/
- API Root: http://127.0.0.1:8000/restaurant/api/
- API Documentation: http://127.0.0.1:8000/restaurant/api/docs/

## API Endpoints

### Authentication Endpoints
- `POST /restaurant/auth/users/` - Register new user
- `POST /restaurant/auth/token/login/` - Login and get token
- `POST /restaurant/auth/token/logout/` - Logout and invalidate token

### Menu Endpoints
- `GET /restaurant/api/menu-items/` - List all menu items
- `POST /restaurant/api/menu-items/` - Create new menu item (Admin only)
- `GET /restaurant/api/menu-items/<id>/` - Get specific menu item
- `PUT/PATCH /restaurant/api/menu-items/<id>/` - Update menu item (Admin only)
- `DELETE /restaurant/api/menu-items/<id>/` - Delete menu item (Admin only)

### Category Endpoints
- `GET /restaurant/api/categories/` - List all categories
- `POST /restaurant/api/categories/` - Create new category (Admin only)

### Booking Endpoints
- `GET /restaurant/api/tables/` - List all bookings
- `POST /restaurant/api/tables/` - Create new booking
- `GET /restaurant/api/tables/<id>/` - Get specific booking
- `PUT/PATCH /restaurant/api/tables/<id>/` - Update booking
- `DELETE /restaurant/api/tables/<id>/` - Delete booking

## Technologies Used
- **Backend Framework**: Django 5.2.2
- **REST API**: Django REST Framework
- **Authentication**: Djoser
- **Database**: SQLite (Development)
- **Image Processing**: Pillow
- **Python Version**: 3.13

## Project Structure
```
littlelemon/
├── littlelemon/          # Project configuration
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── restaurant/          # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── serializers.py   # API serializers
│   └── urls.py          # Application URLs
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details. 