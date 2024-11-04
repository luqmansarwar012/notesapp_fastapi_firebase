
# Notes App with FastAPI and Firebase

This is a RESTful Notes application built using FastAPI, Firebase Realtime Database, and Firebase Authentication. It provides secure user management, along with CRUD operations for managing notes.

## Features

- **User Authentication**: Uses Firebase Authentication for user signup and login.
- **CRUD Operations**: Create, read, update, and delete notes associated with each authenticated user.
- **Firebase Integration**: Utilizes Firebase Realtime Database to store notes.
- **Secure Routes**: Middleware checks for valid access tokens on protected routes.

## Prerequisites

- **Python 3.10+**
- **Firebase Project**: Set up Firebase with Authentication and Realtime Database.
- **Service Account Key**: Download your Firebase service account key as `service_account_key.json`.


## Setup

1. Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd your-repo-name
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up Firebase:

   - Add your Firebase Realtime Database URL and credentials in `firebase/constants.py`.
   - Place `service_account_key.json` in the root directory.

4. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

## Usage

### Authentication

- **Login**: `POST /auth/login` to receive an access token.

### User

- **Signup**: `POST /auth/signup` with `email` and `password`.

### Notes Endpoints

- **Create Note**: `POST /notes/{access_token}` - Create a note for the authenticated user.
- **Update Note**: `PUT /notes/{note_key}/{access_token}` - Update a specific note.
- **Delete Note**: `DELETE /notes/{note_key}/{access_token}` - Delete a specific note.
- **Get All Notes**: `GET /notes/{access_token}` - Retrieve all notes for the authenticated user.

### Middleware

This app uses a custom middleware to verify user authentication on protected routes. Only routes within the `note` module are secured using the access token passed as a URL parameter.


---