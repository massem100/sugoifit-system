# sugoifit-system

A Business Management System for small businesses to manage their 
daily operations and keep track of their financials. 

# Table of Contents 
    
- [Technologies](#technologies)
- [Installation](#installation)
- [How to Launch](#how-to-launch)


# Technologies
This project is built using: 
    - HTML5 
    - CSS3/SCSS
    - Bootstrap 4
    - Python 3.7.9
    - Flask 1.1.2
    - Vue JS 2.9.6
    - MySQL 
    - Node JS
    - Webpack

# Installation 
Brief instructions and links to downloading each language or framework

to be added.

### Install Python and PIP
    - Check if python is installed by typing python -V
    - If not, Download Python https://www.python.org/downloads/release/python-379/
    - Install by pip, by typing python get-pip.py in your terminal. 
      Use `pip -V` to verify successful installation. 
    - Also, ensure the Python path have been added to your system variables.

# How to Launch

The frontend setup is separated from the backend. Since it is separated, each will need to be launched in a separate terminal and using ajax or fetch they will communicate.

Create the venv folder inside the folder with frontend and backend.

### Creating a Python Runtime Environment
    - In your command line, type python -m venv venv in the desired project folder. 
      (This will enable you to isolate your versions when working on multiple projects,
      by preventing the installation from being carried out at a global level.)
    - Activate your virtual environment by typing .\venv\scripts\activate on windows 
      and source venv/bin/activate on MacOS or linux.
    - You should see (venv) at the start of your folder paths.
    - Before closing your project or terminal, deactivate your virtual environment 
      by typing deactivate or more specifically .\venv\scripts\deactivate 
      or source venv/bin/deactivate
    - Remember to include your virtual environment folder, venv in your .gitignore file.
    

## Frontend
Launching the frontend 
  Type cd .\frontend/sugoifit-app or navigate to them one at a time. 
  - Run the development server by typing npm run dev

## Backend
Launching the backend
### Installing the Requirements.txt file 
    - While in an activate virtual environment, type pip install -r requirements.txt
    to install all packages for the project. 
    - To update/ export all installed packages to the requirements.txt file
     use the pip freeze > requirements.txt command.
     
    - run the development server by typing python run.py



