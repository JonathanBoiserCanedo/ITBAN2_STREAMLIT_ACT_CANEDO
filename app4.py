import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Database Configuration
DB_USER = 'root'
DB_PASSWORD = None
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'inventory'

@st.cache_resource
def get_connection():
    if DB_PASSWORD is None:
        connection_url = f"mysql+pymysql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    else:
        connection_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    return create_engine(connection_url)

engine = get_connection()

# Authentication
st.sidebar.header("🔐 Inventory Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

def authenticate(user, pwd):
    return user == "inventoryadmin" and pwd == "inventory123"

if authenticate(username, password):
    st.success(f"Welcome, {username}!")
    st.title("📦 Product Inventory Dashboard")

    table_name = st.selectbox("Choose table to view", ["products", "categories"])

    st.subheader("📄 View Records")
    filter_query = st.text_input("Optional SQL filter (e.g., category = 'Electronics')")

    query = f"SELECT * FROM {table_name}"
    if filter_query.strip():
        query += f" WHERE {filter_query}"

    with engine.connect() as conn:
        result_df = pd.read_sql(text(query), conn)

    st.dataframe(result_df)

    st.subheader(f"➕ Add New Record to `{table_name}`")

    with st.form(key='insert_form'):
        if table_name == 'products':
            product_name = st.text_input("Product Name")
            category = st.text_input("Category")
            price = st.number_input("Price", min_value=0.0, step=0.01)
            quantity = st.number_input("Quantity", min_value=0, step=1)
            submit = st.form_submit_button("Insert Product")

            if submit:
                insert_query = text("""
                    INSERT INTO products (product_name, category, price, quantity)
                    VALUES (:name, :cat, :price, :qty)
                """)
                with engine.connect() as conn:
                    conn.execute(insert_query, {
                        "name": product_name,
                        "cat": category,
                        "price": price,
                        "qty": quantity
                    })
                    conn.commit()
                st.success("✅ Product inserted!")

        elif table_name == 'categories':
            category_name = st.text_input("Category Name")
            description = st.text_area("Description")
            submit = st.form_submit_button("Insert Category")

            if submit:
                insert_query = text("""
                    INSERT INTO categories (category_name, description)
                    VALUES (:name, :desc)
                """)
                with engine.connect() as conn:
                    conn.execute(insert_query, {
                        "name": category_name,
                        "desc": description
                    })
                    conn.commit()
                st.success("✅ Category added!")

else:
    st.warning("Please enter valid login credentials.")
