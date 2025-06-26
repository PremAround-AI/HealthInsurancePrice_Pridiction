# HealthInsurancePrice_Pridiction

🏥 Health Insurance Price Prediction Using Machine Learning

📌 Overview:

This project aims to predict health insurance charges based on a person's BMI, age, number of children, and smoking status using supervised machine learning models.

Understanding how these features affect insurance premiums can help both providers and customers make more informed financial and health-related decisions.

🎯 Problem Statement

Insurance companies want to estimate the cost of health insurance premiums more accurately based on customer profiles. By training a model on historical data, we can predict how much a new customer might be charged.

🧠 Objectives

Perform exploratory data analysis (EDA) on health insurance data.

Build regression models to predict insurance charges.

Evaluate model performance using appropriate metrics.

Interpret feature importance (e.g., effect of smoking or BMI on charges).

🗃️ Dataset

Source: Medical Cost Personal Dataset – Kaggle

Attributes:


age: Age of the person

bmi: Body Mass Index

children: Number of children

smoker: Smoking status (yes/no)

charges: Target variable – insurance premium cost

🧰 Tools & Technologies Used:

Language: Python

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Models Used: Linear Regression, Decision Tree Regressor, Random Forest Regressor

📊 Exploratory Data Analysis Highlights

Smokers pay significantly higher premiums than non-smokers.

Charges increase with age and BMI.

There is no strong correlation between the number of children and charges.

🔁 Data Preprocessing

Encoding categorical variables (e.g., smoker)

Train-test split

Feature scaling (for some models)

Outlier detection and handling (optional)

🤖 Model Training & Evaluation

Models were trained using:

SVM

Linear Regreesion

Decision Tree Regression

Gradient Boosting

extreme Gradient Boosting(XGB)

Evaluation Metrics:

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

R² Score


📁 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/PremAround_AI/HealthInsurancePrice_Prediction.git
cd HealthInsurancePrice_Prediction
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the notebook or script:

bash
Copy
Edit
jupyter notebook Insurance price prediction.ipynb
📌 Future Work
Include additional features like region, gender, or health conditions.

Deploy the model using Flask or Streamlit.

Build an interactive dashboard for live predictions.

🙌 Acknowledgements
Kaggle – Insurance Dataset

Scikit-learn Team

Python Community
