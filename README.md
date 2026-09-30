# Insurance Premium Prediction API

A FastAPI-based machine learning application that predicts an insurance premium category from user information.

The project focuses on learning and applying **FastAPI backend development**, including request validation, response schemas, computed fields, batch prediction, model inference, health checks, Docker containerization, Docker Compose, and Streamlit frontend integration.

## 🚀 Features

* FastAPI REST API
* Pydantic request validation
* Automatic BMI calculation
* Automatic age-group classification
* Lifestyle-risk classification
* City-tier classification
* Machine learning model inference
* Prediction confidence score
* Class probability distribution
* Detailed prediction response
* Batch prediction API
* Health-check endpoint
* Automatic Swagger/OpenAPI documentation
* Streamlit frontend
* CSV-based batch prediction through frontend
* Dockerized FastAPI backend
* Dockerized Streamlit frontend
* Docker Compose for multi-container setup
* Docker Hub images

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn
* Pandas
* NumPy
* Scikit-learn

### Frontend

* Streamlit
* Requests
* Pandas

### DevOps / Deployment

* Docker
* Docker Compose
* Docker Hub
* AWS *(planned)*

## 📁 Project Structure

```text
insurance-premium-prediction-api/
│
├── app.py
├── frontend.py
│
├── Dockerfile.api
├── Dockerfile.frontend
├── docker-compose.yml
├── .dockerignore
│
├── requirements.txt
├── requirements.frontend.txt
│
├── config/
│   └── city_tier.py
│
├── models/
│   ├── model.pkl
│   └── predict.py
│
└── schema/
    ├── user_input.py
    └── prediction_response.py
```

## 🔄 Application Architecture

```text
                         Browser
                       /         \
                      ↓           ↓
              Streamlit :8501   FastAPI :8000
                      │             │
                      │    HTTP     │
                      └─────────────┘
                                    ↓
                              ML Model
                              model.pkl
```

The Streamlit frontend communicates with the FastAPI backend through HTTP requests.

When running with Docker Compose, the frontend communicates with the API using:

```text
http://api:8000
```

## 🔄 API Workflow

### Single Prediction

```text
Client
   │
   ▼
POST /predict
   │
   ▼
Pydantic Validation
   │
   ▼
Feature Engineering
   ├── BMI
   ├── Age Group
   ├── Lifestyle Risk
   └── City Tier
   │
   ▼
ML Model
   │
   ▼
Prediction
   ├── Predicted Category
   ├── Confidence
   ├── Risk Profile
   └── Class Probabilities
   │
   ▼
JSON Response
```

### Batch Prediction

```text
Client
   │
   ▼
POST /predict/batch
   │
   ▼
Validate Multiple Users
   │
   ▼
Run Predictions
   │
   ▼
Return Results
   ├── Total Predictions
   └── Individual Results
```

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/aryak9/insurance-premium-prediction-api.git

cd insurance-premium-prediction-api
```

### 2. Create a virtual environment

macOS/Linux:

```bash
python3 -m venv myenv

