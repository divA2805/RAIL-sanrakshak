import express from 'express';
import multer from 'multer'; // For handling file uploads
import path from 'path';
import { fileURLToPath } from 'url';
import fetch from 'node-fetch'; // To communicate with Flask API

const app = express();
const PORT = 3000;

// Resolve the current directory using import.meta.url
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Multer configuration for file upload
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, path.join(__dirname, 'uploads')); // Store uploaded files in the 'uploads' folder
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname)); // Rename file with timestamp
  }
});

const upload = multer({ storage });

// Serve the frontend files (index.html, etc.)
app.use(express.static('../client'));

// Route to handle image upload and classification
app.post('/classify', upload.single('file'), async (req, res) => {
  const filePath = path.join(__dirname, 'uploads', req.file.filename);

  try {
    // Send the uploaded file path to Flask API for classification
    const response = await fetch('http://localhost:5000/classify', {
      method: 'POST',
      body: JSON.stringify({ filePath }),
      headers: { 'Content-Type': 'application/json' }
    });

    const result = await response.json();
    res.json(result); // Send classification result back to the frontend
  } catch (err) {
    console.error('Error classifying file:', err);
    res.status(500).json({ error: 'Error classifying file' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
