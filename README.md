# RAIL

## Overview

RAIL is a web application designed to classify the cleanliness of washrooms using machine learning. The project consists of a backend built with Flask and Express, and a frontend built with HTML, CSS, and JavaScript.

## Project Structure


## Backend

### Flask API

The Flask API is responsible for handling image classification requests. It loads a pre-trained TensorFlow model to classify images of washrooms.

- **File:** [`BACKEND/flask-api/classify.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FRAIL%2FBACKEND%2Fflask-api%2Fclassify.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%225ae1f63c-1bd1-4cd3-b845-271885ff1015%22%5D "/workspaces/RAIL/BACKEND/flask-api/classify.py")

#### Endpoints

- **POST /classify**
  - Receives an image file path, preprocesses the image, and returns the classification result (clean or dirty).

### Express Server

The Express server handles file uploads from the frontend and communicates with the Flask API to get classification results.

- **File:** [`BACKEND/server/app.js`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FRAIL%2FBACKEND%2Fserver%2Fapp.js%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%225ae1f63c-1bd1-4cd3-b845-271885ff1015%22%5D "/workspaces/RAIL/BACKEND/server/app.js")
- **File:** [`BACKEND/server/package.json`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FRAIL%2FBACKEND%2Fserver%2Fpackage.json%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%225ae1f63c-1bd1-4cd3-b845-271885ff1015%22%5D "/workspaces/RAIL/BACKEND/server/package.json")

#### Endpoints

- **POST /classify**
  - Handles image uploads and sends the file path to the Flask API for classification.

## Frontend

The frontend consists of a simple HTML page with CSS for styling and JavaScript for interactivity.

- **File:** [`FRONTEND/client/index.html`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FRAIL%2FFRONTEND%2Fclient%2Findex.html%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%225ae1f63c-1bd1-4cd3-b845-271885ff1015%22%5D "/workspaces/RAIL/FRONTEND/client/index.html")
- **File:** [`FRONTEND/client/script.js`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FRAIL%2FFRONTEND%2Fclient%2Fscript.js%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%225ae1f63c-1bd1-4cd3-b845-271885ff1015%22%5D "/workspaces/RAIL/FRONTEND/client/script.js")
- **File:** [`FRONTEND/client/style.css`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FRAIL%2FFRONTEND%2Fclient%2Fstyle.css%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%225ae1f63c-1bd1-4cd3-b845-271885ff1015%22%5D "/workspaces/RAIL/FRONTEND/client/style.css")

### Features

- **Slideshow Functionality**
  - JavaScript functions to handle image slideshows.

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
   ```sh
   pip freeze > requirements.txt
   ```

3. **Install the Model from Kaggle as tar.gz:**
   
   Download Model File from the link below
   ```
   https://www.kaggle.com/models/dhruvshgal/washroom_classifier#
   ````

4. **Place it in the folder:**
Place the Model file in the folder path given below
    ```sh
        /BACKEND/flask-api
    ```