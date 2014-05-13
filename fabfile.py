from __future__ import with_statement
from fabric.api import *

env.hosts = [
    'soda@novocasatudo.sodateste.com.br',
]
env.warn_only = True

def deploy():
    with cd('/deploy/sites/novocasatudo/novocasatudo'):
        # get lastest version from git
        run('git pull')
        run('../bin/pip install -r requirements.txt')
        run('../bin/python manage.py rebuild_index --settings=src.settings_production')
        # restart nginx
        run('supervisorctl restart novocasatudo')


def deploy_migrate():
    with cd('/deploy/sites/novocasatudo/novocasatudo'):
        # get lastest version from git
        run('git pull')
        run('../bin/pip install -r requirements.txt')
        run('../bin/python manage.py syncdb --settings=src.settings_production')
        run('../bin/python manage.py migrate --settings=src.settings_production')
        run('../bin/python manage.py rebuild_index --settings=src.settings_production')
        # restart nginx
        run('supervisorctl restart novocasatudo')