source myenv/bin/activate
```

### 3. Install backend dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 5. Start the Streamlit frontend

Open another terminal, activate the virtual environment, and install frontend dependencies:

```bash
pip install -r requirements.frontend.txt
```

Then run:

```bash
streamlit run frontend.py
```

The frontend will be available at:

```text
http://localhost:8501
```

By default, the frontend communicates with:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## 🔗 API Endpoints

| Method | Endpoint         | Description                                              |
| ------ | ---------------- | -------------------------------------------------------- |
| GET    | `/`              | Returns API welcome message                              |
| GET    | `/health`        | Checks API and model status                              |
| POST   | `/predict`       | Predicts insurance premium category for one user         |
| POST   | `/predict/batch` | Predicts insurance premium categories for multiple users |

## 🧪 Single Prediction

### Request

```json
{
  "age": 30,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 8.5,
  "smoker": false,
  "city": "Delhi",
  "occupation": "private_job"
}
```

The API automatically derives:

* BMI
* Age group
* Lifestyle risk
* City tier

### Response

```json
{
  "predicted_category": "Low",
  "confidence": 0.66,
  "risk_profile": {
    "bmi": 22.86,
    "age_group": "adult",
    "lifestyle_risk": "low",
    "city_tier": 1
  },
  "class_probabilities": {
    "High": 0.0,
    "Low": 0.66,
    "Medium": 0.34
  },
  "model": {
    "name": "Insurance Premium Prediction Model",
    "version": "1.0.0"
  }
}
```

The exact prediction and probabilities depend on the trained model and input data.

## 📦 Batch Prediction

The API also supports predicting multiple users in a single request.

### Endpoint

```text
POST /predict/batch
```

### Request

```json
{
  "users": [
    {
      "age": 30,
      "weight": 70,
      "height": 1.75,
      "income_lpa": 8.5,
      "smoker": false,
      "city": "Delhi",
      "occupation": "private_job"
    },
    {
      "age": 52,
      "weight": 82,
      "height": 1.75,
      "income_lpa": 12.0,
      "smoker": true,
      "city": "Mumbai",
      "occupation": "business_owner"
    }
  ]
}
```

The response contains the total number of predictions and the individual prediction results.

## 🖥️ Streamlit Frontend

The project includes a Streamlit frontend for interacting with the FastAPI backend.

### Single Prediction

The frontend allows users to:

* Enter user information
* Submit a prediction request
* View predicted category
* View model confidence
* View risk profile
* View class probabilities
* View model information

### Batch Prediction

The frontend also supports CSV-based batch prediction.

Users can:

1. Download the CSV template
2. Add multiple user records
3. Upload the CSV
4. Send the records to `/predict/batch`
5. View prediction results
6. Download the prediction results as CSV

## 🐳 Docker

The project uses separate Docker images for the FastAPI backend and Streamlit frontend.

### Build with Docker Compose

```bash
docker compose build
```

### Start the application

```bash
docker compose up
```

The services will be available at:

```text
FastAPI:
http://localhost:8000

Swagger:
http://localhost:8000/docs

Streamlit:
http://localhost:8501
```

### Stop the application

```bash
docker compose down
```

### Docker Architecture

```text
Browser
   │
   ├──────────────► Streamlit Container
   │                    :8501
   │                       │
   │                       │ HTTP
   │                       ▼
   └──────────────► FastAPI Container
                        :8000
                           │
                           ▼
                       model.pkl
```

## 🐳 Docker Hub

The Docker images are available on Docker Hub.

### FastAPI API

```text
aryak9/insurance-premium-prediction-api
```

Available tags:

```text
1.0
latest
```

`1.0` represents the earlier basic API version, while `latest` represents the current upgraded API.

### Streamlit Frontend

```text
aryak9/insurance-premium-prediction-frontend
```

Available tag:

```text
latest
```

### Pull the API image

```bash
docker pull aryak9/insurance-premium-prediction-api:latest
```

### Pull the frontend image

```bash
docker pull aryak9/insurance-premium-prediction-frontend:latest
```

## 🎯 Project Objective

The primary objective of this project is to learn how to build and serve a machine learning-backed REST API using FastAPI.

The project demonstrates practical backend concepts including:

* API development
* Request validation
* Response modeling
* Computed fields
* Batch processing
* ML model integration
* Health checks
* Docker containerization
* Multi-container application setup
* Frontend-to-backend communication

## 🔮 Planned Improvements

Future improvements may include:

* [ ] API versioning
* [ ] Centralized exception handling
* [ ] Structured logging
* [ ] Automated API tests
* [ ] Environment-based configuration
* [ ] CORS configuration
* [ ] GitHub Actions CI/CD
* [ ] AWS deployment
* [ ] Production monitoring

## 👨‍💻 Author

**Arya Kumar**

GitHub: https://github.com/aryak9

---

Built with **FastAPI + Python + Scikit-learn + Streamlit + Docker**.
