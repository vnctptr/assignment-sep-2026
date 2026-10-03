# Product Search
## Vincent Potrykus

A Django app for searching and filtering products. Products can be filtered by category and tag. The filter, category and
tag queries can be combined.

### Assumptions
For the purpose of this assignment I assumed that only one category and one tag can be selected at a time.

Products can be searched by description only. They cannot be searched by name as per the "Search and Filter Functionality" section in assignment description _Create a simple HTML page that allows users to: Search products by description._

### Stack
- Database: Django's builtin SQLite
- Frontend: Django's builtin templates

### Setup
#### 1 Clone the repository
```commandline
git clone https://github.com/vnctptr/assignment-sep-2026.git
cd assignment-sep-2026
```
#### 2 Install python

Install python and activate it. Python 3.14 and pyenv are recommended.
```commandline
pyenv install 3.14
pyenv local 3.14
```

#### 3 Create a virtual environment

Create the environment and activate it.
```commandline
python -m venv .venv
source .venv/bin/activate
```

#### 4 Install dependencies
```commandline
python -m pip install Django
```

#### 5 Start the development server
```commandline
python manage.py runserver
```
Go to the link shown in the terminal (most likely http://127.0.0.1:8000/)

#### Password
If you need to access the admin portal at http://127.0.0.1:8000/admin here are the credentials:

username: `vincentpotrykus`

password: `password`

### Tests
To run tests run this command in the assignment-sep-2026 directory:
```commandline
python manage.py test 
```

### AI Usage
I used AI mostly for minor autocompletion. For example:
```python
name = models.CharField(max_length=200) # the part after "models.Char" was autocompleted by Copilot
```

Some repetitive snippets were also autocompleted, for example:
```html
<h4>Name: {{ product.name }}</h4>
<p>Description: {{ product.description }}</p> 
```