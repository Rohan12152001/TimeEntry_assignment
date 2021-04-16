**Assumptions:**

1) All the users have 3 common projects: AWS, Heroku, GoogleCloud
> So users can choose any one project from the dropdown.
2) Users have to register with username & password 
3) The StartTime & EndTime are provided by the user 
4) The StartTime & EndTime can be set for the same day when the task was created

**How to configure the project on your Desktop/Laptop** 

1) Clone the project 

2) Install the dependencies from requirements.txt 

3) Using the terminal firstly migrate the databases using: 
    > python manage.py makemigrations 
                                                               
    > python manage.py migrate 
                                                            
4) Also, we will have to create a superuser to see the databases in Django Admin
    > python manage.py createsuperuser

5) Now, we are up and ready to start the server & and use the Web-app
    > python manage.py runserver 

