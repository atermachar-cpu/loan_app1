import streamlit as st
import pandas as pd
import pickle as pkl

# My name
#Student Identified number

st.sidebar.markdown(" Name: **Ater Machar**")
st.sidebar.markdown("Student ID: **PIUS20230093**")
st.sidebar.markdown("University: **Parami University**")
st.sidebar.markdown(" Country: **Myanmar**")
st.sidebar.markdown(" Contient: **Asia**")
st.sidebar.markdown("Student Continent: **Africa**")
st.sidebar.markdown("Student Nationality: South Sudanese")


# Title
st.title("Loan Approval Prediction App")
Applicant_First_name = st.text_input("Applicant_First_Name")
Applicant_Second_name = st.text_input("Applicant_Second_Name")
Applicant_telephone = st.text_input("Applicant_email")
Applicant_telephone = st.text_input("Telephone")
Applicant_birth_date=st.text_input("Date")
university = st.text_input("Institution name")
st.cache_resource
def load_model():
    with open('LogisticRegression_pipeline.pkl', 'rb') as file:
        loaded_pipeline = pkl.load(file)
        return loaded_pipeline
    
# the loan application informations
st.subheader("Loan Application iformation")
years_employed = st.number_input("Years Employed", min_value=0, max_value=50, step=1)
annual_income = st.number_input("Annual Income", min_value=0, step=1000)
credit_score = st.number_input("Credit Score", min_value=0, max_value=850, step=1)
credit_history_years = st.number_input("Credit History (Years)", min_value=0.0, step=0.5)
savings_asset = st.number_input("Savings Asset", min_value=0, step=100)
loan_amount = st.number_input("Loan Amount", min_value=0, step=1000)
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, step=0.1)
debt_to_income_ratio = st.number_input("Debt-to-Income Ratio", min_value=0.0, step=0.01)
loan_to_income_ratio = st.number_input("Loan-to-Income Ratio", min_value=0.0, step=0.01)
payment_to_income_ratio = st.number_input("Payment-to-Income Ratio", min_value=0.0, step=0.01)
current_debt=st.number_input("current_debt",min_value=0.0, step=0.01)

occupation_status = st.selectbox("Occupation Status", ["Employed", "Unemployed", "Student", "Retired"])
product_type = st.selectbox("Product Type", ["Personal Loan", "Mortgage", "Auto Loan", "Credit Card"])
loan_intent = st.selectbox("Loan Intent", ["Education", "Home Improvement", "Medical", "Business", "Other"])
defaults_on_file = st.selectbox("Defaults on File", ["Yes", "No"])
delinquencies_last_2yrs = st.number_input("Delinquencies (Last 2 Years)", min_value=0, step=1)
derogatory_marks = st.text_input("Derogatory Marks")



# Prepare input data
input_data = pd.DataFrame([{
    'years_employed': years_employed,
    'annual_income': annual_income,
    'credit_score': credit_score,
    'credit_history_years': credit_history_years,
    'savings_asset': savings_asset,
    'loan_amount': loan_amount,
    'interest_rate': interest_rate,
    'debt_to_income_ratio': debt_to_income_ratio,
    'loan_to_income_ratio': loan_to_income_ratio,
    'payment_to_income_ratio': payment_to_income_ratio,
    'occupation_status': occupation_status,
    'product_type': product_type,
    'loan_intent': loan_intent,
    'savings_assets':savings_asset,
    'current_debt':current_debt,
    'defaults_on_file': defaults_on_file,
    'delinquencies_last_2yrs': delinquencies_last_2yrs,
    'derogatory_marks': derogatory_marks
}])

# Prediction Button
if st.button("Predict Loan Approval"):
    try:
        model=load_model()
        prediction = model.predict(input_data)[0]
        if prediction==0:
            st.success("Denied : ")
        else:
            st.success("Aprroval : ")
    except Exception as e:
        st.error(f"Error: {e}")
        st.write("Please check that the model and inputs match the training columns.")
