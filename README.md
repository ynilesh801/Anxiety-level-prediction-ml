# Anxiety Level Prediction using Machine Learning

This project focuses on predicting anxiety levels using lifestyle, health, and behavioral data.  
The goal is to build an end-to-end machine learning pipeline and deploy it as an interactive web application using Streamlit.

The project emphasizes practical aspects such as data preprocessing, model comparison, and deployment rather than only model accuracy.

---

## Project Overview

Instead of predicting an exact anxiety score, the problem was simplified by converting anxiety levels into broader categories.  
This helped improve model stability and made the predictions more reliable and easier to interpret.

The project follows a complete machine learning workflow:
- Data exploration and preprocessing
- Model training and evaluation
- Model selection
- Deployment using Streamlit

---

## Dataset

The dataset contains information related to:
- Lifestyle habits (sleep, physical activity, caffeine, alcohol)
- Health indicators (heart rate, breathing rate, sweating level)
- Behavioral and background factors (stress level, smoking, family history, major life events)

The dataset is included in the repository for transparency and reproducibility.

---

## Exploratory Data Analysis and Preprocessing

The following steps were performed:
- Initial data inspection
- Checking for missing and duplicate values
- Exploratory analysis of numerical features
- Skewness and outlier analysis
- Encoding of categorical variables
- Feature scaling using StandardScaler

Categorical features were encoded using `OrdinalEncoder`, and numerical features were standardized to ensure consistent model performance.

---

## Modeling Approach

Two approaches were explored:
- **Multi-class classification** (predicting exact anxiety levels)
- **Binary classification** (Low vs High anxiety)

Binary classification performed significantly better and provided more stable results.

The following models were trained and evaluated:
- Decision Tree (Raw and Pruned)
- Logistic Regression
- Random Forest (Default and Tuned)

---

## Model Selection

Logistic Regression was selected as the final model due to:
- Stable and consistent performance
- Better interpretability
- Lower risk of overfitting
- Faster training and inference

---

## Deployment

The final model was deployed using **Streamlit Community Cloud**.  
The deployed application allows users to enter lifestyle and health-related inputs and receive a prediction indicating **Low** or **High Anxiety**.

🔗 **Live App:**  
https://anxiety-level-prediction-ml.streamlit.app/

---

## Repository Structure
anxiety-level-prediction/
│
├── app.py
├── model.pkl
├── encoder.pkl
├── scaler.pkl
├── feature_columns.pkl
├── requirements.txt
├── data/
│ └── enhanced_anxiety_dataset.csv
├── notebooks/
│ └── model_training.ipynb
├── README.md
└── LICENSE

---

## Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- GitHub & Streamlit Community Cloud

---

## Disclaimer

This project is created for **educational and demonstration purposes only**.  
It is not intended to provide medical advice or clinical diagnosis.

---

## Author

**Nilesh Yadav**

---

## License

This project is licensed under the **MIT License**.

