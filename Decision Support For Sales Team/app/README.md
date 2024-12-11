
# Flask PostgreSQL Docker CRUD API

This project is a simple RESTful API built using Flask, PostgreSQL, and Docker. It demonstrates basic CRUD (Create, Read, Update, Delete) operations for managing user data stored in a PostgreSQL database. The API is containerized using Docker for easy deployment.

---

## Features

- **Create a User**: Add a new user with a unique username and email.
- **Read Users**: Retrieve all users or a specific user by ID.
- **Update a User**: Modify the username and email of an existing user.
- **Delete a User**: Remove a user from the database.
- **Dockerized**: The entire application is containerized for seamless deployment.
- **Database Integration**: Uses PostgreSQL as the database backend.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Containerization**: Docker and Docker Compose
- **ORM**: SQLAlchemy

---


## Getting Started

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-directory>
```

### **2. Environment Setup**
Ensure the following environment variable is set in `docker-compose.yml`:
```yaml
DB_URL=postgresql://postgres:postgres@flask_db:5432/postgres
```

---

### **3. Build and Run the Application**

Build and run the containers using Docker Compose:

```bash
docker-compose up --build
```

This will:
- Start a PostgreSQL database container.
- Start the Flask application container on port `4000`.

---

## Endpoints

### **Base URL**: `http://localhost:4000`

### **1. Test Route**
- **URL**: `/test`
- **Method**: `GET`
- **Description**: Returns a test message to verify the API is running.
- **Response**:
```json
{
  "message": "test route"
}
```

---

### **2. Create a User**
- **URL**: `/users`
- **Method**: `POST`
- **Description**: Add a new user.
- **Request Body**:
```json
{
  "username": "exampleUser",
  "email": "example@example.com"
}
```
- **Response**:
```json
{
  "message": "user created"
}
```

---

### **3. Get All Users**
- **URL**: `/users`
- **Method**: `GET`
- **Description**: Retrieve all users.
- **Response**:
```json
[
  {
    "id": 1,
    "username": "exampleUser",
    "email": "example@example.com"
  }
]
```

---

### **4. Get User by ID**
- **URL**: `/users/<int:id>`
- **Method**: `GET`
- **Description**: Retrieve a specific user by their ID.
- **Response**:
```json
{
  "user": {
    "id": 1,
    "username": "exampleUser",
    "email": "example@example.com"
  }
}
```

---

### **5. Update a User**
- **URL**: `/users/<int:id>`
- **Method**: `PUT`
- **Description**: Update an existing user's information.
- **Request Body**:
```json
{
  "username": "updatedUser",
  "email": "updated@example.com"
}
```
- **Response**:
```json
{
  "message": "user updated"
}
```

---

### **6. Delete a User**
- **URL**: `/users/<int:id>`
- **Method**: `DELETE`
- **Description**: Delete a user by ID.
- **Response**:
```json
{
  "message": "user deleted"
}
```

---


## Running Locally (Without Docker)

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up the PostgreSQL database and update the `DB_URL` environment variable.

3. Run the Flask application:
   ```bash
   flask run --host=0.0.0.0 --port=4000
   ```

---

## Common Issues

- **Database Connection Error**: Ensure the `DB_URL` in `docker-compose.yml` is correct and matches the database service configuration.
- **Port Conflict**: If port `4000` or `5432` is in use, modify the `docker-compose.yml` file to use a different port.

---

