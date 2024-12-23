# add clear button
# add scroll functionality
# fix render logic




# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Frame, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load your dataset (replace with your actual file path)
df = pd.read_csv('sales.csv')

# Function to create the plots
def create_plots():
    # Create a Tkinter window
    root = Tk()
    root.title("Sales Data Visualizations")
    
    # Frame to hold the plots
    canvas_frame = Frame(root)
    canvas_frame.pack(fill='both', expand=True)

    # 1. Countplot: Distribution of Regions
    fig1 = plt.Figure(figsize=(10, 6))
    sns.countplot(x='Region', data=df, palette='Set1', ax=fig1.add_subplot(111))
    Button(root, text="Display Distribution of Regions", command=lambda: display_plot(fig1, canvas_frame)).pack()

    # 2. Barplot: Average Order Value by Region
    fig2 = plt.Figure(figsize=(10, 6))
    sns.barplot(x='Region', y='Average_Order_Value', data=df, palette='Blues', ax=fig2.add_subplot(111))
    Button(root, text="Display Average Order Value by Region", command=lambda: display_plot(fig2, canvas_frame)).pack()

    # 3. Boxplot: Distribution of Purchase Frequency by Region
    fig3 = plt.Figure(figsize=(10, 6))
    sns.boxplot(x='Region', y='Purchase_Frequency', data=df, palette='Set2', ax=fig3.add_subplot(111))
    Button(root, text="Display Purchase Frequency by Region", command=lambda: display_plot(fig3, canvas_frame)).pack()

    # 5. Violin Plot: Churn Probability by Region
    fig5 = plt.Figure(figsize=(10, 6))
    sns.violinplot(x='Region', y='Churn_Probability', data=df, palette='muted', ax=fig5.add_subplot(111))
    Button(root, text="Display Churn Probability by Region", command=lambda: display_plot(fig5, canvas_frame)).pack()

    # 6. Pairplot: Relationships between Numeric Variables
    fig6 = plt.Figure(figsize=(10, 6))
    sns.pairplot(df[['Lifetime_Value', 'Average_Order_Value', 'Purchase_Frequency', 'Time_Between_Purchases']])
    Button(root, text="Display Pairplot of Selected Variables", command=lambda: display_plot(fig6, canvas_frame)).pack()

    # 7. Scatter Plot: Lifetime Value vs Average Order Value
    fig7 = plt.Figure(figsize=(10, 6))
    sns.scatterplot(x='Lifetime_Value', y='Average_Order_Value', data=df, hue='Region', palette='Set2', ax=fig7.add_subplot(111))
    Button(root, text="Display Lifetime Value vs Average Order Value", command=lambda: display_plot(fig7, canvas_frame)).pack()

    # 8. Barplot: Retention Strategy Count
    fig8 = plt.Figure(figsize=(10, 6))
    sns.barplot(x=df['Retention_Strategy'].value_counts().index, y=df['Retention_Strategy'].value_counts().values, palette='Set3', ax=fig8.add_subplot(111))
    Button(root, text="Display Retention Strategy Count", command=lambda: display_plot(fig8, canvas_frame)).pack()

    # 9. Line Plot: Average Order Value over Time (by Launch Date)
    df['Launch_Date'] = pd.to_datetime(df['Launch_Date'])
    fig9 = plt.Figure(figsize=(10, 6))
    sns.lineplot(x='Launch_Date', y='Average_Order_Value', data=df, marker='o', ax=fig9.add_subplot(111))
    Button(root, text="Display Average Order Value over Time", command=lambda: display_plot(fig9, canvas_frame)).pack()

    # 10. Histogram: Distribution of Lifetime Value
    fig10 = plt.Figure(figsize=(10, 6))
    sns.histplot(df['Lifetime_Value'], bins=30, color='skyblue', kde=True, ax=fig10.add_subplot(111))
    Button(root, text="Display Lifetime Value Distribution", command=lambda: display_plot(fig10, canvas_frame)).pack()

    # 11. Boxplot: Lifetime Value by Season
    fig11 = plt.Figure(figsize=(10, 6))
    sns.boxplot(x='Season', y='Lifetime_Value', data=df, palette='coolwarm', ax=fig11.add_subplot(111))
    Button(root, text="Display Lifetime Value by Season", command=lambda: display_plot(fig11, canvas_frame)).pack()

    # 12. Barplot: Average Time Between Purchases by Product Category
    fig12 = plt.Figure(figsize=(10, 6))
    sns.barplot(x='Most_Frequent_Category', y='Time_Between_Purchases', data=df, palette='muted', ax=fig12.add_subplot(111))
    Button(root, text="Display Time Between Purchases by Product Category", command=lambda: display_plot(fig12, canvas_frame)).pack()

    # 13. Pie Chart: Distribution of Customer Retention Strategies
    fig13 = plt.Figure(figsize=(8, 8))
    retention_counts = df['Retention_Strategy'].value_counts()
    retention_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'), ax=fig13.add_subplot(111))
    Button(root, text="Display Customer Retention Strategies", command=lambda: display_plot(fig13, canvas_frame)).pack()

    # 14. Line Plot: Cumulative Lifetime Value by Product
    df_grouped = df.groupby('Product_ID')['Lifetime_Value'].sum()
    fig14 = plt.Figure(figsize=(10, 6))
    sns.lineplot(x=df_grouped.index, y=df_grouped.values, color='orange', marker='o', ax=fig14.add_subplot(111))
    Button(root, text="Display Cumulative Lifetime Value by Product", command=lambda: display_plot(fig14, canvas_frame)).pack()

    # 15. FacetGrid: Time Between Purchases by Region (with scatter plot)
    fig15 = plt.Figure(figsize=(10, 6))
    g = sns.FacetGrid(df, col="Region", height=6, aspect=1.5)
    g.map(sns.scatterplot, 'Lifetime_Value', 'Time_Between_Purchases', alpha=0.7)
    g.set_axis_labels('Lifetime Value (USD)', 'Time Between Purchases (days)')
    g.set_titles("{col_name}")
    Button(root, text="Display Time Between Purchases by Region", command=lambda: display_plot(fig15, canvas_frame)).pack()

    # Start the Tkinter loop
    root.mainloop()

# Function to display each plot on the canvas
def display_plot(fig, canvas_frame):
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.get_tk_widget().pack(fill='both', expand=True)
    canvas.draw()

# Run the function to create and display the plots
create_plots()
