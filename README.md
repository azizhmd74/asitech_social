# Asitech Social Network

A mini social network built with Django, featuring user registration, post creation, comments, and a like system. This project allows users to interact with posts and share their thoughts.

## Features

- **User Registration:** Users can register and create an account.
- **Login/Logout:** Secure user authentication with a custom login and logout functionality.
- **Profile Management:** Users can view and edit their profile.
- **Post Creation:** Users can create new posts and view a list of all posts.
- **Commenting System:** Users can comment on posts and view comments from other users.
- **Like System:** Users can like any post, with the ability to see the list of users who liked a post.
- **Timestamps:** Each post and comment displays the creation date and time.
- **Responsive Design:** The project is designed to be presentable and user-friendly.

## Technologies Used

- Python 3.x
- Django 5.1.1
- HTML/CSS
- JavaScript
- SQLite (or any other database of your choice)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/azizhmd74/asitech_social.git
   cd asitech_social
   
2-    
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3-install requirements 
pip install -r requirements.txt

4-Apply migrations:
python manage.py make migrations
python manage.py migrate

5-Run the development server:
http://127.0.0.1:8000/social/

# Asitech Social Network - URL List

This document provides a list of URLs for the Asitech Social Network project, along with descriptions of their functionalities.

## URL Links

- **User Registration:**  
  [http://127.0.0.1:8000/registration/](http://127.0.0.1:8000/registration/)  
  *Allows new users to register for an account.*

- **User Login:**  
  [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)  
  *Allows users to log into their account.*

- **User Profile:**  
  [http://127.0.0.1:8000/social/profile/](http://127.0.0.1:8000/social/profile/)  
  *Displays the user's profile information.*

- **Post List and Creation:**  
  [http://127.0.0.1:8000/social/](http://127.0.0.1:8000/social/)  
  *Displays a list of all posts and provides a form for creating new posts.*

- **Post Detail:**  
  [http://127.0.0.1:8000/social/post/<post_id>/](http://127.0.0.1:8000/social/post/<post_id>/)  
  *Displays a specific post along with its comments.*

- **Add Comment:**  
  [http://127.0.0.1:8000/social/add_comment/<post_id>/](http://127.0.0.1:8000/social/add_comment/<post_id>/)  
  *Provides a form to add comments to a specific post.*

## Conclusion

These URLs facilitate navigation through the Asitech Social Network, enabling users to register, log in, manage posts, and interact with content.



