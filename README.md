#### Please, use your real email for registration (for password restore functionality)
##### [**@wannagooutbot**](https://t.me/wannagooutbot) - bot for notifications
##### JSON file with requests list for Postman is provided
#
### Installation
```sh
git clone https://github.com/RedSSD/SolidWay-test-task
cd /project_directory/
sudo docker compose up --build
```
##### Server is available at ```0.0.0.0:8000```
#
##### PgAdmin4 is available at ```0.0.0.0:5050```

###### PgAdmin email: admin@admin.com
###### PgAdmin password: admin
#
#
##### Data for PostgreSQL db connection in PgAdmin
###### Host: db
###### Port: 5432
###### Username: postgres
###### Password: postgres
#
#
#
#### Authentication + credentials change requests
Registration - POST request ```/auth/users/```
Login - POST request ```/auth/token/login/```
Logout - POST request ```/auth/token/logout/```
Set email - POST request ```/auth/users/set_email/```

### Password recovery
1) POST request to ```/auth/users/reset_password/```
2) You will receive a link to your email like 
```sh
http://localhost:8000/password/reset/confirm/NA/c9p7rc-4c03c3c79729ce95d529f2fce6f11d26
```
3) Put "NA" as uid parameter to request body WITHOUT quotation marks
4) Put "c9p7rc-4c03c3c79729ce95d529f2fce6f11d26" as token parameter WITHOUT quotation marks
5) Input new password and send request

## User requests
User profile - GET request ```/me```
User profile change - PATCH request ```/me/```
User avatar delete - DELETE request ```/me/delete_avatar/```
User profile delete - DELETE request ```/me/```
#
##### Article is able to store simple text or HTML (if article have images, links, etc.)
##### To check this functionality create a superuser log in to Django admin panel.
#
```sh
sudo docker ps -a
// copy id of the solidway-test-task-api docker container (example: 04a98b163b45)
sudo docker exec -it "hash" bash
// inside container run: 
python3 manage.py createsuperuser
```
## Article requests

Article list - GET request ```/articles/```
3rd Party article list - GET request ```/3rd-party-articles/```
Article detail view - GET request ```/articles/<int:article_id>```
Article list - GET request ```/articles/```
Create article - POST request ```/articles/create/```
Update article - PATCH request ```/articles/<int:article_id>```
Delete article - DELETE request ```/articles/<int:article_id>```
