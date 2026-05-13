# School Management API

A robust, scalable RESTful API designed to manage school operations, including pupils, teachers, and lessons. Built with modern backend technologies, this project demonstrates a stateless architecture using MongoDB and is fully containerized with Docker for seamless deployment.

## 🚀 Features

* **Full CRUD Operations:** Create, Read, Update, and Delete records for Pupils, Teachers, and Lessons.
* **Referential Integrity:** Automated database updates (e.g., deleting a pupil automatically removes their ID from all associated lessons).
* **Data Validation:** Strict schema validation and type checking using Pydantic.
* **Stateless Architecture:** Replaced legacy file-based storage with MongoDB, allowing for scalable, concurrent requests.
* **Containerized:** Fully packaged with Docker and Docker Compose for a "works everywhere" deployment.
* **Interactive Documentation:** Auto-generated Swagger UI for easy API testing and exploration.

## 🛠️ Tech Stack

* **Language:** Python 3.10
* **Framework:** FastAPI
* **Database:** MongoDB
* **Data Validation:** Pydantic
* **Server:** Uvicorn
* **DevOps/Deployment:** Docker & Docker Compose

## 📁 Project Structure

```text
.
├── models/             # OOP classes (Pupil, Teacher, Lesson)
├── managers/           # Business logic and database interactions
├── api.py              # FastAPI application and endpoint routing
├── database.py         # MongoDB connection setup
├── schemas.py          # Pydantic models for request/response validation
├── docker-compose.yml  # Multi-container orchestration
├── Dockerfile          # Image blueprint for the FastAPI app
└── requirements.txt    # Python dependencies
```

## ⚙️ Getting Started

### Prerequisites
You only need to have **[Docker Desktop](https://www.docker.com/products/docker-desktop)** installed on your machine. No local Python or MongoDB installation is required.

### Installation & Running

1. **Clone the repository:**
```bash
git clone [https://github.com/no271l/school-management-system.git](https://github.com/no271l/school-management-system.git)
cd school-management-system
```

2. **Start the application using Docker Compose:**
```bash
docker compose up --build
```
*This command will pull the required images, install dependencies, and start both the FastAPI server and the MongoDB database simultaneously.*

3. **Access the API:**
* **Swagger UI (Interactive Docs):** Open your browser and navigate to `http://localhost:8000/docs` to test the endpoints directly.
* **Alternative API Docs (ReDoc):** `http://localhost:8000/redoc`

4. **Database Access (Optional):**
* You can connect to the running database using **MongoDB Compass** by connecting to `mongodb://localhost:27017/`.

### Stopping the Application
To stop the containers, press `Ctrl + C` in the terminal where Docker is running, or run:
```bash
docker compose down
```

## 🔗 API Endpoints Overview

* **Pupils:** `GET /pupils`, `POST /pupils`, `PUT /pupils/{id}`, `DELETE /pupils/{id}`
* **Teachers:** `GET /teachers`, `POST /teachers`, `PUT /teachers/{id}`, `DELETE /teachers/{id}`
* **Lessons:** `GET /lessons`, `POST /lessons`, `PUT /lessons/{id}`, `DELETE /lessons/{id}`
