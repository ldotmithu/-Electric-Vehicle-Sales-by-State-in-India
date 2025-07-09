# 🚗⚡️ Electric Vehicle Sales in India: Data Analysis and Insights

This project analyzes the *"Electric Vehicle Sales by State in India"* dataset to uncover trends, patterns, and key insights into the adoption of electric vehicles (EVs) across different states and vehicle categories in India. 🌍🔋

## 1. Introduction 📝
The objective of this project is to provide a comprehensive analysis of EV sales data in India, helping to understand market dynamics, identify high-growth regions, and highlight popular vehicle categories. The insights gained can be valuable for policymakers, manufacturers, and investors in the EV sector. 🚀

## 2. Dataset 📊
The analysis is based on the `Electric Vehicle Sales by State in India.csv` dataset, which contains information on:

- **Year**: Year of sale. 📅
- **Month_Name**: Month of sale. 🗓️
- **Date**: Full date of sale. 📆
- **State**: Indian state/union territory where the sale occurred. 🗺️
- **Vehicle_Class**: Specific class of the vehicle (e.g., M-CYCLE/SCOOTER, CAR). 🏍️🚗
- **Vehicle_Category**: Broader category of the vehicle (e.g., 2-Wheelers, 3-Wheelers, 4-Wheelers). 🛵
- **Vehicle_Type**: Specific type within a category (e.g., 2W_Personal, 3W_Shared_LowSpeed). 🚲
- **EV_Sales_Quantity**: Number of EVs sold. 📈

## 3. Analysis and Insights 🔍
The analysis provides over 15 insights covering various aspects of EV sales:

- **Overall Sales Trends**: Yearly and monthly growth patterns, including year-on-year growth rates and seasonal variations. 📅📈
- **State-wise Performance**: Identification of top-performing states, states with lowest sales, and growth trends in recent years. 🗳️
- **Vehicle Category & Type Analysis**: Breakdown of sales by different vehicle categories (2-Wheelers, 3-Wheelers, 4-Wheelers, etc.) and specific vehicle types, highlighting their market share and growth over time. 🚗🛵
- **Market Share**: Percentage contribution of each state and vehicle category to the total EV sales. 📊
- **Popularity Trends**: Identification of the most popular vehicle classes and types, both overall and within leading states. 🌟
- **Data Overview**: Counts of unique states, vehicle classes, categories, and types present in the dataset. 📋

**Key findings** include the exponential growth of EV sales in recent years, the dominance of 2-Wheelers and 3-Wheelers in the market, and the leading role of states like Uttar Pradesh in EV adoption. 🚀🔝

## 4. Visualizations 📊🎨
To complement the numerical insights, several plots have been generated using `matplotlib.pyplot` to provide a visual understanding of the data:

- **Total EV Sales Over Time (Yearly)**: A line plot showing the overall growth trajectory. 📈
- **Top 10 States by Total EV Sales**: A bar chart highlighting the leading states in cumulative sales. 🏆
- **Total EV Sales by Vehicle Category**: A bar chart illustrating the sales distribution among different vehicle categories. 🚗🛵
- **Overall Monthly EV Sales Trend**: A bar chart depicting seasonal sales patterns. 🗓️
- **Growth of Top Vehicle Categories Over Time**: Line plots showing the individual growth trends of 2-Wheelers, 3-Wheelers, and 4-Wheelers. 📉

## 5. Code Structure 💻
The analysis is performed using Python with the `pandas` library for data manipulation and `matplotlib.pyplot` and `altair` for visualization.

The provided Python code includes:

- **Data Loading**: Reading the CSV file into a pandas DataFrame. 📂
- **Data Preprocessing**: Converting data types for Year and Date columns. 🛠️
- **Data Analysis**: Numerous pandas operations (grouping, aggregation, calculations) to derive the insights listed above. 🔢
- **Plotting**: Code to generate the aforementioned visualizations, which are saved as PNG image files and an interactive JSON file (for Altair chart). 🖼️

## 6. How to Run 🏃‍♂️
To run this analysis and reproduce the insights and visualizations:

1. Ensure you have **Python** installed. 🐍
2. Install the required libraries:
   ```bash
   pip install pandas matplotlib 
   ```
   