# Project 5 — Customer Churn Prediction & Analytics

## Overview

An end-to-end machine-learning project that predicts telecom customer churn and analyzes the customer segments most associated with churn. It is designed to be run locally from a notebook or explored through a Streamlit dashboard.

## Pipeline
Raw CSV → data cleaning → EDA → feature engineering → preprocessing → Logistic Regression + Random Forest → evaluation → feature importance → error analysis → saved model → SQLite/SQL → Streamlit dashboard.

## Models
- Logistic Regression
- Random Forest

Metrics:
- Accuracy
- Precision
- Recall
- F1
- ROC-AUC

## Repository contents

- `customer_churn.ipynb` — complete project workflow
- `models/customer_churn_model.joblib` — trained Random Forest pipeline
- `app/dashboard.py` — interactive churn predictor with churn probability
- `data/raw/` and `data/processed/` — source and cleaned data produced by the notebook
- `customer_churn.db` — SQLite database used by the SQL examples
- `sql/analytics.sql` — SQL analysis
- `requirements.txt` — dependencies

## Data source

The notebook downloads IBM's Telco Customer Churn sample dataset and stores a local copy in `data/raw/`. The data is used for learning and portfolio purposes; see the [IBM source dataset](https://github.com/IBM/watsonx-ai-samples/tree/master/cpd4.5/data/customer_churn).

## Run
1. Create and activate a Python virtual environment (Python 3.10+ recommended).
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run `customer_churn.ipynb` from top to bottom. This creates the model, processed dataset, and SQLite database.
4. Start the dashboard: `python -m streamlit run app/dashboard.py`

For a non-interactive reproducibility check, run:

```bash
jupyter nbconvert --to notebook --execute --stdout customer_churn.ipynb > /dev/null
python -m unittest discover -s tests -v
```

## Dashboard

Choose a customer's service, contract, and billing details, then select **Predict Churn**. The dashboard reports the probability of churn and a plain-language prediction. The model is cached after its first successful load so subsequent dashboard interactions are fast.

## Skills demonstrated
Python, Pandas, NumPy, data cleaning, EDA, feature engineering, categorical encoding, scaling, classification, Logistic Regression, Random Forest, model evaluation, feature importance, SQL, SQLite, Streamlit, and automated dashboard testing.
