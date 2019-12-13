# SSTI-on-FLASK-Jinja2
Example of SSTI using Flask and Jinja2

To run application you need Flask and Python3 installed.
Install Flask: https://python-scripts.com/install-flask-green-unicorn-on-ubuntu (without Gunicorn)
Run Flask project:

For Linux and Mac:

$ export FLASK_APP=flaskproj
$ export FLASK_ENV=development
$ flask init-db
$ flask run

For Windows cmd, use set instead of export:

> set FLASK_APP=flaskproj
> set FLASK_ENV=development
> flask init-db
> flask run

flasproj - route to application directory
development - route to virtual environment directory
