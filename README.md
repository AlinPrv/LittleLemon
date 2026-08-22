# LittleLemon

# LittleLemon Restaurant API - Endpoints for Testing

Base URL: http://127.0.0.1:8000/

## MENU API

GET /restaurant/menu/items - List all menu items
POST /restaurant/menu/items - Create a new menu item
GET /restaurant/menu/items/<id> - Retrieve a single menu item
PUT /restaurant/menu/items/<id> - Update a menu item
DELETE /restaurant/menu/items/<id> - Delete a menu item

## TABLE BOOKING API (requires authentication)

GET /restaurant/booking/tables/ - List all bookings
POST /restaurant/booking/tables/ - Create a new booking
GET /restaurant/booking/tables/<id>/ - Retrieve a single booking
PUT /restaurant/booking/tables/<id>/ - Update a booking
DELETE /restaurant/booking/tables/<id>/ - Delete a booking

Note: Booking endpoints require a valid authentication token.
Obtain a token via POST to /api-token-auth/ with username and password.

## USER REGISTRATION & AUTHENTICATION (Djoser)

GET /auth/users/ - List registered users
POST /auth/users/ - Register a new user
POST /auth/token/login/ - Log in and obtain auth token
POST /auth/token/logout/ - Log out (invalidate token)
POST /api-token-auth/ - Obtain auth token (alternative endpoint)

Example request body for /auth/users/ (POST):
{
"email": "test@example.com",
"username": "testuser",
"password": "yourpassword123"
}

Example request body for /api-token-auth/ (POST):
{
"username": "testuser",
"password": "yourpassword123"
}

## ADMIN PANEL

/admin/ - Django admin interface (superuser login required)
