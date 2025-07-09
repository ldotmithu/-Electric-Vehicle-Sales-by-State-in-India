import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Loading and cleaning data
def load_and_clean_data():
    df = pd.read_csv("Data/Electric Vehicle Sales by State in India.csv")
    
    # Converting Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Handling missing values
    df['EV_Sales_Quantity'] = df['EV_Sales_Quantity'].fillna(0)
    
    # Converting EV_Sales_Quantity to integer
    df['EV_Sales_Quantity'] = df['EV_Sales_Quantity'].astype(int)
    
    return df

# Analysis functions
def total_sales_by_year(df):
    return df.groupby('Year')['EV_Sales_Quantity'].sum()

def sales_by_vehicle_category(df):
    return df.groupby('Vehicle_Category')['EV_Sales_Quantity'].sum()

def top_states_by_sales(df, year=2023):
    return df[df['Year'] == year].groupby('State')['EV_Sales_Quantity'].sum().nlargest(5)

def sales_trend_by_category(df):
    return df.groupby(['Year', 'Vehicle_Category'])['EV_Sales_Quantity'].sum().unstack()

def top_vehicle_types(df):
    return df.groupby('Vehicle_Type')['EV_Sales_Quantity'].sum().nlargest(5)

def state_category_distribution(df, year=2023):
    return df[df['Year'] == year].groupby(['State', 'Vehicle_Category'])['EV_Sales_Quantity'].sum().unstack()

def monthly_sales_trend(df, year=2023):
    return df[df['Year'] == year].groupby('Month_Name')['EV_Sales_Quantity'].sum()

def sales_by_vehicle_class(df):
    return df.groupby('Vehicle_Class')['EV_Sales_Quantity'].sum()

def growth_rate(df):
    yearly_sales = total_sales_by_year(df)
    growth = yearly_sales.pct_change() * 100
    return growth

def state_wise_growth(df):
    state_yearly = df.groupby(['State', 'Year'])['EV_Sales_Quantity'].sum().unstack()
    growth = state_yearly.pct_change(axis=1) * 100
    return growth.mean(axis=1).nlargest(5)

def category_distribution_by_state(df, state, year=2023):
    return df[(df['State'] == state) & (df['Year'] == year)].groupby('Vehicle_Category')['EV_Sales_Quantity'].sum()

def sales_by_vehicle_type_year(df):
    return df.groupby(['Year', 'Vehicle_Type'])['EV_Sales_Quantity'].sum().unstack()

def top_states_by_vehicle_type(df, vehicle_type, year=2023):
    return df[(df['Vehicle_Type'] == vehicle_type) & (df['Year'] == year)].groupby('State')['EV_Sales_Quantity'].sum().nlargest(5)

def sales_correlation(df):
    return df.groupby(['Year', 'State'])['EV_Sales_Quantity'].sum().unstack().corr()

def seasonal_pattern(df):
    monthly_avg = df.groupby(['Year', 'Month_Name'])['EV_Sales_Quantity'].sum().unstack()
    return monthly_avg.mean()

