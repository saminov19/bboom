Django Blog App
This is a Django web application that implements a simple blog, including user authentication and API endpoints.

Features
User registration and authentication.
Adding, listing, and deleting posts.
API endpoints to retrieve user lists, user posts, create new posts, and delete posts.
Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/django-blog-app.git
cd django-blog-app
Install the required packages:
Copy code
pip install -r requirements.txt
Apply the database migrations:
Copy code
python manage.py migrate
Create a superuser (for admin access):
Copy code
python manage.py createsuperuser
Run the development server:
Copy code
python manage.py runserver
The app will be accessible at http://127.0.0.1:8000/.

API Documentation
The API endpoints provided by this app can be accessed using the following URLs:

User List API: /api/users/ (GET)
User Posts API: /api/users/<user_id>/posts/ (GET)
Create Post API: /api/posts/ (POST)
Delete Post API: /api/posts/<post_id>/ (DELETE)
Please refer to the API section above for more details about each endpoint.

Usage
Access the app in your web browser at http://127.0.0.1:8000/.

Register as a new user or log in with your existing account.

After logging in, you can add new posts, view your posts, and delete your posts.

To access the API endpoints, use the URLs provided above in API Documentation section.

Testing
To run the unit tests for the app, use the following command:

bash
Copy code
python manage.py test
