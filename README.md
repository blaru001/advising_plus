# advising_plus
Advising office software created for Software Engineering 1

##How do I get set up?
* install python 3.5.2

* install pip3 

* clone the repository

* install postgresql
 
  * [Setup Postgres for
Django](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
  *  substitute these values in the tutorial 
    * DatabaseName: advising_plus 
    * username : ap_admin 
    * Password: temp 
* set up a virtual environment for python
  * pip3 install virtualenv
  * create a virtual env
    * virtualenv name_of_environment 
  * activate your virtual env
    * source name_of_environment/bin/activate
    * when your done programming use the command deactivate to exit virtual env
* install dependencies
  * pip install -r requirements.txt
* Migrate database
   * python manage.py makemigrations
   * python manage.py migrate


## Dependencies
  * python 3.5.2
  * virtualenv
  * django-1.10.3
  * psycopg2-2.6.2
  * postgresql-9.5
