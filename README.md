# django-app

# This is the django backend server for React App.

# Below are some steps to configure django server..
Note- This dajngo backend server is used for storing excel data in django model(sqlite)..

step-1:- First, replicate this project to your local machine using git command. Here is the github repo link..
        https://github.com/surya1-git/django-app.git .
        
step-2:- After clonnig project in local machine, go to project directory and open the terminal for installing necessary
        python packages. For this first we need to create virtual environment, where we will run our django server.
        Below are some required commands to setup environment for project...
        To create virtual environment, use below command
        - virtualenv env (Note:- virtualenv should be install on your computer. if it is not installed. First install virtualenv using 'pip intsall virtualenv'.)
          This command will create virtual environment as env.
          Activate this env and install all required libraries..
        - pip install -r requirements.txt
          This will install all required python packages..
         (Note- Here we do not have to do migrations, As we are using dbsqlite. So we can directly use that file as database.)
         
step-3:- Run django server using below command 
        python manage.py runserver.
        It will start the django server on port 8000.
        
If you want see excel data in django datbase. Go to admin panel, using http://127.0.0.1/admin url..
login as admin and password is also admin..If will find CsvData model there...
        
Now we can use our React app. (Note- Both server should be on running mode..)
