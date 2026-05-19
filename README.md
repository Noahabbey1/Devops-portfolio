# Flask API — Containerized Microservice

A production-style Python Flask REST API containerized with Docker 
and pushed to Docker Hub.

## What this demonstrates
- Writing a production Dockerfile (slim base image, .dockerignore, pinned deps)
- Building and tagging images with semantic versioning
- Running and testing a containerized service locally
- Pushing versioned images to Docker Hub


## Deep dive 

for the docker file, we have utilised two COPY commands - one for the dependencies and
the other for the aplication. This separation allows Docker to use its build cache to make 
your container builds significantly faster. the docker file is processed sequesntially,
hence it checks if the files in the copy command have changed,so lets say an update was made to 
 the app.py, it retiains the cache for the dependency and only update the application file  

## Project structure

docker/   Dockerfile, app.py, requirements.txt
screenshots/  Evidence of the running container

## How to run it

docker pull abbeysne/flask_api:v1
docker run -d -p 5000:5000 --name flask_api abbeysne/flask_api:v1

curl http://localhost:5000/health

## Docker Hub
https://hub.docker.com/r/abbeysne/flask_api

## Screenshot

