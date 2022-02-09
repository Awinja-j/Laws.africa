# leave request submission system

To Run this :-
          
 1. Clone this repo using htts or ssh, depending on your preference.

    ssh:

                          $ git clone git@github.com:Awinja-j/Law.africa.git

    http:

                          $ git clone https://github.com/Awinja-j/Law.africa.git
 
 2. cd into the created folder and install a virtual environment
 
                           $ virtualenv venv
                           
 3. Activate the virtual environment
 
                           $ source venv/bin/activate
                           
 3.  Install all app requirements
 
                          $ pip install -r requirements.txt  
  
 4. makemigrations
 
                          $ python3 leave/manage.py makemigrations
 
 5. migrate to database
 
                          $ python3 leave/manage.py migrate

 6. add dummy data
 
                          $ python3 leave/manage.py loaddata leave/data.json
  
 7. Runserver
 
                          $ python3 leave/manage.py runserver

 7. Run tests

                         $ python3 leave/manage.py test submission_app



Endpoints:

| HTTP REQUEST | URL             | PARAMS                                                                                                                                                                       |
|--------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GET          | /leave/         | N/A                                                                                                                                                                          |
| GET          | /leave/?pk=<id> | 3                                                                                                                                                                            |
| POST         | /leave/         | {      "leave_requester" :  "Gwen Doe" ,      "start_date" :  "2020-01-01" ,      "end_date" :  "2020-01-01" ,      "reason" :  "I need a vacation" ,      "status" :  "P" } |
| PUT          | /leave/?pk=1    | 3                                                                                                                                                                            |
| DELETE       | /leave/?pk=1    | 3                                                                                                                                                                            |