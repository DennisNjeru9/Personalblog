## Project Name 
**the_Phi Construction Blog**

## Author 
**Dennis Njeru**

## Description 
- This is is a personal blogging website focusing on the construction industry, where the owner can post and share his opinions in construction topics and projects. Additionally other users can read and comment on the topics.

## User Story in Pictures
####  User view
* User can view the blog posts on the site
* User can see random quotes on the site
* User can view the most recent posts
* User can subscribe to blog mailing list and receives an email alert when a new post is made.
* User can comment on blog posts

####  Writer view
* Sign in to the blog.
* Publish a blog from the application.
* Delete comments that I find problematic
* Update or delete blogs I have created.

## Technologies Used
* Python 
* Flask 
* PostgreSQL 
* SQLAlchemy
* HTML5  
* CSS3
* Bootstrap  

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file.

    ## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/DennisNjeru9/Personalblog.git'**.
* **Step 2** : Go to the project root directory and install the virtualenv library using pip and afterwards create a virtual environment. Run the following commands sequently:
    * **`python3 -m venv virtual`**
    * **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL databse client.
* **Step 5** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
    * Create a file in your root directory called start.sh and store a generated SECRET key like so **`export SECRET_KEY="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`** 
* **Step 6** : On your terminal, run the following command, **`chmod a+x start.sh`**
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.
    * You can run tests by changing the configuration in manage.py (**'app = create_app('test')'**) and run **'python3 manage.py test'** command in the terminal.

## Known Bugs
* On creating a new post, a subscribed user wil receive a notification email. However, the page will display an error when redirecting the writer to the post page. This feature has been temporarily disabled due to this -- FIXED

## Contacts 
Email: dennis.njeru@student.moringaschool.com
LinkedIn: https://www.linkedin.com/in/dennis-gitonga-227246193/

## live link 
https://thephiconstructionblog.herokuapp.com/

## License
[GNU GPL v3.0](./LICENSE)

Copyright (c) [2021] **Dennis Njeru**