# team-Earth-GP
Introduction 
This project was meant to use a series of APIs to generate various “objects” depending on varied factors. For this we have developed four different applications API-colour, API-food, API-drink, and API-post. The application is run through Jenkins on port-8080 the code below is what is entered into the configuration tab.

```
#!/bin/bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv venv
activate () {
. venv/bin/activate 
}
activate
pip3 install -r api_colour/requirements.txt
```
This code here is the initial setup for the virtual environment as well as the installation of all the needed modules in the "pip3 install -r api_colour/requirements.txt". 

```
python3 -m pytest --cov-report term-missing --cov api_colour/application/ api_colour/testing/
python3 -m pytest --cov-report term-missing --cov api-food/application/ api-food/tests/
python3 -m pytest --cov-report term-missing --cov api-drink/application/ api-drink/tests/
python3 -m pytest --cov-report term-missing --cov api-post/application/ api-post/tests/
```
## Testing \
Testing was run via Jenkins and written in pytest. A coverage of 100% was achieved for each of the services, and thus 100% coverage was reached overall.
Whilst written as unit tests, due to the nature of the Flask microframework these tests can also be considered integration tests.
Get responses were mocked with patch and response from the native python library in order to test the services. \

## Unit Test


```
sudo docker-compose build 
sudo docker-compose push
sudo docker stack deploy --compose-file docker-compose.yaml flask-app
```
\
This is the final part which would first run all APIs together as a docker image it is then pushed to dockerhub and finally it is run using “sudo docker stack deploy --compose-file docker-compose.yaml flask-app”\
## API (food, drink and post):
Lists for Foods and Drinks are created on api-food and api-drink respectively. The method consists of a list of 5 objects, 5 for foods and 5 for drinks. From this list, one random object is selected using the random function, making a selection between an index of 0 and 4.
The response is then returned as plain text to ports 5001 (food) and 5050 (drink).
Service 1 (api_colour), makes post requests to Service 4 (api-post). Once the order, comprised of a food and drink is created, Service 4 returns a message based of this. It splits the overall Order back into the two parts that made it. The variables it breaks up into are equated to food and drink variables again and an output is based on the combination.
For example:
``` if food == "Apples" and drink == "Juice":
     return "Apple Juice would be nice"  ``` 

## Tech used \
Flask \
Ansible \
Docker \
Jenkins 

## The team 
Zake Ahmed- https://github.com/Zake-Ahmed \
Gregor rule- https://github.com/gregorule \
Gregory Laporta- https://github.com/laportag \
Christopher Aghedo- https://github.com/caghedo \
Afzal Kotadia- https://github.com/AfKot \
Dwayne Okoye-kachikwu- https://github.com/dokoye98 \

