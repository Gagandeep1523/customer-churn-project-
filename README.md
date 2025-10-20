# customer-churn-project-
Slide 1: Title Slide

Title: Customer Churn Prediction Dashboard
Subtitle: Using Machine Learning and SQL for Data Cleaning
Author: Gagandeep singh
Date: October 2025

⸻

Slide 2: Project Overview
	•	Objective: Predict which customers are likely to churn
	•	Goal: Help businesses retain high-risk customers
	•	Tools used: Python, SQL, Streamlit, scikit-learn

⸻

Slide 3: Data Collection
	•	Dataset source: [Specify source if any, e.g., telecom company sample data]
	•	Total records: 1,409
	•	Key features: Tenure, Monthly Charges, Contract Type, Senior Citizen, Paperless Billing

⸻

Slide 4: Data Cleaning & Preprocessing
	•	SQL used for cleaning and preparing data
	•	Missing value handling
	•	Feature encoding (One-hot encoding for categorical features)
	•	Data split: 80% training, 20% testing

⸻

Slide 5: Feature Engineering
	•	Created tenure groups
	•	Converted categorical variables into numerical columns
	•	Ensured features match model requirements

⸻

6: Models Used
	1.	Random Forest Classifier – initial experimentation
	2.	Logistic Regression (LR) – final model selected for the dashboard

	•	LR chosen for better generalization on test data
	•	Simpler, easier to interpret, less prone to overfitting than Random Forest
⸻

Slide 7: Model Evaluation Metrics
	•	Accuracy, Precision, Recall, F1-Score
	•	Confusion matrix insights
	•	Evaluated on training and test data

⸻

Slide 8: Random Forest Results

Training Accuracy: 0.9934
Test Accuracy: 0.7637

Classification Report (Test Data):
	•	Class 0: Precision 0.82, Recall 0.87, F1-score 0.84
	•	Class 1: Precision 0.56, Recall 0.47, F1-score 0.51
	•	Accuracy: 0.76

⸻

Slide 9: Logistic Regression Results

Training Accuracy: 0.7868
Test Accuracy: 0.8048

Classification Report (Test Data):
	•	Class 0: Precision 0.84, Recall 0.90, F1-score 0.87
	•	Class 1: Precision 0.67, Recall 0.53, F1-score 0.59
	•	Accuracy: 0.80

⸻

Slide 10: Model Comparison
Model               Train Accuracy  Test Accuracy
Random Forest         0.9934           0.7637
Logistic Regression    0.7868          0.8048

______

Slide 11: Streamlit Dashboard
	•	Uses Logistic Regression (LR) model for predictions
	•	Inputs: Customer info (tenure, monthly charges, contract type, etc.)
	•	Outputs: Churn probability, stay/churn prediction
	•	Visualizations:
	•	Feature importance (based on LR coefficients)
	•	Churn by segment
	•	Top customers likely to churn with download option

⸻

Slide 12: Conclusion
	•	Logistic Regression (LR) was selected as the final model for its test accuracy and interpretability
	•	SQL + Python used for data cleaning and feature engineering
	•	Dashboard provides interactive, actionable insights for customer retention
