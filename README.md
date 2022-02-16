# PITCH
## Developer
Ngure Ann

## Description
In life, you only have 60 seconds to impress someone. 1 minute can make or break you. How do we make sure that you use your 1 minute to actually say something meaningful?
This application allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
#### Link to deployed site
https://makeyou.herokuapp.com/


#### Technologies used
    - Python 3
    - HTML
    - Heroku
    - Postgresql
    -SQLAlchemy


#### get project from github .
```bash
https://github.com/annngure/Pitch.git
```

#### Create and activate the virtual environment
```bash
python3 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```


#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE tutorial;
```

#### Make and run migrations
```bash
python3 run.py make migrations && python3 run.py migrate
```

#### Run the app
```bash
./start.sh
```
Open [localhost](http://127.0.0.1:5000/)


## Bugs
#### Known bugs
 - none yet


## Support and contact details
Contact [Ngure Ann](annngurewanjiku@gmail.com) for further help/support

### License
MIT

Copyright (c)2022 **Ngure Ann**