# Main analysis function
def analyze_ev_sales():
    df = load_and_clean_data()
    
    # Creating visualizations
    plt.figure(figsize=(15, 10))
    
    # 1. Total sales trend over years
    plt.subplot(3, 2, 1)
    total_sales_by_year(df).plot(kind='line', title='Total EV Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales Quantity')
    
    # 2. Sales by vehicle category
    plt.subplot(3, 2, 2)
    sales_by_vehicle_category(df).plot(kind='bar', title='EV Sales by Vehicle Category')
    plt.xlabel('Vehicle Category')
    plt.ylabel('Sales Quantity')
    
    # 3. Top 5 states by sales in 2023
    plt.subplot(3, 2, 3)
    top_states_by_sales(df).plot(kind='bar', title='Top 5 States by EV Sales (2023)')
    plt.xlabel('State')
    plt.ylabel('Sales Quantity')
    
    # 4. Sales trend by category over years
    plt.subplot(3, 2, 4)
    sales_trend_by_category(df).plot(kind='line', title='Sales Trend by Vehicle Category')
    plt.xlabel('Year')
    plt.ylabel('Sales Quantity')
    
    # 5. Top 5 vehicle types
    plt.subplot(3, 2, 5)
    top_vehicle_types(df).plot(kind='bar', title='Top 5 Vehicle Types by Sales')
    plt.xlabel('Vehicle Type')
    plt.ylabel('Sales Quantity')
    
    plt.tight_layout()
    plt.savefig('ev_sales_analysis.png')
    plt.close()

    # Collecting insights
    insights = []
    
    # Insight 1: Total sales growth
    total_sales = total_sales_by_year(df)
    insights.append(f"1. Total EV sales increased from {total_sales[2014]:.0f} in 2014 to {total_sales[2023]:.0f} in 2023")
    
    # Insight 2: Dominant vehicle category
    category_sales = sales_by_vehicle_category(df)
    top_category = category_sales.idxmax()
    insights.append(f"2. {top_category} is the dominant vehicle category with {category_sales[top_category]:.0f} total sales")
    
    # Insight 3: Top state
    top_state = top_states_by_sales(df).index[0]
    insights.append(f"3. {top_state} led EV sales in 2023 with {top_states_by_sales(df)[top_state]:.0f} units")
    
    # Insight 4: Growth rate
    growth = growth_rate(df)
    insights.append(f"4. Average yearly growth rate: {growth.mean():.2f}%")
    
    # Insight 5: Top vehicle type
    top_type = top_vehicle_types(df).index[0]
    insights.append(f"5. {top_type} is the most popular vehicle type with {top_vehicle_types(df)[top_type]:.0f} units sold")
    
    # Insight 6: State with highest growth
    top_growth_state = state_wise_growth(df).index[0]
    insights.append(f"6. {top_growth_state} showed the highest average growth rate")
    
    # Insight 7: E-Rickshaw adoption
    erickshaw_sales = df[df['Vehicle_Type'] == '3W_Shared_LowSpeed']['EV_Sales_Quantity'].sum()
    insights.append(f"7. E-Rickshaws (3W_Shared_LowSpeed) total sales: {erickshaw_sales:.0f}")
    
    # Insight 8: 2-Wheeler popularity
    two_wheeler_sales = df[df['Vehicle_Category'] == '2-Wheelers']['EV_Sales_Quantity'].sum()
    insights.append(f"8. 2-Wheelers account for {two_wheeler_sales:.0f} total sales")
    
    # Insight 9: Uttar Pradesh category distribution
    up_dist = category_distribution_by_state(df, 'Uttar Pradesh')
    insights.append(f"9. Uttar Pradesh's top category in 2023: {up_dist.idxmax()} with {up_dist.max():.0f} units")
    
    # Insight 10: Monthly sales pattern
    monthly_trend = monthly_sales_trend(df)
    peak_month = monthly_trend.idxmax()
    insights.append(f"10. Peak sales month in 2023: {peak_month} with {monthly_trend[peak_month]:.0f} units")
    
    # Insight 11: Bus sales trend
    bus_sales = df[df['Vehicle_Category'] == 'Bus']['EV_Sales_Quantity'].sum()
    insights.append(f"11. Total bus sales: {bus_sales:.0f}")
    
    # Insight 12: Delhi's contribution
    delhi_sales = df[df['State'] == 'Delhi']['EV_Sales_Quantity'].sum()
    total_sales_all = df['EV_Sales_Quantity'].sum()
    insights.append(f"12. Delhi contributes {delhi_sales/total_sales_all*100:.2f}% of total EV sales")
    
    # Insight 13: Vehicle class diversity
    class_count = len(df['Vehicle_Class'].unique())
    insights.append(f"13. Dataset includes {class_count} unique vehicle classes")
    
    # Insight 14: 4-Wheeler personal use
    four_wheeler_personal = df[df['Vehicle_Type'] == '4W_Personal']['EV_Sales_Quantity'].sum()
    insights.append(f"14. 4-Wheeler personal vehicles sold: {four_wheeler_personal:.0f}")
    
    # Insight 15: Regional variations
    state_count = len(df['State'].unique())
    insights.append(f"15. EV sales recorded across {state_count} states/UTs")
    
    # Insight 16: Low-speed vehicle adoption
    low_speed_sales = df[df['Vehicle_Type'].str.contains('LowSpeed')]['EV_Sales_Quantity'].sum()
    insights.append(f"16. Low-speed vehicles (E-Rickshaw) total sales: {low_speed_sales:.0f}")
    
    # Printing insights
    print("Electric Vehicle Sales Analysis Insights:")
    for insight in insights:
        print(insight)

if __name__ == "__main__":
    analyze_ev_sales()