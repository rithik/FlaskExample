# Getting Started with Flask

## Setup

### Step 1

Fork this repository on GitHub.

### Step 2

Clone your forked repository to your local file system.

### Step 3

Update runtime.txt to the version of python you are using. You can find out the version by using `python -V` or `python3 -V` (for Python3). Your runtime.txt file should look like `python-<VERSION NUMBER>`.

### Step 4

Rename the `secret.py.example` file to the `secret.py`. Use `cp secret.py.example secret.py` or `mv secret.py.example secret.py`. Add in appropriate variables. Make sure to change the `SECRET_KEY` field.  

### Step 5

Add all required python packages and libraries to the `requirements.txt` file. Use `pip freeze > requirements.txt`.

### Step 6

Create the database. 

First, install PostgreSQL by going to [https://www.postgresql.org/download/](https://www.postgresql.org/download/). 

Once PostgreSQL is installed, create a new database. You can do this by running `psql`. This will open up a new shell to access the database. Next, create the database by running `CREATE DATABASE DATABASE_NAME;`, replacing `DATABASE_NAME` with your database name. Exit the shell by typing `\q`. 

Change the DB_URL value in your `secret.py` file to use the following format: `postgresql://localhost/DATABASE_NAME`. 

When you are using a cloud based database (such as Google Cloud or AWS), use the following connection string: `postgresql://USERNAME:PASSWORD@IP_ADDRESS/DATABASE_NAME`.

### Step 7

Add necessary code to your project.

All CSS files should be added to the `static/css` folder. All JavaScript file should be added to the `static/js` folder. All images should be added to the `static/img` folder.

As you add code to the `static/css`, `static/js` and `static/img` folders, you can remove the `.gitignore` files in these folders.

All HTML files should be added to the `templates` folder.

All views should be added to the `app.py` file.

All models should be added to the `models.py` file.

### Step 8

Run the development Flask Server by typing `./run.sh dev`. A server will start running and will be up at http://localhost:5000/. 

Run the production Flask server by typing `./run.sh prod`. By default, the script will use `gunicorn` to start the server with four workers and will be hosted on port 5000.

## Things to remember

You should not share your `secret.py` file with anyone.

Do not change the `manage.py` file.

You should not commit your database file to GitHub.

The `Procfile` is necessary if you are deploying to Heroku.

Do not change the `database.py` file.

## Database Setup

In order to get the database fully functional, run `./manage.py db init` to get the database running.

Every time you modify your models, run the following two commands in the following order:
```
./manage.py db migrate
./manage.py db upgrade
```

## Shell Access

In order to get access to the shell, run `./manage.py shell`. This will open a shell without any imports.

In order to modify database entries (rows), once the shell opens run the following lines:
```
from app import db
from models import _
```
where the _ should be replaced by all of the models you wish to import.

## Deploying to Heroku

### Step 1

Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

### Step 2

Run the following command to login to Heroku: `heroku login`.

### Step 3

Setup the git repo by running `git init`.

### Step 3

Run the following command to create a new app: `heroku create APP_NAME`.

### Step 4

Go to the Heroku Dashboard and click "Configure Add Ons". Then click "Find More Add-ons". Search for "Heroku Postgres" and click on it. Then click install. This will configure the database to the Heroku app.

### Step 5

Go to the settings tab and click "Reveal Config Vars". Add all of the variables that are listed in the `secret.py` file.

### Step 6

Run `git push heroku master` to push your code base to Heroku.

### Step 7

Navigate to `https://APP_NAME.herokuapp.com`.

### Step 8

If you need to re-deploy, run the following set of commands:
```
git add .
git commit -m "COMMIT MESSAGE"
git push heroku master
```
