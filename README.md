


# RAIL-संरक्षक






https://github.com/user-attachments/assets/7e7b3863-465c-4106-9a7f-d8c3a43fef9a




## Overview

AI-powered enhancement of Rail Madad for automated complaint categorization, prioritization, data extraction, and smart routing using visual content, improving resolution speed, accuracy , and user experience.

## Project Structure

This project integrates a **Backend** using Flask and Express servers with a **Frontend** HTML file that includes internal CSS for styling and JavaScript for functionality. The system allows users to upload complaint-related images, videos, and audio files for classification and provides real-time feedback.

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
