import streamlit as st
import pandas as pd  

# CONFIGS
YEAR = 2023
PREVIOUS_YEAR = 2022
CITIES = ["🏙️ Karachi", "🌆 Lahore", "🏢 Islamabad"]
DATA_PATH = "pakistan_sales_data.csv"  # Use your local file

st.title("☪ Pakistan Sales Dashboard", anchor=False)

@st.cache_data
def get_and_prepare_data(data):
    df = pd.read_csv(data).assign(
        date_of_sale=lambda df: pd.to_datetime(df["date_of_sale"]),
        month=lambda df: df["date_of_sale"].dt.month,
        year=lambda df: df["date_of_sale"].dt.year,
    )
    return df

df = get_and_prepare_data(DATA_PATH)

# Calculate total revenue for each city and year
city_revenues = (
    df.groupby(["city", "year"])["sales_amount"]
    .sum()
    .unstack()
    .assign(change=lambda x: x.pct_change(axis=1)[YEAR] * 100)
)

# Display metrics with emojis
columns = st.columns(3)
for i, city in enumerate(CITIES):
    with columns[i]:
        st.metric(
            label=city,
            value=f"PKR {city_revenues.loc[city.replace('🏙️ ', '').replace('🌆 ', '').replace('🏢 ', ''), YEAR]:,.0f}",
            delta=f"📈 {city_revenues.loc[city.replace('🏙️ ', '').replace('🌆 ', '').replace('🏢 ', ''), 'change']:.0f}% vs. last year",
        )

# Filter options
left_col, right_col = st.columns(2)
analysis_type = left_col.selectbox(
    label="📊 Analysis by:",
    options=["📆 Month", "🛒 Product Category"],
    key="analysis_type",
)
selected_city = right_col.selectbox("🏢 Select a city:", CITIES)

# Toggle for selecting the year
previous_year_toggle = st.toggle(
    value=False, label="📅 Compare with Previous Year", key="switch_visualization"
)
visualization_year = PREVIOUS_YEAR if previous_year_toggle else YEAR

st.write(f"**📈 Sales for {visualization_year}**")

# Filter data for visualization
if analysis_type == "🛒 Product Category":
    filtered_data = (
        df.query("city == @selected_city.replace('🏙️ ', '').replace('🌆 ', '').replace('🏢 ', '') & year == @visualization_year")
        .groupby("product_category")["sales_amount"]
        .sum()
        .reset_index()
    )
else:
    filtered_data = (
        df.query("city == @selected_city.replace('🏙️ ', '').replace('🌆 ', '').replace('🏢 ', '') & year == @visualization_year")
        .groupby("month")["sales_amount"]
        .sum()
        .reset_index()
    )
    filtered_data["month"] = filtered_data["month"].apply(lambda x: f"{x:02d}")

# Display chart
st.bar_chart(filtered_data.set_index(filtered_data.columns[0])["sales_amount"])
