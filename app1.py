import streamlit as st
import pandas as pd

st.title("FILE UPLOADER")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    show_raw_data = st.checkbox("Show raw data")
    if show_raw_data:
        st.write("Raw Data:", df)

    columns = df.columns.tolist()
    column_to_filter = st.selectbox("Select a column to filter by", columns)
    
    unique_values = df[column_to_filter].unique()
    selected_value = st.selectbox(f"Select a value from {column_to_filter}", unique_values)
    
    filtered_df = df[df[column_to_filter] == selected_value]
    st.write(f"Filtered data for {column_to_filter} = {selected_value}:")
    st.dataframe(filtered_df)
