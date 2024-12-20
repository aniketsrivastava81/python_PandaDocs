# README for Pandas Data Exercises

## Objective

The objective of these exercises is to practice and enhance skills in data manipulation, cleaning, visualization, and analysis using Pandas and other Python libraries. These exercises cover a variety of tasks, such as removing duplicates, cleaning columns, aggregating data, visualizing trends, and merging datasets. The exercises aim to improve proficiency in handling different types of data and performing operations like filtering, grouping, and applying functions across datasets.

## Tech Stack

- **Python**: The main programming language used for data manipulation and analysis.
- **Pandas**: The primary library for data structures and data analysis tools.
- **Matplotlib/Seaborn**: Used for data visualization, including plotting various charts.
- **NumPy**: A supporting library for array manipulation.

## Steps to Reproduce

1. **Set Up Environment**:
    Install Python and the necessary libraries using:
    ```bash
    pip install pandas matplotlib seaborn numpy
    ```

2. **Download the Files**:
    Ensure that you have the following data files in your working directory:
    - `Customer Call List.xlsx`
    - `world_population.csv`
    - `Flavors.csv`
    - `LOTR.csv`
    - `LOTR 2.csv`
    - `Ice Cream Ratings.csv`

3. **Load the Data**:
    Import the datasets using `pd.read_csv()` for CSV files and `pd.read_excel()` for Excel files:
    ```python
    df = pd.read_csv('filename.csv')  # for CSV files
    df = pd.read_excel('filename.xlsx')  # for Excel files
    ```

4. **Execute the Code**:
    Follow the steps in each file to complete data processing tasks. These tasks include cleaning, filtering, grouping, and visualizing data.

5. **Visualizations**:
    For data visualization, use `matplotlib.pyplot` or `seaborn` for different types of plots like line charts, bar plots, scatter plots, etc.

## File List and Descriptions

| File Name                         | Description                                                                 | Key Operations                                                   |
|-----------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------|
| Customer Call List.xlsx           | Performs data cleaning and removes unnecessary columns, duplicates         | Data cleaning, handling null values, column dropping            |
| world_population.csv              | Analyzes global population data and produces summary statistics             | Aggregation, correlation, grouping, visualization               |
| Flavors.csv                       | Analyzes and groups flavor ratings by base flavor                           | Grouping, aggregation, statistical summary                      |
| LOTR.csv and LOTR 2.csv           | Merges two datasets on common columns and explores join types              | Merge, join, concatenation                                       |
| Ice Cream Ratings.csv             | Visualizes ice cream ratings data with multiple plot types                  | Plotting, trend analysis, box plots, pie charts                 |
| Pandas Series and Dataframes.ipynb| Demonstrates creating and manipulating Pandas Series and DataFrames         | Series and DataFrame creation and manipulation                   |
| Merge, Join, and Concatenate in Pandas.ipynb | Merges and joins data using different types of joins              | Merge, join, concatenate operations                              |

## File List and Descriptions

| File Name                         | Description                                                                 | Key Operations                                                   |
|-----------------------------------|-----------------------------------------------------------------------------|------------------------------------------------------------------|
| File 1 - Pandas Data Cleaning Exercise | This file demonstrates cleaning and preprocessing customer data from an Excel file. | - Remove duplicates<br>- Drop unnecessary columns<br>- Clean and format phone numbers<br>- Split address into components<br>- Replace/modify 'Do_Not_Contact' column<br>- Drop rows with missing phone numbers or contacts |
| File 2 - Data Extrapolation Exercise | This file works with a world population dataset to explore and visualize global population trends. | - Summarize data with describe() and info()<br>- Handle missing values<br>- Create visualizations (heatmap, box plot)<br>- Group data by continent and analyze population changes over time |
| File 3 - Order and Filter Exercise | This file filters and sorts population data, focusing on specific countries and continents. | - Filter by rank, specific countries<br>- Use .isin() and .str.contains() for advanced filtering<br>- Apply sorting and filtering by country and continent |
| File 4 - Groupby and Aggregating Exercise | This file demonstrates grouping and aggregation techniques using a flavor ratings dataset. | - Group data by 'Base Flavor'<br>- Aggregate ratings (mean, sum, count)<br>- Use .agg() for multiple statistics<br>- Describe grouped data |
| File 5 - Indexing Exercise          | This file demonstrates indexing techniques and how to manipulate indices in a dataset. | - Set and reset index with set_index() and reset_index()<br>- Index using both .loc[] and .iloc[]<br>- Perform sorting on multi-index columns |
| File 6 - Merge, Join, and Concatenate | This file demonstrates how to merge, join, and concatenate two datasets. | - Perform different types of joins (inner, outer, left, right, cross)<br>- Use join() and concat() for combining dataframes<br>- Merge based on multiple keys |
| File 7 - Pandas Series and DataFrames | This file shows how to create and manipulate Pandas Series and DataFrames with basic operations. | - Create Series with custom indices<br>- Perform arithmetic on Series<br>- Create DataFrames from lists and dictionaries<br>- Manipulate DataFrame indices |
| File 8 - Merge, Join, and Concatenate in Pandas | Another demonstration of merge and join operations using merge(), join(), and concat(). | - Merge two datasets using multiple join types<br>- Concatenate along different axes<br>- Demonstrate cross join |
| File 9 - Data Visualization        | This file demonstrates various ways to visualize ice cream rating data using Pandas and Matplotlib. | - Line plot, bar plot, scatter plot, histogram<br>- Box plot and pie chart<br>- Set figure styles and visualize trends |

## Additional Information

These exercises aim to provide hands-on experience with data processing tasks such as cleaning, transforming, and visualizing data, which are crucial skills for data science and analysis. The techniques used in these files can be applied to real-world datasets for deeper insights into data.
