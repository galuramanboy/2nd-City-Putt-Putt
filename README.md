# 2nd-City-Putt-Putt

## Usage

### Requirements

- Docker (<https://www.docker.com/products/docker-desktop>)

- docker-compose (<https://docs.docker.com/compose/install/>)

### Starting/Stopping the Application

To launch, run the following in the root directory:

```bash
docker-compose -f docker/docker-compose.yml up -d
```

The website can then be accessed in a local web browser at
<http://localhost:8000/>

To shut down the application run the following:

```bash
docker-compose -f docker/docker-compose.yml down
```

### Building the Docker Image

docker-compose will build the image automatically, but you can also
build the image without using docker-compose. To do so, run the
following in the root directory:

```bash
docker build -f docker/Dockerfile .
```

## Development

When the application is launched with docker-compose all edits you make
to code will be live updated. This means that there is no need to
restart the containers while developing the django application.

That being said, any changes to the environment (including installing
new Python modules) will require the image to be rebuilt.


# Sprint 1 README

## Version Control Procedures
The team will use GitHub to track changes to the system from start to finish. Team members must submit pull requests which must be approved by another team member. 

## Stack
Web Framework: Django
Frontend Library: Bootstrap
Database: Postgres
Continuous integration and deployment: Docker

Setup instructions can be found in the root directory's README

## Unit testing
As suggested by the django project documentation our team will perform unit tests through the unittest module which is built-in to Python.

## Testing the entire solution
Attempt to built the project using Docker
Start the unit tests. 
Actual manual testing.


## Version Control Procedures
The team will use GitHub to track changes to the system from start to finish. Team members must submit pull requests which must be approved by another team member. 

## Stack
- Web Framework: Django
- Frontend Library: Bootstrap
- Database: Postgres
- Continuous integration and deployment: Docker

Setup instructions can be found in the root directory's README

## Unit testing
As suggested by the django project documentation our team will perform unit tests through the unittest module which is built-in to Python.

## Testing the entire solution
Attempt to build the project using Docker
Start the unit tests. 
Actual manual testing.

## Other notes