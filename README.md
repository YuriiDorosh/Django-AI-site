<div align="center">



</div>

## Chatty A.I.

![home_page](home_page.png)


### Cloning the repository

--> Clone the repository using the command below :

```bash
git clone https://github.com/YuriiDorosh/Django-AI-site.git

```

--> Move into the directory where we have the project files :

```bash
cd Django-AI-site

```

--> Create a virtual environment :

```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv venv

```

--> Activate the virtual environment :

```bash
# Windows
venv\scripts\activate
# Linux
source venv/bin/activate

```

--> Install the requirements :

```bash
pip install -r requirements.txt
```

### Set the project:

--> Create a file named .env in the root of the project 
and specify the necessary environment variables:

```bash
API_KEY = 'Your key' # The key from https://openai.com
SECRET_KEY = 'Django key'

```

### Apply migrations to the database:
```bash
python manage.py migrate

```


### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

Open a web browser and go to http://localhost:8000/ to view the site.


## Using


On the main page, you can select a programming language and enter a code to get its patch.

In the "Previous codes" section, you can view the history of entered codes and their corrections.

In the "Code explanation" section, you can enter the code and get an explanation of its operation.

### Making contributions
If you want to contribute to the project, please create a separate branch and submit a pull request with your suggestions.

### The authors

Me :)