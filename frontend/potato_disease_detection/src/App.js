import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);

    const handleFileChange = (event) => {
        setSelectedFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        if (!selectedFile) {
            alert('Please select a file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await axios.post('http://localhost:8000/predict', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setPrediction(response.data);
            setError(null);
        } catch (err) {
            setError('An error occurred while uploading the image.');
            setPrediction(null);
        }
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Potato Disease Detection</h1>
                <p className="subtitle">Upload an image to detect potato diseases</p>

                <input
                    type="file"
                    accept="image/*"
                    onChange={handleFileChange}
                    className="file-input"
                />
                <button onClick={handleUpload} className="upload-button">Upload</button>

                {prediction && (
                    <div className="prediction-results">
                        <h2>Prediction</h2>
                        <p><strong>Disease:</strong> {prediction.class}</p>
                        <p><strong>Confidence:</strong> {prediction.confidence.toFixed(2) * 100}%</p>
                    </div>
                )}

                {error && <p className="error-message">{error}</p>}
            </header>
        </div>
    );
}

export default App;
