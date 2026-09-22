# Insurance Premium Prediction API

A FastAPI-based REST API that predicts an insurance premium category from user information using a trained machine learning model.

The project focuses on learning and applying **FastAPI backend development**, including request validation, response schemas, computed fields, API endpoints, model inference, health checks, and Docker-based deployment.

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
* Health-check endpoint
* Automatic Swagger/OpenAPI documentation
* Docker support

## 🛠️ Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn
* Pandas
* NumPy
* Scikit-learn
* Docker

## 📁 Project Structure

```text
insurance-premium-prediction-api/
│
├── app.py
├── Dockerfile
├── requirements.txt
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

## 🔄 API Workflow

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
   └── Class Probabilities
   │
   ▼
JSON Response
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

### 3. Install dependencies

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

| Method | Endpoint   | Description                         |
| ------ | ---------- | ----------------------------------- |
| GET    | `/`        | Returns API welcome message         |
| GET    | `/health`  | Checks API and model status         |
| POST   | `/predict` | Predicts insurance premium category |

## 🧪 Prediction Request

Example request:

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

## 📤 Prediction Response

Example:

```json
{
  "predicted_category": "Medium",
  "confidence": 0.8432,
  "class_probabilities": {
    "Low": 0.0521,
    "Medium": 0.8432,
    "High": 0.1047
  }
}
```

The exact prediction and probabilities depend on the trained model and input data.

## 🐳 Docker

Build the Docker image:

```bash
docker build -t insurance-premium-api .
```

Run the container:

```bash
docker run -p 8000:8000 insurance-premium-api
```

The API will then be available at:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

## 🎯 Project Objective

The primary objective of this project is to learn how to build and serve a machine learning-backed REST API using FastAPI.

The project also provides a foundation for adding production-oriented backend features such as API versioning, structured logging, testing, authentication, frontend integration, CI/CD, and cloud deployment.

## 🔮 Planned Improvements

The project will be developed further with:

* [ ] Professional FastAPI project structure
* [ ] API versioning
* [ ] Centralized exception handling
* [ ] Structured logging
* [ ] Automated API tests
* [ ] Environment-based configuration
* [ ] CORS configuration
* [ ] Frontend application
* [ ] Improved Docker configuration
* [ ] GitHub Actions CI/CD
* [ ] AWS deployment
* [ ] Production monitoring

## 👨‍💻 Author

**Arya Kumar**

GitHub: https://github.com/aryak9

---

Built with **FastAPI + Python**.
