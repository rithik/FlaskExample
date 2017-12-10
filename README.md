# Getting Started with Flask

## Step 1

Fork this repository on GitHub. Next, clone your forked repository to your local file system.

## Step 2

Create a `secret.py` file from the `secret.py.example` file.

## Step 3

Add necessary code to your project. All CSS, JS and image files should be added to `Static` Folder. All HTML files should be added to the `Templates` folder. All views should be added to the `app.py` file. All models should be added to the `models.py` file.


## Things to remember

#### You should not share your `secret.py` file with anyone.
#### Do not change the `manage.py` file.
#### You should not commit your database file to GitHub.
#### The `Procfile` is necessary if you are deploying to Heroku.
#### Change the `runtime.txt` file to the appropriate version of Python.
#### You should not need to change the `database.py` file.
#### If you need additional libraries not included in the `requirements.txt` file, you may use the command `pip install <LIBRARY NAME>`. Once this is done, use the command `pip freeze > requirement.txt` to overwrite the existing `requirements.txt` file.
