# CredSecure Credit Card Fraud Detection Application using Random Forest

This project implements a **fraud detection application** using a **Random Forest** model, built with **Flask** and **Python** to predict fraudulent credit card transactions. The model outperforms others like **XGBoost** and **Decision Trees** in accuracy, recall, and ROC-AUC, making it ideal for handling imbalanced datasets in real-time fraud detection.

## Model Comparison:
- **Random Forest**: Best overall performance with high accuracy, recall, and ROC-AUC, making it ideal for fraud detection in imbalanced datasets.
- **XGBoost**: Performs well in accuracy but suffers from overfitting and slight recall drop, leading to missed fraud cases.
- **Decision Tree**: Easy to interpret but prone to overfitting, with poor generalization.
- **Logistic Regression**: Simple and interpretable, but fails to capture complex patterns, resulting in lower accuracy and recall.

## Key Features:
- Real-time fraud detection using a trained Random Forest model
- Simple, user-friendly interface built with Flask
- High accuracy, precision, and recall for accurate predictions
- Scalable and easy to deploy in production environments

## Technologies Used:
- Python
- Flask
- Random Forest (for fraud detection)

## Setup & Installation:
1. Clone the repository:
``` bash
git clone https://github.com/KrishnenduMR/CredSecure.git
cd CredSecure
```
2. install dependencies
``` bash
pip install -r requirements.txt
```
3. Run the app
``` bash
python app.py
```
Now the app should be running locally on `http://127.0.0.1:5000/`.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
