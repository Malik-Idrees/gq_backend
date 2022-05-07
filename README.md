## Installation

clone the repository. Create a virtual environment, so you have a clean python installation.

```
python -m venv venv
```

Activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

```
.\venv\scripts\activate
```

You can install all the required dependencies by running

```
pip install -r requirements.txt
```

Run database migrations

```
pip manage.py makemigrations
pip manage.py migrate
```

Run server

```
pip manage.py runserver
```
