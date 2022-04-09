# ka-chat
This is a simple chat app

## what is ka-chat
This is a simple chat app, the intention is to make this the backend for the app, it is going to utilize flask to serve the natural web requests and anything that needs long-polling and websockets is going to be handled by eventlet which will work hand in hand with flask-socketio which handles socket connections to implement the realtime effect.

## Setup and installation
Ofcourse if you would like to give this app a run then the first step is to fork or clone this app and then follow the below steps.

1. Set up virtualenv
    This will create a virtual environment that will leave your global python installation as pristine as possible. It is a good habit to get into I mean the one of using virtual environments for all apps that you make.

   ```bash
        virtualenv venv
   ```

2. Activate virtualenv 

   ```bash
      LINUX/MAC

      . venv/bin/activate

      WINDOWS

      . venv\Scripts\activate
      
   ```

3. Install dependencies

   ```bash
        pip install -r requirements.txt
   ```

4. Database configuration.

   The project uses PostgreSQL to persist data and if you wish to use the same you can [get it here](https://www.postgresql.org/download/) ,it supports different Operating Systems just follow the prompts for the different cases, depending on your operating system. To make your life easier you will also want to install pgAdmin it is an Open Source postgres administration platform, rather you will use it to create and manage database instances for Postgres, I highly suggested you install that also and if sold on it you can [get it here](https://www.pgadmin.org/download/)

   Once you have successfully installed both then, Create both **ka_chat** and **ka_chat_test_db** databases on pgAdmin - their usage is straight forward I believe. After creating databases then run the below command, it will apply the migrations to the database.

   ## .env file example

   Before finishing up on the database part, you will want to create a **.env** file in the root of your project and below is an example of it's contents.

   ```bash
      FLASK_APP = wsgi.py
      FLASK_DEBUG = 1
      FLASK_ENV = "development"
      SECRET_KEY = "yoursecretkey"
      SENDGRID_KEY = "sendgrid api key to assit in sending emails"
      DATABASE_URL = "postgres://postgres:{your postgres password}@localhost/todos"
      TEST_DATABASE_URL= "postgres://postgres:{your postgres password}@localhost/todos_test_db"
      VERIFY_EMAIL_URL= "{url for your frontend app}/verify"
      PASSWORD_RESET_URL = "{url for your frontend app}/reset"
   ```

   Once you are done with the **.env** file then you can run the below commands

   ```bash
      flask db init

      flask db migrate -m "initializing the database"
    
      flask db upgrade
   ```

5. Running tests 

You can run tests to assertain that the setup works

   ```bash
      python -m pytest --cov=app/api
   ```

6. Start the server

   ```bash
      flask run or python wsgi.py 
   ```

<details>
<summary>ka-chat endpoints</summary>

METHOD       | ENDPOINT      |  DESCRIPTION
------------ | ------------- | ------------
POST  |  /users/signup  | signup a user
POST  |  /users/verify  | verify a user email
POST  |  /users/signin  | signin a user
POST  |  /users/forgot  | send reset password link
PUT   |  /users/update-password |change/update a user password



</details>

<details open>

Incase of a bug or anything else use any on the below channels to reach me

[Find me on twitter](https://twitter.com/kabakiantony) OR  drop me an email at kabaki.antony@gmail.com.

