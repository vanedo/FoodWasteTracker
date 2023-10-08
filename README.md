# FoodWasteTracker
Food Waste Tracker - UN SDG Project \
The food waste tracker is a website for the community to track food waste, find food storage information and upcycling tips. You can contribute your food waste data and join our mission to reduce food waste today!

## Information
* Language: Python 3.8
* Framework: Django 4.2
* IDE: Visual Studio Code
* Operating system: Mac OS

## Clone repo
* Start by cloning this repository by typing this into command line:\
 `git clone https://github.com/vanedo/FoodWasteTracker.git`

## Set up virtual environment
* Navigate to the folder where the app is saved (you should see the `bin`, `lib`, `src` .. folders)
  * Hint: use `pwd` to check which working directory you're currently in.
  * Use `ls` to list out the files/folders in the current directory
  * `cd [directory name]` will move you into the directory
  * ` cd ../` will take you one folder up.
* You will need to set up a virtual environment to run this app \
`python3 -m venv .venv`
\
`source .venv/bin/activate`

## Install packages
* Make sure you have installed Django. Type the following into the command line:\
`pip install django`
* Install requirements \
`pip3 install -r requirements.txt`

## Run app
1. Run the following lines to start the app
Run this if it's the first time you've opened this app, or if you have made changes to the data model: \
`python manage.py makemigrations`
\
`python manage.py migrate`

2. You can just run this line otherwise:\
`python manage.py runserver`
