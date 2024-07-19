# VesselTracker 
- Track vessel and get voyage duration API.
- Under development: 
  - Login/Signup feature with user role based authentication.
  - UI implementation of whole project.
  - Parcel Tracking with Email.

## Project Setup
### Clone the repository & enter inside the project directory
```
git clone https://github.com/tanjil-dev/VesselTracker.git
```
```
cd VesselTracker
```
### create virtual environment
```
python -m venv [name]
```

### activate virtual environment(Windows)
```
.[name]\Scripts\activate.bat
```

### activate virtual environment(Linux & macOS)
```
source [name]/bin/activate
```

### install all requirements
```
pip install -r requirements.txt
```

### migration query into the default database
```
python manage.py migrate
```

### run server
```
python manage.py runserver
```

## PostgreSQL Download
- We will download and install postgresql into the local machine
- [Download Page](https://www.postgresql.org/download/)
## PostgreSQL with Django Application
- Please read [this tutorial](https://syscrews.medium.com/configure-postgresql-database-in-django-project-2ac706636fc7) and configure psycopg2-binary package within the project
- We will avoid putting the database credentials into the settings.py file. Because it will expose your database credential when we will upload code or host our project in public.
## Create .env file using CMD
- From project root directory we will enter the TodoApp directory.
```
cd WikiFilmScraper
```
- We will make a .env file.
```
touch .env
```
- Copy all the variables from the .sample_env file and paste it into the .env file
- Please put the variable values for database credentials and local directory path etc.

## Thank you!
Thank you for checking out this project! If you have any questions, feel free to open an issue or contact me directly. I hope you find this project helpful and look forward to your contributions.
- **Email:** tanzil.ovi578@gmail.com


### Happy coding!