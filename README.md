# 🍽️ Zomato Restaurant Analysis

An exploratory data analysis project using Python and Power BI to uncover insights into restaurant listings, ratings, cuisines, locations, and online ordering.

## 📌 Project Overview

This project analyzes Zomato restaurant data to understand restaurant distribution, customer ratings, cuisine categories, and online ordering availability.

## 🛠️ Tools & Technologies

- **Python** — Data cleaning and analysis
- **Pandas** — Data manipulation
- **Matplotlib & Seaborn** — Data visualization
- **Power BI** — Interactive dashboard development

## 📂 Project Structure

```text
Zomato-Restaurant-Analysis/
├── src/
│   └── analyze_zomato.py
├── outputs/
│   ├── data_quality_report.csv
│   ├── top_10_locations.png
│   ├── rating_distribution.png
│   ├── top_10_cuisines.png
│   ├── online_ordering.png
│   ├── rating_by_online_order.png
│   ├── top_10_restaurant_types.png
│   └── votes_vs_rating.png
└── README.md
```

## 🔍 Project Workflow

1. Loaded the Zomato restaurant dataset using Pandas.
2. Cleaned column names and whitespace.
3. Converted ratings, votes, and approximate cost into numeric formats where possible.
4. Examined missing values and generated a data quality report.
5. Explored restaurant locations, cuisines, ratings, and online ordering.
6. Created visualizations using Matplotlib and Seaborn.
7. Built a Power BI dashboard to present key metrics and comparisons.

## 📊 Visualizations

The analysis includes:

- Top 10 restaurant locations
- Restaurant rating distribution
- Top 10 cuisine categories
- Online ordering availability
- Ratings by online ordering availability
- Top restaurant types
- Votes versus restaurant ratings

## 📈 Key Findings

The initial dataset contains **51,717 rows and 17 columns**. The average numeric restaurant rating after cleaning is approximately **3.70 out of 5**.

Other findings can be added after reviewing the final charts and dashboard.

## 💻 How to Run

1. Install Python.
2. Install the required libraries:

   ```bash
   pip install pandas matplotlib seaborn
   ```

3. Update the dataset path in `src/analyze_zomato.py` to point to your local CSV file.
4. Run the script:

   ```bash
   python src/analyze_zomato.py
   ```

## 📁 Project Outputs

The `outputs` folder contains the cleaned dataset, data quality report, and generated chart images.

## 👩‍💻 Author

Created as a data analysis portfolio project using Python and Power BI.
