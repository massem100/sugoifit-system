# sugoifit-system

A Business Management System for small businesses to manage their
daily operations and keep track of their financials.

## Table of Contents

    - [Technologies](#technologies)
    - [Installation](#installation)
    - [How to Launch](#how-to-launch)
    - [Generating Data for Database](#generating-data-for-database)

### Technologies

    This project is built using: 
        - HTML 
        - CSS3/SCSS
        - Python 3.7.9 and above
        - Pip 20.1.1
        - Flask 1.1.2
        - Vue JS 2.9.6
        - NUXT JS 2.14.12
        - MySQL 
        - NPM 6.14.10
      Check requirements.txt file to see specific versions used. 

### Installation

    Brief instructions and links to downloading each language or framework

### Backend

    https://www.python.org/downloads/release/python-379/

#### Frontend

    https://nodejs.org/en/download/
    https://vuejs.org/v2/guide/installation.html
    https://cli.vuejs.org/guide/installation.html
    https://nuxtjs.org/docs/2.x/get-started/installation

#### Database

    https://dev.mysql.com/downloads/

### Install Python and PIP

    - Check if python is installed by typing python -V
    - If not, Download Python https://www.python.org/downloads/release/python-379/
    - Install by pip, by typing python get-pip.py in your terminal. 
      Use `pip -V` to verify successful installation. 
    - Also, ensure the Python path have been added to your system variables.

## How to Launch

The frontend setup is separated from the backend. Since it is separated, each will need to be launched in a separate terminal. Run the backend server before starting the frontend.

Create the venv folder inside the folder with frontend and backend.

### Creating a Python Runtime Environment

    - type python -m venv venv 
    - Activate  .\venv\scripts\activate on windows or source venv/bin/activate on MacOS or linux.
    - You should see (venv) at the start of your folder paths.
    - Deactivate your virtual environment 
      type deactivate or .\venv\scripts\deactivate or source venv/bin/deactivate
    - Remember to include your virtual environment folder, venv, in your .gitignore file.

### Frontend

    Launching the frontend 
    Type cd .\frontend/sugoifit-app or navigate to them one at a time. 
  
### install dependencies

      npm install

### serve with hot reload at localhost:3000

      npm run dev

### build for production and launch server

      npm run build
      $ npm run start

## Backend

    Launching the backend

### Installing the Requirements.txt file

    - While in an activated virtual environment, type pip install -r requirements.txt
    to install all packages for the project. 
    - To update/ export all installed packages installed in the environment to the requirements.txt file
     use the pip freeze > requirements.txt command.
     
    - run the development server by typing python run.py

## Generating Random Data for Database

## Faker Python Library

Faker Documentation
  <https://faker.readthedocs.io/en/master/>

### Installing Faker

        In activated virtual environment:
        -pip install faker 

### Import faker module

        - from faker import Faker

### Initialize a Faker generator

        fake = Faker()

Use the faker documentation for more instructions on how to use the library.

## Install Pandas

    Pandas Documentation 
    https://pandas.pydata.org/docs/index.html

### Installing Pandas

        In activated virtual environment:
        -pip install pandas

### Import pandas module

        import pandas as pd 

        'as pd' is not neccessary but a shortcut to avoid typing out the full word. 

## Actual Generation of Data

### Populate Table

    Create a data dictionary to store the data. 
        table_name = defaultdict(list)

#### Populate dictionary

    Set a loop to run for the number of records desired to populate table.
    Using the field names for the table as the keys of the dictionary append values 
    which match the data types for the fields. 

##### Call on fake.[faker provider] () in append bracket

    See example below:
        for _ in range(1,30):
    
            table_name["phone"].append(fake.phone())

##### Managing data that is outside of faker's scope

    Store a list of sample data and randomly pick a index to cycle through the list when appending. 

    service = ["Painting", "Plumbing", "Transporation", "Catering"]
     
    E.g.
    for _ in range(0,10):
        service["serv_name"].append(service[random.randint(0,2)])

##### Packaging data into pandas data frame

        A data frame is 2-Dimensional data structure resembling a table. 

        The below is used to convert the dictionary, table_name, created above to a data frame. 

        - df_table = pd.DataFrame(table_name)

### Use the sqlalchemy engine to connect to the db

    engine = create_engine('mysql://username:password@localhost/db', echo=False)

### Add the pandas dataframe to the database

    This tells pandas to convert the dataframe to sql and if the table already exists
    to append and if not create a new one. 

    df_table.to_sql('table_name', con=engine, index=False, if_exists = "append")

### Run the file

    python datascripts.py
