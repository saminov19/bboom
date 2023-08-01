# Django Blog App

This is a Django web application that implements a simple blog, including user authentication and API endpoints.

## Features

- User registration and authentication.
- Adding, listing, and deleting posts.
- API endpoints to retrieve user lists, user posts, create new posts, and delete posts.

## Installation

1. Clone the repository to your local machine:

markdown
Copy code
git clone https://github.com/saminov19/django-blog-app.git
cd django-blog-app


2. Install the required packages


3. Apply the database migrations:

python manage.py migrate


4. Create a superuser (for admin access):

python manage.py createsuperuser



5. Run the development server:
python manage.py runserver

markdown
Copy code

The app will be accessible at `http://127.0.0.1:8000/`.

## API Documentation

The API endpoints provided by this app can be accessed using the following URLs:

- User List API: `/api/users/` (GET)
- User Posts API: `/api/users/<user_id>/posts/` (GET)
- Create Post API: `/api/posts/` (POST)
- Delete Post API: `/api/posts/<post_id>/` (DELETE)

Please refer to the API section above for more details about each endpoint.

## Usage

1. Access the app in your web browser at `http://127.0.0.1:8000/`.

2. Register as a new user or log in with your existing account.

3. After logging in, you can add new posts, view your posts, and delete your posts.

4. To access the API endpoints, use the URLs provided above in the API Documentation section.

## Testing

To run the unit tests for the app, use the following command:
python manage.py test


