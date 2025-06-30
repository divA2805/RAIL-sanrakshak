<div align="center">
  <h1>🚆RAIL-संरक्षक</h1>
</div>

<div align="center">
  <h3>Transforming Complaint Management with AI Precision</h3>
</div>


---

## 📊 Project Stats

![last commit](https://img.shields.io/badge/last%20commit-April-blue)
![HTML](https://img.shields.io/badge/html-86.2%25-blue)
![languages](https://img.shields.io/badge/languages-3-blue)

---

## ⚙️ Built with the Tools and Technologies

### 🔧 Backend & Frameworks

![Express](https://img.shields.io/badge/Express-black?logo=express&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-black?logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![npm](https://img.shields.io/badge/npm-CB3837?logo=npm&logoColor=white)
![TOML](https://img.shields.io/badge/TOML-8D6748?logo=toml&logoColor=white)

---

### 🧠 AI/ML Libraries

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-red?logo=keras&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![SymPy](https://img.shields.io/badge/SymPy-414141?logo=sympy&logoColor=white)
![Numba](https://img.shields.io/badge/Numba-00AEEF?logo=numba&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E66EB2?logo=pydantic&logoColor=white)

---

### 📦 Data & UI Representation

![JSON](https://img.shields.io/badge/JSON-black?logo=json&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-black?logo=markdown&logoColor=white)
![Rich](https://img.shields.io/badge/Rich-yellow?logo=python&logoColor=black)
![tqdm](https://img.shields.io/badge/tqdm-yellow?logo=tqdm&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)

---

### 🟨 Web Technologies

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Babel](https://img.shields.io/badge/Babel-F9DC3E?logo=babel&logoColor=black)

---

## 🧠 About the Project

**RAIL-SANRAKSHAK** is a next-generation complaint management system designed for the Indian Railways. It leverages artificial intelligence to streamline complaint classification, response generation, and resolution tracking—ensuring a faster and more transparent experience for passengers and authorities.

---

## 🛤️ Key Features

- AI-powered complaint categorization
- Real-time dashboards using Streamlit
- RESTful API support via Flask/FastAPI
- Multi-model ML backend using TensorFlow, Keras, Scikit-learn
- Intelligent suggestions for resolution using NLP
- Frontend integration with JavaScript for UI-based feedback

---











https://github.com/user-attachments/assets/7e7b3863-465c-4106-9a7f-d8c3a43fef9a



---

## Project Structure

This project integrates a **Backend** using Flask and Express servers with a **Frontend** HTML file that includes internal CSS for styling and JavaScript for functionality. The system allows users to upload complaint-related images, videos, and audio files for classification and provides real-time feedback.

---

## Backend

### Flask API

The Flask API handles image classification requests using a pre-trained TensorFlow model for categorizing complaints based on washroom cleanliness.

- **File:** [`BACKEND/flask-api/classify.py`](BACKEND/flask-api/classify.py)

#### Endpoints

- **POST /classify**  
  Accepts an image file path, preprocesses the image, and returns the classification result (clean or dirty).

### Express Server

The Express server manages file uploads from the frontend and interacts with the Flask API to classify the complaints.

- **File:** [`BACKEND/server/app.js`](BACKEND/server/app.js)  
- **File:** [`BACKEND/server/package.json`](BACKEND/server/package.json)

#### Endpoints

- **POST /classify**  
  Manages image uploads and sends the file path to the Flask API for classification.

---

## Frontend

The frontend is an HTML file with **internal CSS and JavaScript**, making it self-contained.

- **File:** [`FRONTEND/client/index.html`](FRONTEND/client/index.html)

### Key Features

- **Internal CSS:**  
  The HTML file contains CSS styles embedded in the `<style>` tag to handle layout, colors, animations, and responsiveness without relying on external files.
  
- **Internal JavaScript:**  
  JavaScript functions included within the `<script>` tag provide key functionalities such as:
  - **File Upload:** Allows drag-and-drop or click-to-upload functionality for images, videos, and audio files.
  - **AI Analysis Simulation:** Provides real-time feedback with progress bars and displays classification results based on the AI analysis.
  - **Image Preview:** Displays an image preview and classification status after upload.
  - **Smooth Scrolling:** Ensures smooth navigation between sections on the page.

- **Progress Bar:**  
  A simulated progress bar shows the upload status, providing a visual cue to users while the system processes their files.

- **Animations:**  
  Animations (such as the title animation) enhance the user experience and engagement.

---

## Getting Started

### Prerequisites

- Node.js  
- Python  
- TensorFlow  
- Flask

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/dhruv-shgal/RAIL.git
   ```

2. **Install dependencies:**
To install all dependencies run this command
   ```
   pip install -r requirements.txt
   ```

3. **Install the Model from Kaggle as tar.gz:**
   
   Download Model File from the link below
   ```
   https://www.kaggle.com/models/dhruvshgal/washroom_classifier#
   ````

4. **Place it in the folder:**
Place the Model file in the folder path given below
    ```
        /BACKEND/flask-api
    ```

---
