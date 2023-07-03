# Mark_app using flask_docker 
This project demonstrates the creation and deployment of a Flask application using Docker. The project showcases how to containerize a Flask application for easy deployment and scalability.

## Prerequisites
Before getting started, ensure that you have the following prerequisites installed on your machine:

Docker: Install Docker

## Getting Started
Follow these steps to create and deploy your Flask application using Docker:

* Clone the Repository
Clone this repository to your local machine by running the following command:


git clone repository-url

Replace repository-url with the URL of your Git repository.

## Set Up Flask Application
Navigate to the project directory:

cd project-directory

Replace project-directory
with the name of the directory where you cloned the repository.

Inside the project directory, set up your Flask application according to your project requirements. You can modify the existing Flask app or create a new one. Update the necessary dependencies in the requirements.txt file.

* Build the Docker Image
Build the Docker image for your Flask application using the provided Dockerfile:


docker build -t myflaskapp:latest

This command builds the Docker image using the Dockerfile in the current directory and assigns it the tag myflaskapp:latest.

## Run the Docker Container
Start a Docker container from the image you built:

docker run -d -p 5000:5000 myflaskapp:latest

This command runs the Docker container in detached mode (-d) and maps port 5000 from the container to port 5000 on your local machine.

* Access the Flask Application
Open your web browser and go to http://localhost:5000 to access your Flask application running inside the Docker container.

* Customization and Development
Feel free to customize the Flask application according to your project's requirements. You can modify the code and configurations in the project directory. To reflect the changes, rebuild the Docker image using the docker build command mentioned earlier.

During development, you can leverage Docker volumes to mount your local application directory inside the container, allowing you to make code changes without rebuilding the image each time.

## Conclusion
Congratulations! You have successfully created and deployed a Flask application using Docker. Containerizing your application with Docker provides flexibility, portability, and scalability, making it easier to manage and deploy your Flask projects.
