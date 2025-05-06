Activity 1 

The first thing to do is to import the Streamlit library with import streamlit as st and set a title, header, and some description text on the page. We create two input fields where the user can type their email and PIN, storing their input in two variables. Thereafter, the app displays what the user entered, showing both the email and PIN along with small icons to make it visually clear.

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/7cddbe5c4020ae231d6f3f71a65d6f7e2a5b7afe/Screenshot%20(199).png)

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/2239a5a21501f6f1e573b32b79c05f35819b4b3f/activity1_canedo.png)



Activity 2 

This Streamlit app begins by setting a title with st.title("FILE UPLOADER"), which displays at the top of the app. It then uses st.file_uploader() to create an upload button, allowing the user to select a CSV file. I upload the sales dataset. Additionally, there's a filtering option where you can select a column and pick a specific value from it. This helps you narrow down the data you're interested in, and the app will show you the filtered results. It provides an easy way to interact with and explore your CSV data.

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/a1c01b74c5ea2bfed1867812e6a49d5defca146d/Screenshot%20(200).png)

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/da489aa9a87894d3d36d26ff83648afdc1f12f42/activity2_canedo.png)




Activity 3 



In this Activity 3, I created an interactive interface for exploring data warehousing and enterprise data management topics. Users can select topics from a sidebar dropdown menu (selectbox), where users can choose from different topics. I also included tabs for additional content, such as "Real-Time Analytics" and "Cloud Data Warehousing," that provide users with deeper insights.

![mage alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/1756fe0c73a3d77ef79d65a5ccdaebb4e0d9f134/Screenshot%20(201).png)
![imag alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/137647397e225eb20a0b14733541902f6a8670c5/activity3_canedo.png)



Activity 4 

In this activity it provides an interactive COVID-19 data dashboard where users can select a country to view detailed statistics. I used the requests library and then processed it into a DataFrame with pandas to retrieve the COVID-19 data for the past 30 days. It computes daily new cases, deaths, and recoveries by calculating the difference in values day-over-day. The app then displays multiple charts: a line chart showing daily new cases, an area chart of cumulative cases, a dual-line chart comparing new deaths and recoveries, and a 7-day moving average of new cases. 

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/b03c2182e05af56c9e86e2607776946a13284772/Screenshot%20(204).png)

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/ade3eeec5622a7f53f46af2977daa7c10107b68e/activity4_canedo.png)



Activity 5

In activity 5, my system is managing an inventory, allowing users to view and add products and categories in a database. The app connects to a MySQL database via SQLAlchemy and requires the user to enter valid login credentials ("inventoryadmin" and "inventory123") through the sidebar. After logging in with predefined credentials, users can view and filter records from "products" or "categories" tables. The app also allows adding new records to the selected table, either products (with name, category, price, and quantity) or categories (with name and description).

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/85cdab3b086b817a8c311fc4eccb14642695cf55/Screenshot%20(206).png)

![image alt}(https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/19d728704bd5f9ea90aaa3c48f80be43ac11f19d/activity5_canedo.png)

![image alt](https://github.com/JonathanBoiserCanedo/ITBAN2_STREAMLIT_ACT_CANEDO/blob/117bf28a4f3fce6cb637a721466b31504d7d1636/activity5_canedo2.png)


Activity 6 



Activity 6 is an app that lets you take a snapshot with your webcam. It has brightness and contrast in real time using sliders. It also applies filters like grayscale and Canny edge detection by checking a box. When you click the "Take Snapshot" button, the app captures the current frame, applies your adjustments and filters, and saves it with a timestamped filename. The video keeps playing until you take a snapshot, after which it stops, and you'll get a notification that the snapshot has been saved.
