import streamlit as st
import pandas as pd

# ============================================================
#  PHASE 4 — Streamlit Dashboard
#  Employee Salary Interactive Dashboard
# ============================================================

# Page config
st.set_page_config(
    page_title="Employee Salary Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Employee Salary Dashboard")
st.markdown("**COBOL to Python Modernization Project**")
st.divider()

# Load CSV data
df = pd.read_csv(r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\01_employee-salary-pipeline\output\employees.csv")

# ── Summary Cards ──
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Employees", len(df))

with col2:
    st.metric("Total Salary", f"₹{df['SALARY'].sum():,.2f}")

with col3:
    st.metric("Average Salary", f"₹{df['SALARY'].mean():,.2f}")

st.divider()

# ── Bar Chart ──
st.subheader("Salary Comparison")
st.bar_chart(df.set_index('EMP_NAME')['SALARY'])

st.divider()

# ── Data Table ──
st.subheader("Employee Data")
st.dataframe(df, use_container_width=True)