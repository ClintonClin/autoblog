# Auto Blog!
This is a blog application that allows users to write blogs for people to see.

#### By **[Clinton Okerio](https://github.com/ClintonClin)**

## Description
This applicaton is meant to help users post their blogs online and can be deletedas per wish.
 

## Prerequsites
    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo
    - Install python 3.6
    - Run chmod a+x start.py
    - Run ./start.py
    - pip3 install -r requirements (dependencies)

## Technologies used

    - Python 3.6
    - HTML
    - Bootstrap
    -Postgresql

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blogger'
export SECRET_KEY='Your secret key'
```
### The application does use Postgresql. To Run database Migrations, run the following: 
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```
### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

### [License](LICENSE)

Copyright 2018 CLINTON OKERIO

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) **Clinton Okerio**