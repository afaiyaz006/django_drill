# django_drill
A repository I have created to practice and learn about python django.
# To test run the project
First of all clone the whole project
```bash
git clone https://github.com/afaiyaz006/django_drill
```

Now change directory

```bash
cd django_drill
```

Create a virtual enviroment
```bash
pipenv shell
```

Install the requirements

```bash
pip install -r requirements.txt
```

Now, apply necessary  migrations

```bash
python django_practice/manage.py migrate

```

Finally to start the project

```bash
python django_practice/manage.py runserver
```

This will start a webserver on 127.0.0.1:8000. So navigate to http://127.0.0.1:8000