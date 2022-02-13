from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Server
from app import create_app
from app import db 
from app.models import User,Post,Comment

app= create_app('development')


migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def add_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Comment': Comment}


if __name__=='__main__':
    app.run()