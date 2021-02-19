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
    - Flask 
    - Vue JS 
    - MySQL 
    - Webpack

# Installation 
Brief instructions and links to downloading each language or framework

### Install Python and PIP
    - Check if python is installed by typing __`python -V`__
    - If not, Download Python https://www.python.org/downloads/release/python-379/
    - Install by pip, by typing __`python get-pip.py`__ in your terminal. 
      Use `pip -V` to verify successful installation. 
    - Also, ensure the Python path have been added to your system variables.

# How to Launch

### Creating a Python Runtime Environment
    - In your command line, type __`python -m venv venv`__ in the desired project folder. 
      (This will enable you to isolate   your versions when working on multiple projects,
      by preventing the installation from being carried out at a global level)
    - Activate your virtual environment by typing __`.\venv\scripts\activate`__ on windows 
      and __`source venv/bin/activate`__ on MacOS or linux.
    - You should see (venv) at the start of your folder paths.
    - Before closing your project or terminal, deactivate your virtual environment 
      by typing __deactivate__ or more specifically __`.\venv\scripts\deactivate`__ 
      or __`source venv/bin/deactivate`__
    - Remember to include your virtual environment folder, venv in your .gitignore file.
    

### Installing the Requirements.txt file 
    - While in an activate virtual environment, type __pip install -r requirements.txt__ 
    to install all packages for the project. 
    - To update/ export all installed packages to the requirements.txt file
     use the __pip freeze > requirements.txt__ command.
     


