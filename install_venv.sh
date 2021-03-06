#! /bin/bash

python3 -m venv flask
source flask/bin/activate
pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install guess_language
pip install flipflop
pip install coverage
tar -zxvf app/static/papers.tar.gz -C app/static
mv app/static/app/static/papers app/static
rm -r app/static/app
