import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import OrdinalEncoder

# Load model and preprocessing objects
model = joblib.load(r"C:\Users\Admin\OneDrive\Desktop\Power BI\PBI_Project\FinanceDomainProjects\BankingProject\Loan_defaultML\loanDefault.pkl")
scaler = joblib.load(r"C:\Users\Admin\OneDrive\Desktop\Power BI\PBI_Project\FinanceDomainProjects\BankingProject\Loan_defaultML\scaler.pkl")
expected_columns = joblib.load(r"C:\Users\Admin\OneDrive\Desktop\Power BI\PBI_Project\FinanceDomainProjects\BankingProject\Loan_defaultML\columns.pkl")

# Title
st.markdown("<h1 style='text-align: center;'>💳 Loan Default Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict whether a loan applicant is likely to default</p>", unsafe_allow_html=True)
st.markdown("---")

st.header("Applicant Details")

# Personal Details
with st.expander("Basic Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider("Age", 18, 80, 30)
        marital = st.selectbox("Marital Status", ['Single','Married','Divorced'])
    with col2:
        income = st.number_input("Annual Income", min_value=1000, max_value=1000000, step=1000)
        employment = st.selectbox("Employment Type", ['Unemployed','Full-time','Part-time','Self-employed'])
    with col3:
        cred_score = st.slider("Credit Score", 300, 850, 650)
        education = st.selectbox("Education", ["High School","Bachelor's","Master's","PhD"])

# Loan Details
with st.expander("Loan Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        loan_amt = st.number_input("Loan Amount", min_value=500, max_value=500000, step=500)
        purpose = st.selectbox("Loan Purpose", ['Education','Auto','Home','Business','Other'])
    with col2:
        dti_ratio = st.number_input("DTI Ratio (%)", min_value=0.0, max_value=100.0, step=0.1, value=20.0)
        interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=50.0, step=0.1, value=10.0)
    with col3:
        loan_term = st.number_input("Loan Term (months)", min_value=6, max_value=360, step=6, value=120)
        months_employed = st.number_input("Months Employed", min_value=0, max_value=600, step=1, value=24)
        num_credit_lines = st.number_input("Number of Credit Lines", min_value=0, max_value=50, step=1, value=5)

# Optional Checks
with st.expander("Other Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        mortgage = st.selectbox("Has Mortgage?", ["No","Yes"])
    with col2:
        dependents = st.selectbox("Has Dependents?", ["No","Yes"])
    with col3:
        cosigner = st.selectbox("Has Co-Signer?", ["No","Yes"])

# Build input dataframe
input_dict = {
    'Income': income,
    'LoanAmount': loan_amt,
    'Age': age,
    'CreditScore': cred_score,
    'Education': education,
    'EmploymentType': employment,
    'MaritalStatus': marital,
    'LoanPurpose': purpose,
    'HasMortgage': 1 if mortgage=="Yes" else 0,
    'HasDependents': 1 if dependents=="Yes" else 0,
    'HasCoSigner': 1 if cosigner=="Yes" else 0,
    'DTIRatio': dti_ratio,
    'InterestRate': interest_rate,
    'LoanTerm': loan_term,
    'MonthsEmployed': months_employed,
    'NumCreditLines': num_credit_lines
}
input_data = pd.DataFrame([input_dict])

# Encode categorical variables
education_ord = ["High School","Bachelor's","Master's","PhD"]
emp_ord       = ['Unemployed','Full-time','Part-time','Self-employed']
married_ord   = ['Single','Married','Divorced']
purpose_ord   = ['Education','Auto','Home','Business','Other']

oe = OrdinalEncoder(categories=[education_ord, emp_ord, married_ord, purpose_ord])
input_data[['Education','EmploymentType','MaritalStatus','LoanPurpose']] = \
    oe.fit_transform(input_data[['Education','EmploymentType','MaritalStatus','LoanPurpose']])

# Reorder columns
input_data = input_data[expected_columns]

# Scale input
input_scaled = scaler.transform(input_data)

# Prediction button at the end
if st.button("Predict Default Risk"):
    y_prob = model.predict_proba(input_scaled)[:,1][0]
    y_pred = int(y_prob >= 0.35)

    st.markdown("---")
    st.subheader("📊 Prediction Result")
    if y_pred == 1:
        st.error(f"⚠️ High Risk of Default (Probability = {y_prob:.2f})")
    else:
        st.success(f"✅ Low Risk of Default (Probability = {y_prob:.2f})")
