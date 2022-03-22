## NEIGHBORWATCH

### Created on 22/3/2022

* By Winifred Mwikali Kyalo

### Description

A web application that allows one to be in the loop about everything happening in one's neighbourhood. It has A section for post where the latest happenings are posted. It has contact information for Police and health services.

* User Stories
* User Can :-

* Sign in with the application to start using.
*Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.
* Access the website
* Need the latest browser to be able to View


It is hosted by heroku

### Setup and Installation

To get the project .......

* Clone Repository:
<https://github.com/mwikalikyalo/NeighborWatch>
* Install and activate Virtual Enviroment envneighbour
* cd Neighbour  && python3 -m venv envneighbour && source neighbour/bin/activate
* Install Dependencies
* pip install -r requirements.txt
* Setup Database
* SetUp Database User,Password, Host then following Command

* Create .env file

  SECRET_KEY='<SECRET_KEY>'
  DEBUG=True
  DB_NAME='database name'
  DB_USER='database user'
  DB_PASSWORD='password'
  DB_HOST='127.0.0.1'
  MODE='dev'
  ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
  DISABLE_COLLECTSTATIC=1

  EMAIL_USE_TLS=True
  EMAIL_HOST='.gmail.com'
  EMAIL_PORT=587
  EMAIL_HOST_USER='email'
  EMAIL_HOST_PASSWORD='email-password'
* python manage.py makemigrations neigbour
* Now Migrate
* python manage.py migrate
* Run Application
* python3 manage.py server
* Test Application
* python manage.py test neighbour
* Open the application on your browser 127.0.0.1:8000.

### Technology used

* HTML
* CSS
* Bootstrap
* Git
* Python Django Framework


Heroku

### Bugs

None at the Moment

### Contact Details

Email: winniemwikali07@gmail.com

#### Copyright (c) 2021 Winifred Mwikali Kyalo

### License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.