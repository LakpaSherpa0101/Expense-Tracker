import streamlit as st
import pandas as pd
from datetime import date

# Web page title and icon
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="centered")

st.title("💰 Personal Expense Tracker")
st.write("Welcome! Track your daily expenses easily from your phone or PC.")

if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Input Form
with st.form("expense_form"):
    st.subheader("Add New Expense")
    
    col1, col2 = st.columns(2)
    with col1:
        exp_date = st.date_input("Date", date.today())
        amount = st.number_input("Amount (Rs.)", min_value=0.0, step=10.0)
    with col2:
        category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"])
        description = st.text_input("Description (Optional)")
        
    submit_btn = st.form_submit_button("➕ Add Expense", use_container_width=True)
    
    if submit_btn:
        if amount > 0:
            st.session_state.expenses.append({
                "Date": str(exp_date),
                "Category": category,
                "Amount": amount,
                "Description": description
            })
            st.success("Expense added successfully!")
        else:
            st.error("Please enter a valid amount.")

# Data Display
if len(st.session_state.expenses) > 0:
    st.divider()
    st.subheader("📊 Your Expenses")
    
    # Data lai table (DataFrame) ma dekhaune
    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Total nikalne
    total_expense = df["Amount"].sum()
    st.metric(label="Total Expense", value=f"Rs. {total_expense:,.2f}")
    
    # Clear Data Button
    if st.button("🗑️ Clear All Data"):
        st.session_state.expenses = []
        st.rerun()
else:
    st.info("No expenses added yet. Add your first expense above!")