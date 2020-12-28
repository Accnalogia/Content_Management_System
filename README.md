# Content_Management_System

The following project is made for Ajackus for the role of Software Development Engineer

The stack used is Django and the Api's are developed as per REST structure.

Firstly, a requirement.txt file is added. To download all the libraries used in the project please run "pip install -r requirements.txt". (Note: Not all files in the requirements file are used in the project)

In the configuration file for the project, the secret key is removed.

The project contains of 2 users, Author and Admin. Both use a single user model. Authors can are created using the apis. Author has access to register and login api. Author can register using their email Id and password.
Admin user can be created by using "python manage.py seed --mode=refresh". Below mentioned are the urls.

Register URL: BASEURL + '/core/register/'
Login URL: BASEURL + '/core/login/'
These API's provide Authentication token to access further API's

The content part of the system can be accessed by admin and author. Their workflow varies depending on their roles.
Author: Create, Read, Update, Delete their own contents
Admin: Read, Update, Delete contents posted throughout the system.

Author API's
post_content URL: POST: BASEURL + '/contentdata/content/'
list_content URL: GET: BASEURL + '/contentdata/content/'
get_content URL: GET: BASEURL + '/contentdata/content/<uuid:content_id>'
update URL: PATCH: BASEURL + '/contentdata/content/<uuid:content_id>'
delete URL: DELETE: BASEURL + '/contentdata/content/<uuid:content_id>'
post_content_category URL: POST: BASEURL + '/contentdata/content/<uuid:content_id>/add_category'

Admin API's
list_all_content URL: GET: BASEURL + '/contentdata/users/'
list_content URL: GET: BASEURL + '/contentdata/users/<uuid:user_id>/content'
get_content URL: GET: BASEURL + '/contentdata/users/<uuid:user_id>/content/<uuid:content_id>'
update_content URL: PATCH: BASEURL + '/contentdata/users/<uuid:user_id>/content/<uuid:content_id>'
delete_content URL: DELETE: BASEURL + '/contentdata/users/<uuid:user_id>/content/<uuid:content_id>'

API's for both
list_content URL: GET: BASEURL + '/contentdata/search/content/'

Please review the code and thanks.


