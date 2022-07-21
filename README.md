# team-Earth-GP
Introduction 
This project was meant to use a series of APIs to generate various “objects” depending on varied factors. For this we have developed four different applications API-colour, API-food, API-drink, and API-post. The application is run through Jenkins on port-8080 the code below is what is entered into the configuration tab.
///
#!/bin/bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv venv
activate () {
. venv/bin/activate 
}
activate
pip3 install -r api_colour/requirements.txt
///
This code here is the initial setup for the virtual environment as well as the installation of all the needed modules in the "pip3 install -r api_colour/requirements.txt". 
///
python3 -m pytest --cov-report term-missing --cov api_colour/application/ api_colour/testing/
python3 -m pytest --cov-report term-missing --cov api-food/application/ api-food/tests/
python3 -m pytest --cov-report term-missing --cov api-drink/application/ api-drink/tests/
python3 -m pytest --cov-report term-missing --cov api-post/application/ api-post/tests/
///
Next is the testing for each API “python3 -m pytest --cov-report term-missing” this shows not only which methods work but also the percentage of what methods are tested, our coverage is 100%. 
///
sudo docker-compose build 
sudo docker-compose push
sudo docker stack deploy --compose-file docker-compose.yaml flask-app
///
This is the final part which would first run all APIs together as a docker image it is then pushed to dockerhub and finally it is run using “sudo docker stack deploy --compose-file docker-compose.yaml flask-app”
API drink- this is a random String generator with the fields 'Juice', 'Milkshake', 'Smoothie', 'Coffee', 'Iced Tea' the purpose of this application would be to one of the variables and post it on the webpage. The string is placed in a list which is made into the variable drinks, it is then selected as a random number between 0 and 4 -> “randomnum = random.randint(0,4)”.
API food-this API runs on the same code as API drink with the same number of fields they are 'Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries'.
API colour- this API is service 4 which is the combination of API food and drink.

API post-###
Tech used 
Flask
Ansible 
Docker
Jenkins

The team
Zake Ahmed 
Gregor rule
Gregory Laporta 
Christopher Aghedo
Dwayne Okoye-kachikwu
