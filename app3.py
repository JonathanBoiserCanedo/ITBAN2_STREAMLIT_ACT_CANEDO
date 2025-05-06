import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.title("🦠 COVID-19 Data Dashboard - Enhanced Charts")

country = st.selectbox("Choose a country", ["USA", "Philippines", "India", "Brazil", "Germany"])

url = f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=30"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'timeline' in data:
        timeline = data['timeline']
        cases = pd.Series(timeline['cases'])
        deaths = pd.Series(timeline['deaths'])
        recovered = pd.Series(timeline['recovered'])

        df = pd.DataFrame({
            'Date': pd.to_datetime(cases.index),
            'Cases': cases.values,
            'Deaths': deaths.values,
            'Recovered': recovered.values
        })

        # Compute daily new values
        df['New Cases'] = df['Cases'].diff().fillna(0)
        df['New Deaths'] = df['Deaths'].diff().fillna(0)
        df['New Recovered'] = df['Recovered'].diff().fillna(0)

        df.set_index('Date', inplace=True)

        # Chart 1: Line chart of daily new cases
        st.subheader("📈 Daily New Cases")
        st.line_chart(df['New Cases'])

        # Chart 2: Area chart of cumulative cases
        st.subheader("🌄 Cumulative Cases Over Time")
        st.area_chart(df['Cases'])

        # Chart 3: Dual-line chart: new deaths and new recoveries
        st.subheader("📊 New Deaths vs. Recoveries")
        st.line_chart(df[['New Deaths', 'New Recovered']])

        # Chart 4: Moving average (7-day) of new cases
        df['7-day Avg Cases'] = df['New Cases'].rolling(7).mean()
        st.subheader("📉 7-Day Moving Average of New Cases")
        st.line_chart(df['7-day Avg Cases'])

        # Chart 5: Pie chart of last day's new data
        st.subheader("📌 Latest Day Breakdown (New Cases)")
        latest_day = {
            'New Cases': df['New Cases'].iloc[-1],
            'New Deaths': df['New Deaths'].iloc[-1],
            'New Recovered': df['New Recovered'].iloc[-1]
        }
        fig, ax = plt.subplots()
        ax.pie(latest_day.values(), labels=latest_day.keys(), autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    else:
        st.error("No timeline data found.")
else:
    st.error(f"API request failed with status code {response.status_code}")
