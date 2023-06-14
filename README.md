# Tracking Exchanges Data ETL Process and Dashboard
> This application shows the process of data flow from the source to visualizations. 


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Contact](#contact)

## General Information
- This project was created because I wanted to learn...
- Data source: [here](https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data?select=indexProcessed.csv)


## Technologies Used
- Python - version 3.10.6
- Pandas - version 1.5.3

## Features
List the ready features here:
- Creating s3 bucket in AWS,
- Creating S3 bucket connection with app,
- Creating Pandas dataframe with data from s3 bucket,
- Creating database instance Microsoft SQL Server in AWS RDS,
- Creating connection with AWS SQL Server from api,
- Creating database and tables from api with Python,
- Loading data to database and check database in Azure Data Studio,

## Screenshots
![Example screenshot](/app/static/func-diagram.png)

## Setup
For starting application with docker you need [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/).


## Usage
The application can be built from sources or can be run in docker.

##### Build from sources
```bash
$ # Move to directory
$ cd folder/to/clone-into/
$
$ # Clone the sources
$ git clone https://github.com/mateuszgua/tracking-exchanges-ETL-dashboard.git
$
$ # Move into folder
$ cd tracking-exchanges-ETL-dashboard
$
$ # Create virtual environment
$ python3 -m venv venv
$
$ # Activate the virtual environment
$ source venv/bin/activate
$
$ # Install requirements.txt file
$ pip install -r requirements.txt
$
$ # Start app
$ flask --app app.py run
$ # ...
$ # * Running on http://127.0.0.1:5000 
```


## Project Status
Project is: in_progress



## Contact
Created by [@DevGua](https://devgua-portfolio.web.app/) - feel free to contact me!
