# SailLogic2021
Navigation logic for the 2020/2021 season.
# TODO
Update this with anything you find useful. Especially solutions relating to setup.

# Setup
Heres how to get setup:

Install python 3.8.5 from (https://www.python.org/downloads/) and add to your PATH variable.

Install Docker desktop (will be used to support development databases.) from (https://docs.docker.com/get-docker/)

Install Node (https://nodejs.org/en/download/) we are using node as our front end framework.

In a shell run these commands to install dependencies.

    pip3 install pipenv
    npm install -g @angular/cli
    npm install --save-dev @angular-devkit/build-angular

To setup database using docker
    docker run --name sail_logic_db     -p 5432:5432     -e POSTGRES_DB=sail_logic     -e POSTGRES_PASSWORD=Sa1lL0gic     -d postgres

To tear down database
    docker ps -a 
        Get pid of database container
        docker rm {pid}
    Note: you should do this whenever you change the schemas

To run the backend
    ./bootstrap &