# Flask API — Containerized Microservice

A production-style Python Flask REST API containerized with Docker 
and pushed to Docker Hub.

## What this demonstrates
- Writing a production Dockerfile (slim base image, .dockerignore, pinned deps)
- Building and tagging images with semantic versioning
- Running and testing a containerized service locally
- Pushing versioned images to Docker Hub


## Deep dive 

### Layer Caching with Dual COPY Commands
We split the file transfer into two distinct steps to leverage Docker's sequential build cache:
COPY requirements.txt .: Copies only the dependency definitions. Because this file changes infrequently, Docker installs the Python packages (RUN pip install) once and caches the heavy layer.
COPY . /app: Copies the rest of the application source code into the target /app directory.The Performance Win: When you modify code files (like app.py), Docker invalidates the cache only from the COPY . /app step onward. It completely skips reinstalling dependencies, reducing subsequent image build times from minutes to seconds. 

### Deterministic Environment via Version Pinning
To make this caching strategy safe and reliable, all dependencies are strictly locked in requirements.txt (e.g., Flask == 3.0.2):Consistency: Guarantees that when the cache eventually updates (e.g., when adding a new package), Docker installs the exact same version stack across all developer machines and production servers.Stability: Prevents pip from automatically downloading breaking, unvalidated major updates during a clean build.
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

### Docker Image Creation 
<img width="2698" height="1388" alt="Image 19-05-2026 at 15 02" src="https://github.com/user-attachments/assets/680094d7-632a-4630-ae0d-45c604bd87f5" />

### Container details
<img width="2460" height="212" alt="Image 19-05-2026 at 15 12" src="https://github.com/user-attachments/assets/bb8ee7ba-19c9-4ab4-85b4-22961cd76b1c" />

### Container health status
<img width="898" height="562" alt="health" src="https://github.com/user-attachments/assets/5128298e-8135-445e-9a6f-42a8c7c4935a" />


