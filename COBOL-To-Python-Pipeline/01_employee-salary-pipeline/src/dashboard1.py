import streamlit as st
import pandas as pd

# ============================================================
#  PHASE 4 — Streamlit Dashboard
#  Employee Salary Interactive Dashboard
# ============================================================

st.set_page_config(
    page_title="Employee Salary Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Employee Salary Dashboard")
st.markdown("**COBOL to Python Modernization Project**")
st.divider()

# Load CSV data
df = pd.read_csv(r"C:\Mainframe-Modernization\COBOL-To-Python-Pipeline\01_employee-salary-pipeline\output\employees.csv")

# ============================================================
#  SIDEBAR FILTERS
# ============================================================
st.sidebar.header("🔎 Filters")

# Filter 1 — Search by name
search = st.sidebar.text_input("Search Employee Name")

# Filter 2 — Salary range slider
min_sal = int(df['SALARY'].min())
max_sal = int(df['SALARY'].max())
sal_range = st.sidebar.slider(
    "Salary Range",
    min_value=min_sal,
    max_value=max_sal,
    value=(min_sal, max_sal)
)

# Filter 3 — Sort by
sort_by = st.sidebar.selectbox(
    "Sort By",
    ["EMP_NAME", "SALARY", "WORK_HRS", "WORK_RATE"]
)

sort_order = st.sidebar.radio(
    "Sort Order",
    ["Ascending", "Descending"]
)

# ============================================================
#  APPLY FILTERS
# ============================================================
filtered_df = df.copy()

# Apply name search
if search:
    filtered_df = filtered_df[
        filtered_df['EMP_NAME'].str.contains(search, case=False)
    ]

# Apply salary range
filtered_df = filtered_df[
    (filtered_df['SALARY'] >= sal_range[0]) &
    (filtered_df['SALARY'] <= sal_range[1])
]

# Apply sort
filtered_df = filtered_df.sort_values(
    by=sort_by,
    ascending=(sort_order == "Ascending")
)

# ============================================================
#  SUMMARY CARDS
# ============================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Employees", len(filtered_df))
with col2:
    st.metric("Total Salary", f"₹{filtered_df['SALARY'].sum():,.2f}")
with col3:
    st.metric("Average Salary", f"₹{filtered_df['SALARY'].mean():,.2f}" if len(filtered_df) > 0 else "₹0.00")
with col4:
    st.metric("Highest Salary", f"₹{filtered_df['SALARY'].max():,.2f}" if len(filtered_df) > 0 else "₹0.00")

st.divider()

# ============================================================
#  BAR CHART
# ============================================================
st.subheader("💰 Salary Comparison")
if len(filtered_df) > 0:
    st.bar_chart(filtered_df.set_index('EMP_NAME')['SALARY'])
else:
    st.warning("No employees found matching your filters!")

st.divider()

# ============================================================
#  DATA TABLE
# ============================================================
st.subheader("👥 Employee Data")
st.dataframe(filtered_df, use_container_width=True)

# ============================================================
#  DOWNLOAD BUTTON
# ============================================================
st.divider()
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_employees.csv",
    mime="text/csv"
)