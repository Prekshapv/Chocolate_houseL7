# Chocolate_houseL7
# Chocolate House Management App

1. Clone the repository.
git clone https://github.com/Prekshapv/Chocolate_houseL7.git
main branch

2. Run `db_setup.py` to set up the database.
python db_setup.py
3. Run `app.py` to start the application.
python app.py


# Docker Setup
1.Clone the repository
git clone https://github.com/Prekshapv/Chocolate_houseL7.git
Ensure you're on the main branch.

2.Navigate to the project directory

3.Build the Docker image: Create a Docker image named chocolate-house-app:
docker build -t <container-name> .

4.Run the Docker container: Start the application by running a container from the chocolate-house-app image:
docker run -it -p 8000:8000 chocolate-house-app


