from __future__ import with_statement
from fabric.api import *

env.hosts = [
    'ubuntu@150.165.15.94:9022',
]
env.warn_only = True

def deploy():
    with cd('/opt/dragoesdomar'):
        # get lastest version from git
        run('git pull')
        run('../venvs/dragoesdomar/bin/pip install -r requirements.txt')

        # restart
        run('killall python')
        run('../venvs/dragoesdomar/bin/python manage_production.py runfcgi host=127.0.0.1 port=8080')
        run('sudo service nginx restart')


#def deploy_migrate():
