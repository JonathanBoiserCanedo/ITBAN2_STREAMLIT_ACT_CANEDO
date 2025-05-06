import streamlit as st

# Sidebar for Filters and Options
st.sidebar.title("Data Warehousing & Enterprise Data Management")
option = st.sidebar.selectbox(
    "Select a Topic", 
    ("Overview of Data Warehousing", 
     "ETL Process", 
     "Data Integration", 
     "Data Governance", 
     "Performance Optimization")
)

# Toggleable section for introductory content
with st.expander("What is Data Warehousing and Enterprise Data Management?"):
    st.write("""
    Data Warehousing is a process of collecting and managing data from different sources 
    to enable efficient querying and reporting. Enterprise Data Management (EDM) is an 
    overarching strategy that ensures an organization's data is accurate, consistent, and secure.
    """)

# Layout with Columns for Topic Details
if option == "Overview of Data Warehousing":
    st.title("Overview of Data Warehousing")
    col1, col2 = st.columns(2)
    with col1:
        st.header("What is a Data Warehouse?")
        st.write("""
        A Data Warehouse is a centralized repository that allows you to store historical 
        data for business intelligence (BI) and analytics. It involves organizing data 
        for easy access and reporting.
        """)
    with col2:
        st.header("Components of a Data Warehouse")
        st.write("""
        - *Data Sources*: Operational databases or external data sources.
        - *ETL Process*: Extracting, transforming, and loading data into the warehouse.
        - *Data Marts*: Subsets of data tailored to specific departments or business needs.
        """)

elif option == "ETL Process":
    st.title("ETL Process in Data Warehousing")
    st.write("""
    The *ETL (Extract, Transform, Load)* process is crucial for getting data into a data warehouse:
    - *Extract*: Data is extracted from multiple source systems.
    - *Transform*: The data is cleaned, normalized, and enriched for analysis.
    - *Load*: The transformed data is loaded into the data warehouse.
    """)

elif option == "Data Integration":
    st.title("Data Integration in Data Warehousing")
    st.write("""
    Data integration is essential to consolidate data from disparate sources into a unified view. Key methods include:
    - *Data Replication*: Copying data from multiple systems into the warehouse.
    - *Data Federation*: Integrating data without physically moving it.
    - *Data Virtualization*: Providing a real-time view of data across systems.
    """)

elif option == "Data Governance":
    st.title("Data Governance in Enterprise Data Management")
    st.write("""
    Data governance ensures that data is accurate, secure, and compliant with policies and regulations:
    - *Data Quality*: Ensures data is accurate and complete.
    - *Data Security*: Protects sensitive data from unauthorized access.
    - *Data Privacy*: Ensures compliance with laws like GDPR.
    """)

elif option == "Performance Optimization":
    st.title("Performance Optimization in Data Warehousing")
    st.write("""
    Data warehouse performance can be optimized in several ways:
    - *Indexing*: Speed up queries by creating indexes on frequently queried columns.
    - *Partitioning*: Split large tables into smaller, more manageable pieces.
    - *Query Optimization*: Use efficient queries and caching mechanisms.
    """)

# Using st.tabs for additional content sections related to data management
st.tabs(["Real-Time Analytics", "Cloud Data Warehousing", "Data Archiving"])

if "Real-Time Analytics" in st.session_state:
    st.write("Learn how real-time analytics is integrated into data warehouses for immediate insights.")
elif "Cloud Data Warehousing" in st.session_state:
    st.write("Explore how cloud technologies are used to scale data warehousing systems.")
elif "Data Archiving" in st.session_state:
    st.write("Discover strategies for archiving data in the long term and managing data retention.")
