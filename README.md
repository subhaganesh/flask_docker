
![images](https://github.com/subhaganesh/mark_app-using-flask_docker/assets/96689756/54292f9d-9e54-402c-872d-6b2cb79dd577)



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


docker build -t mark-app:latest

This command builds the Docker image using the Dockerfile in the current directory and assigns it the tag mark-app:latest.

## Run the Docker Container
Start a Docker container from the image you built:

docker run -d -p 5000:5000 mark-app:latest

This command runs the Docker container in detached mode (-d) and maps port 5000 from the container to port 5000 on your local machine.

* Access the Flask Application
Open your web browser and go to http://localhost:5000 to access your Flask application running inside the Docker container.

* Customization and Development
Feel free to customize the Flask application according to your project's requirements. You can modify the code and configurations in the project directory. To reflect the changes, rebuild the Docker image using the docker build command mentioned earlier.

During development, you can leverage Docker volumes to mount your local application directory inside the container, allowing you to make code changes without rebuilding the image each time.

## Conclusion
Congratulations! You have successfully created and deployed a Flask application using Docker. Containerizing your application with Docker provides flexibility, portability, and scalability, making it easier to manage and deploy your Flask projects.

## Downloading the Container Image
To download the container image for this project, follow these steps:

Open a terminal or command prompt on your local machine.

Run the following command to pull the container image from Docker Hub:

## docker pull subhaganesh/mark-app:latest
 use the above command for download the docker app

Wait for the download to complete. Docker will retrieve the image from the Docker Hub repository.

Once the image is downloaded, you can use it to run the container locally on your machine.
