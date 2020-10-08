# SailLogic2021
Navigation logic for the 2020/2021 season.

# Contributors
Mitch Broeders - 15mjlb@queensu.ca

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

# Testing
To test using REST endpoints use postman. You can also use curl if you would like but I've found it to be a nightmare.

1. Install Postman
2. Create a request by setting the body of the request (set as raw, with content type set to json) to something like
    {
    "commandID": "test1",
    "commandValue": "123"
    }  
3.  Set the request type to POST and the adddress to http://0.0.0.0:5000/sailLogicCommand
4.  Hit send, this should create a new object in the database with the values you sent. This should be viewable using sailcontrol.