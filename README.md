# AI Powered Potato Leafs Disease Detection Web App 

This project is a **Potato Disease Detection System** developed using **React** for the front-end and **FastAPI** with a **Convolutional Neural Network (CNN)** for disease classification on the back-end. The system allows users to upload images of potato leaves and classifies them into different disease categories with an accuracy score.


## Introduction

Potato disease detection is crucial for agriculture to ensure healthy crop production. In this project, a **React app** serves as the front-end, while the disease classification is handled by a **CNN** model deployed through **FastAPI** for prediction.

The app allows users to upload images of potato leaves, and the CNN model classifies the images, predicting the type of disease along with the confidence score.

## Features

- Upload an image of a potato leaf.
- Classify the leaf into different disease categories.
- Display prediction results with confidence percentages.
- Handle errors with informative messages.
  
## Technologies Used

- **Frontend**: 
  - React.js
  - Axios (for HTTP requests)
  - HTML/CSS

- **Backend**:
  - Python
  - FastAPI (for the backend API)
  - TensorFlow and Keras (for training the CNN model)

- **Libraries**:
  - Axios (for API calls in React)
  - React Hooks (useState, useEffect)
  - FastAPI (for building the backend server)
  - Uvicorn (ASGI server to run FastAPI)

## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Before you start, ensure you have the following installed on your machine:

- **Node.js** (v12 or higher): You can download it from [here](https://nodejs.org/).
- **npm** (comes bundled with Node.js)
- **Python** (for the backend and training the CNN model)
- **Uvicorn** (for running FastAPI)
  
### Installation

1. **Clone the repository**:
   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Shahzad-Ali-44/Potato_disease_detection_full_stack_web_app_using_CNN.git
   ```

2. **Install frontend dependencies**:

   Run the following command in the project root directory to install React dependencies:

   ```bash
   npm install
   ```

3. **Install backend dependencies**:

   Install the required Python dependencies for the backend by running:

   ```bash
   pip install fastapi uvicorn tensorflow
   ```
  

### Run the App

1. **Start the React development server**:

   In the frontend directory, run the following command:

   ```bash
   npm start
   ```

   This will start the React app at `http://localhost:3000/` in your web browser.

2. **Running the Backend (FastAPI)**:

   In the backend directory, run the following command:

   ```bash
   python main.py
   ```
   
   By default, FastAPI runs on port `8000`, so the backend will be available at `http://localhost:8000`.


## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.


## 📜 License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- Dataset contributors for their valuable efforts.
- TensorFlow and Keras for their robust deep learning frameworks.
- Open-source community for tools and libraries enabling this work. 
