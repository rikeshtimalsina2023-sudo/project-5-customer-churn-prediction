"""Interactive Streamlit dashboard for the customer-churn model."""

from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

BASE = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE / "models" / "customer_churn_model.joblib"


@st.cache_resource
def load_model(model_path: str):
    """Load the trained pipeline once per Streamlit server."""
    model = joblib.load(model_path)
    if not hasattr(model, "predict") or not hasattr(model, "predict_proba"):
        raise TypeError("The saved artifact must provide predict and predict_proba methods.")
    return model

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📉", layout="wide")
st.title("📉 Customer Churn Predictor")
st.caption("Project 5 — Customer Churn Prediction & Analytics")

if not MODEL_PATH.exists():
    st.error("Model not found. Run the Jupyter notebook from beginning to end first.")
    st.stop()

try:
    model = load_model(str(MODEL_PATH))
except Exception as exc:
    st.error(f"The saved model could not be loaded: {exc}")
    st.stop()

st.subheader("Enter customer information")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)

with col2:
    phone = st.selectbox("Phone Service", ["No", "Yes"])
    multiple = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
    online_backup = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])

with col3:
    device = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
    tech = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
    streaming_tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
    streaming_movies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

monthly = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
total = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=max(70.0, monthly * max(tenure, 1)))
paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
payment = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

if st.button("Predict Churn", type="primary"):
    avg_spend = total / tenure if tenure > 0 else monthly
    tenure_group = (
        "0-12 months" if tenure <= 12 else
        "13-24 months" if tenure <= 24 else
        "25-48 months" if tenure <= 48 else
        "49-72 months"
    )
    partner_dep = int(partner == "Yes" or dependents == "Yes")

    row = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device,
        "TechSupport": tech,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total,
        "AvgMonthlySpend": avg_spend,
        "TenureGroup": tenure_group,
        "HasPartnerOrDependents": partner_dep
    }])

    prediction = model.predict(row)[0]
    classes = list(model.classes_)
    churn_index = classes.index(1)
    probability = model.predict_proba(row)[0, churn_index]

    c1, c2 = st.columns(2)
    c1.metric("Churn probability", f"{probability:.1%}")
    c2.metric("Prediction", "Likely to churn" if prediction == 1 else "Likely to stay")

    if prediction == 1:
        st.warning("The model predicts this customer as likely to churn.")
    else:
        st.success("The model predicts this customer as likely to stay.")
