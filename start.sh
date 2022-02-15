export SQLALCHEMY_DATABASE_URI='postgressql+psycopg2://ann:db_password@localhost:pitch'
export MAIL_USERNAME='annngurewanjiku@gmail.com'
export MAIL_PASSWORD='0705351175'
export SECRET_KEY='12345'
export FLASK_ENV='development'
export FLASK_APP=run

#source start.sh
# flask db init >>>> to create a migrations folder
# flask run >>>> to run the app
# flask db migrate >>>> to make migrations
# flask db upgrade >>>> to create tables in the db
python3 run.py server