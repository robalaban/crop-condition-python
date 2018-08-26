## Project Overview

Small Python Flask app, which connects to United States Dept. of Agriculture’s National Agricultural Statistics Service (NASS) [link](https://quickstats.nass.usda.gov/api), grabs the history of the measured condition of the corn crop in Kansas and writes it to a PostgreSQL database.

## Dependencies and Installation

#### Overview of architecture

The project is wrapped into two Docker containers, one for the database and the other a small alpine Linux installation with Flask.

#### Requirements

- Docker
- docker-compose

#### Installation

`git clone https://github.com/robalaban/crop-condition-python.git && cd crop-condition-python`

`docker-compose up --build`

## Working with the project

#### Accessing / Querying the database

`docker ps`

Check / note the ID for postgres container

`docker exec -it {CONTAINER_ID} bash`

`sudo su postgres`

`psql -d nass_crop_conditions_kansas`

`\dt` To view the database tables. Write queries here

## TODO

- Writing test cases
- Expand functionality to create database tables for each comodity
