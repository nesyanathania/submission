# E-Commerce Data Analysis Dashboard

This project aims to analyze an e-commerce dataset and create an interactive dashboard using **Streamlit**. The dashboard provides insights into two main areas of analysis:

1. **Correlation between Product Photo Quantities and Review Scores**: This analysis examines if there is any correlation between the number of product photos and customer review scores.
2. **Top Product Categories by Sales and Revenue**: This analysis identifies the product categories with the highest sales and revenue.

## Project Structure

The project directory is organized as follows:

- `dashboard/`
  - `data1_project.csv`: The dataset containing product photo quantities and review scores.
  - `data2_project.csv`: The dataset for sales and revenue analysis per product category.
  - `dashboard.py`: The Python script that runs the Streamlit dashboard.
- `notebook.ipynb`: The Jupyter/Colab notebook for data analysis.
- `requirements.txt`: A file listing all the Python libraries required to run the project.
- `README.md`: This file, providing an overview of the project.
- `url.txt`: A file to store the link to the deployed dashboard (if applicable).

## Analysis Overview

### 1. Correlation between Product Photo Quantities and Review Scores

This part of the analysis uses a scatter plot to visualize the relationship between:
- **X-axis**: The number of product photos (`product_photos_qty`).
- **Y-axis**: The review scores (`review_score`).

### 2. Top Product Categories by Sales and Revenue

This part of the analysis uses a bar chart and line plot to display:
- **Top 5 Product Categories**: Based on total sales (`order_id` count) and total revenue (`price` sum).

The chart visualizes both the total revenue and total number of products sold in the top 5 categories.

## How to Run the Dashboard

To run the dashboard locally, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/username/repository-name.git
    ```

2. Navigate into the project folder:
    ```bash
    cd repository-name
    ```

3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit dashboard:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

5. The dashboard will automatically open in your default web browser. If not, navigate to `http://localhost:8501/` manually.

## Libraries Used

This project utilizes the following libraries:

- `pandas`: For data manipulation and analysis.
- `streamlit`: For creating the interactive dashboard.
- `matplotlib`: For plotting graphs.
- `seaborn`: For statistical data visualization.
- `numpy`: For numerical operations.
- `scipy.stats`: For performing statistical analysis.

## Dataset Information

The datasets used in this project are:

- **data1_project.csv**: Contains the columns `product_photos_qty` and `review_score` used to analyze the correlation between the number of product photos and review scores.
- **data2_project.csv**: Contains the columns `order_id` and `price`, used to analyze product sales and revenue per category.

## Example of Dashboard Visuals

- **Scatter Plot**: Visualizing the correlation between product photo quantities and review scores.
- **Bar & Line Plot**: Displaying the top 5 product categories by sales and revenue.

## Requirements

The required libraries are listed in the `requirements.txt` file. You can install them using:
```bash
pip install -r requirements.txt
