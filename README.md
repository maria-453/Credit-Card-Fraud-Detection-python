# Credit Card Fraud Detection

This project demonstrates a credit card fraud detection system using machine learning. The system is built using Python, Flask, and Scikit-learn, and can be deployed as a web application.

---

## Motivation

Credit card fraud is a significant problem faced by financial institutions and users globally. By leveraging machine learning, this project helps in early detection and prevention of fraudulent transactions, ensuring better financial security for users.

---

## Description

This project aims to detect fraudulent credit card transactions using machine learning techniques. The system is designed to identify potentially fraudulent activities by analyzing transaction data and flagging anomalies. The project includes a machine learning model, a Flask-based web application for deployment, and a preprocessed dataset for training and testing.

---

## Features

- **Jupyter Notebook** for data preprocessing, model training, and evaluation.
- **Flask-based Web Application** for real-time fraud detection.
- **Integrated Dataset** for training, testing, and validating the model.
- **Pre-trained Model** for easy deployment and demonstration.
- **Visualization Tools** to understand the dataset and model performance.

---

## Technologies Used

- **Python**: Programming language for machine learning and web application.
- **Flask**: Framework for building the web application.
- **Pandas & NumPy**: For data manipulation and analysis.
- **Scikit-learn**: For building and evaluating the machine learning model.
- **Matplotlib**: For data visualization.

---

## Dataset

The project uses the [Credit Card Fraud Detection dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud), which contains real-world transactions made using credit cards in September 2013 by European cardholders. The dataset has 284,807 transactions, including 492 fraudulent ones, making it highly imbalanced.

---

## How It Works

1. Data is preprocessed to remove noise and handle imbalanced classes.
2. A machine learning model (Random Forest Classifier) is trained on the dataset.
3. The trained model is serialized (`model.pkl`) for deployment.
4. A Flask API accepts transaction data and predicts whether it is fraudulent or not.

---

## Project Structure

```
credit-card-fraud-detection/
│
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── app.py                   # Flask application for deployment
├── fraud_detection.ipynb    # Jupyter Notebook for model training
├── model.pkl                # Pre-trained ML model
└── data/
    └── creditcard.csv       # Dataset for training and testing
```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/maria-453/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the web application:
   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000` in your browser to interact with the API.

---

