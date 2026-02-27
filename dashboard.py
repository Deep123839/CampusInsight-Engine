import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="College Analytics Dashboard", layout="wide")

st.title("🎓 College Student Analytics Dashboard")

# Load Data
file_path = "students_data.xlsx"
df = pd.read_excel(file_path)

# Auto Result Calculation
df["Result"] = df["Percentage"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# ===============================
# 🔎 SIDEBAR FILTERS
# ===============================

st.sidebar.header("🔍 Filter Options")

result_filter = st.sidebar.multiselect(
    "Select Result",
    options=df["Result"].unique(),
    default=df["Result"].unique()
)

placement_filter = st.sidebar.multiselect(
    "Select Placement Status",
    options=df["PlacementStatus"].unique(),
    default=df["PlacementStatus"].unique()
)

search_name = st.sidebar.text_input("Search by Student Name")

filtered_df = df[
    (df["Result"].isin(result_filter)) &
    (df["PlacementStatus"].isin(placement_filter))
]

if search_name:
    filtered_df = filtered_df[filtered_df["Name"].str.contains(search_name, case=False)]

# ===============================
# 📊 KPI SECTION
# ===============================

total_students = len(filtered_df)
pass_count = len(filtered_df[filtered_df["Result"] == "Pass"])
fail_count = len(filtered_df[filtered_df["Result"] == "Fail"])
placed_count = len(filtered_df[filtered_df["PlacementStatus"] == "Placed"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", total_students)
col2.metric("Pass Students", pass_count)
col3.metric("Fail Students", fail_count)
col4.metric("Placed Students", placed_count)

st.divider()

# ===============================
# 🏆 TOPPER SECTION
# ===============================

if not filtered_df.empty:
    topper = filtered_df.loc[filtered_df["Percentage"].idxmax()]
    st.subheader("🏆 Topper")
    st.success(f"{topper['Name']} - {topper['Percentage']}%")

st.divider()

# ===============================
# 📊 CHARTS SECTION
# ===============================

col5, col6 = st.columns(2)

with col5:
    st.subheader("📌 Placement Distribution (Pie Chart)")
    placement_fig = px.pie(
        filtered_df,
        names="PlacementStatus",
        title="Placement Status Distribution"
    )
    st.plotly_chart(placement_fig, use_container_width=True)

with col6:
    st.subheader("📌 Result Distribution (Bar Chart)")
    result_fig = px.bar(
        filtered_df["Result"].value_counts(),
        title="Pass vs Fail"
    )
    st.plotly_chart(result_fig, use_container_width=True)

st.divider()

# ===============================
# 📊 Percentage Bar Chart
# ===============================

st.subheader("📈 Student Percentage Comparison")

percentage_fig = px.bar(
    filtered_df,
    x="Name",
    y="Percentage",
    color="Result",
    title="Student Percentage Overview"
)

st.plotly_chart(percentage_fig, use_container_width=True)

st.divider()

# ===============================
# 📋 DATA TABLE
# ===============================

st.subheader("📋 Student Data Table")
st.dataframe(filtered_df, use_container_width=True)