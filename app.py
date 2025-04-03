import streamlit as st
import joblib
clf=joblib.load('loan_data1.joblib')
st.title('LOAN APP RCE')
m=st.number_input('Enter Gender 0:Male,1:Female')
g=st.number_input('Enter Maritial Status 0:No,1:Yes')
ai=st.number_input('Enter Applicant Income in thousands')
la=st.number_input('Enter Loan Amount in thousands')
if st.button('PREDICT'):
    prediction=clf.predict([[g,m,ai,la]])
    if prediction=='Y':
        st.text('LOAN APPROVED')
    else:
        st.text('LOAN IS REJECTED')
