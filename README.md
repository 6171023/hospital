# hospital

Hospital Reservation System in Django

## Features
- Reservation System 
  - General User (Patient) can reserve a doctor
  - That doctor can accept/decline the reservation

- Doctor Filter System
  - User can filter by gender and minimum years of experience of a doctor

## How to Setup
- Have Python 3 installed (preferably Python 3.10)

- Install pip requirements (inside your preferred virtual environment):
`pip install -r requirements.txt`

**Django setups:**

- Create (Migrate) the database:
`python manage.py migrate`

- Create a superuser:
`python manage.py createsuperuser`

- Run the server:
`python manage.py runserver`

- Feel free to create Doctor users in the admin panel, and the sign up some General Users to test out the querying system and reservation system, Have Fun!

Note that there is no landing page for an admin user, so to logout with that you have to navigate to `<url>/admin/` manually


## Future Goals
- Cloud-Hosting (Heroku, etc)
- CSS Designs