# birthday-project
To run this project please follow the instructions. 
1. Create a python3 virtualenv and active this environment
2. Run pip install -r requirements.txt
3. Create a database on postgresql
4. Run python manage.py makemigration ( here I already added migrations file so you can skip this step )
5. Run python manage.py migrate
6. To add cron tab Rub python manage.py crontab add
7. This cron tab will call every midnight at 12.10 am to send mail all customers who's are bithday today.
8. After sending mail it will store reports those customer records
9. To stop cron tab RUn python manage.py crontab remove
10. To Run the project type python manage.py runserver
