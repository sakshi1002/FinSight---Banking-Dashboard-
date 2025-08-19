# FinSight – Banking Dashboard & Loan Default Prediction

An end-to-end analytics solution for the banking domain: from raw data to interactive dashboards and loan default predictions.

---

##  Project Overview
**FinSight** is a comprehensive analytics workflow that starts with banking CSV data and builds through:
- Data ingestion and preprocessing
- Exploratory Data Analysis (EDA)
- KPI extraction and visualization via Power BI
- Predictive modeling using Logistic Regression
- Streamlit-based UI for easy, non-technical interaction

Designed to empower finance teams with actionable insights and predictive decision support.

---

##  Key Features

### 1. Data Pipeline & Analysis
- Processed raw banking CSV data with Python (Pandas, NumPy)
- Cleaned and transformed data, handled missing values and outliers
- Learned patterns in client behavior and key financial KPIs through detailed EDA

### 2. Interactive Visualizations
- Created a **Power BI dashboard** showcasing client demographics, transaction insights, and performance metrics
- Enabled intuitive exploration of KPIs via interactive visuals

### 3. Predictive Modeling
- Built a **Logistic Regression model** to predict loan default risks
- Achieved strong model performance (e.g., ~85% accuracy), helping preemptively flag high-risk applicants

### 4. End-User Deployment
- Delivered a user-friendly **Streamlit app** for interactive predictions—enter customer data and instantly receive default risk scores
- Enabled seamless adoption by business users without coding knowledge

---
##  Repository Contents

├── Banking-EDA.ipynb # EDA notebook: exploration and KPI development
├── BankingDashboard.pbix # Power BI file for interactive dashboard
├── LoanDefault_Prediction.ipynb # Notebook: modeling pipeline and evaluation
├── LoanDefaultPrediction.py # Streamlit app for ML model deployment
├── Banking.csv # Raw banking dataset
├── Loan_default.csv # Dataset for loan modeling
├── scaler.pkl # Saved preprocessing scaler
├── columns.pkl # Feature definitions for model input
├── loanDefault.pkl # Trained Logistic Regression model
└── README.md # Project documentation


---

##  How to Use

1. Clone the repo and explore the data via `Banking-EDA.ipynb`.
2. Open `BankingDashboard.pbix` in Power BI to interact with the visual analytics.
3. Inspect and experiment in `LoanDefault_Prediction.ipynb`.
4. Run Streamlit app:
   ```bash
   streamlit run LoanDefaultPrediction.py


##  Repository Contents

