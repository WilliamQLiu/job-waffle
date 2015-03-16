"""
    Fabfile lets us run a script to deploy our Django app onto AWS EC2 server
    For now these are just reminders of what commands are mostly used
    Run on server like so:
    $fab -H localhost,linuxbox host_type
 """

import boto, boto.ec2
from fabric.api import run, cd, env, prompt, put, sudo, local
from fabric.contrib.files import exists

### Configuration


def setup_instance():
    """ Set up an Amazon EC2 instance using the Linux AMI """
    print "TO DO"
    pass


### Server Tasks
def update_requirements():
    """ Update requirements.txt on local server """
    run('cd /opt/job-waffle')
    run('pip freeze > requirements.txt')


def aptget_update():
    """ Get the latest updates to the server"""
    run('sudo apt-get update')


def aptget_upgrade():
    """ Upgrade the latest upgrades """
    run('sudo apt-get upgrade')


def restart_server():
    """ Restart the entire server """
    reboot(wait=30)  # wait in seconds


def start_nginx():
    """ start nginx """
    run('sudo service nginx start')


def activate_virtualenv():
    """ Activate virtualenv """
    with cd('~'):  # Go to directory
        run('source /opt/job-waffle/bin/activate')


def start_gunicorn():
    """ Start gunnicorn with 6 workers """
    activate_virtualenv()
    run('cd /opt/job-waffle')
    run('gunicorn jobwaffle.wsgi:application --bind 10.1.1.7:8000 -w 6')


def see_gunicorn_processes():
    """ See all gunicorn processes """
    run('ps ax|grep gunicorn')


def kill_gunicorn_processes():
    """ Kill all gunicorn processes """
    run('pkill gunicorn')


### Django Stuff Below
def install_project_requirements():
    """ Make sure requirements are installed """
    run('cd /opt/job-waffle')
    activate_virtualenv()
    run('pip install -r requirements.txt')


def git_fetch_code():
    """ Get latest code from git """
    run('git fetch --all')
    # Will be prompted username and password
    run('git reset --hard origin/master')


def syncdb():
    """ Sync the database in case models changed """
    run('cd /opt/job-waffle')
    run('python manage.py syncdb')


if __name__ == '__main__':

    boto.set_stream_logger('boto')  # debug logging

    ### Connect to services and authorize
    try:
        s3_conn = boto.connect_s3()
        ec2_conn = boto.ec2.connect_to_region("us-east-1d")

    except "NoAuthHandlerFound":
        print "Check your login creditials at ~/.boto config file"

    update_requirements()
    aptget_update()
    aptget_upgrade()
    restart_server()

    # Change settings.py DEBUG=False, TEMPLATE_DEBUG=False
    # Change settings.py DATABASE
    #activate_virtualenv()
    git_fetch_code()  # Get latest GitHub code
    install_project_requirements()
    syncdb()
    start_nginx()
    start_gunicorn()
