# Login-System

**Overview**
This repository contains a full-stack web application designed for user authentication processes, including account creation, login, and deletion functionalities. The application operates by interacting with a JSON-based database to store and manage user credentials securely.

**Features**
User Login: Users can log in with their username and password. Successful authentication displays a success message.
Account Creation: New users can create an account by providing a username and password, with additional validation to ensure the password meets specific criteria (handled by specialPassword.py).
Account Deletion: Users can delete their accounts by re-entering their credentials for confirmation.
Technical Details
The application uses a local JSON file (data.json) as a simple database to store user accounts, including usernames and passwords.
Password validation is performed through specialPassword.py, ensuring that passwords adhere to defined security standards before account creation.
The application maintains a temporary in-memory database (tempDatabase) to optimize the authentication process without repeatedly reading the JSON file.
How It Works
Initialization: Upon starting the application, it loads existing account details from data.json into an in-memory database for quick access.
User Interaction: The application prompts the user to choose between logging in, creating an account, or deleting an account.
For login, it checks the entered credentials against the in-memory database.
For account creation, it guides the user through setting up a username and a validated password before updating the JSON database.
For account deletion, it verifies the user's credentials before removing the account from the database.
Session Management: After each operation, the user is returned to the main menu, allowing for multiple actions within the same session. The session can be exited at any time.
Running the Application
To run the application, ensure you have Python installed on your system. Navigate to the directory containing the application files and execute the following command in your terminal:

Copy code
python loginSystem.py
Dependencies
Python 3.x
JSON for data storage
specialPassword.py for password validation (ensure this script is in the same directory as loginSystem.py).
Security Notice
This application is a demonstration of basic authentication functionality using Python and should not be used as is in production environments. It lacks encryption for stored passwords, making it unsuitable for real-world applications without further security enhancements.
