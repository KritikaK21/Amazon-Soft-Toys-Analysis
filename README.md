# Amazon Soft Toys Analysis 🧸📊

## Overview 🌟
This project focuses on analyzing Amazon's soft toys data to uncover insights and trends that help us understand factors influencing product ratings, prices, and user preferences. The analysis is performed through data cleaning, exploratory data analysis (EDA), and implementing a recommendation system.

## Features 🔍
- Data Cleaning: Preprocesses raw data by handling missing values, converting data types, and removing outliers 🧹.

- Exploratory Data Analysis (EDA): Visualizes key patterns and distributions in the data such as price vs ratings, and reviews 📈.

- Recommendation System: Uses a simple algorithm to recommend the highest-rated soft toys based on user ratings ⭐.

- Data Visualization: Graphical plots to represent the data's characteristics such as price distribution, rating distribution, etc. 📊.

## Tools & Libraries 🛠️
- Pandas: For data manipulation and cleaning 🧰.

- Numpy: For numerical operations ➗.

- Matplotlib / Seaborn: For data visualization 🎨.

- Sklearn: For simple machine learning algorithms 🤖.

## Project Structure 📁

- **data_cleaning.py:** Contains code for cleaning the raw dataset 🧹.

- **eda.py:** Generates visualizations and explores the dataset 📊.

- **recommendation.py:** Implements the recommendation system to suggest the best soft toys based on user preferences 💡.

- **requirements.txt:** Lists all the required libraries and dependencies to run the project 📑.

## Installation & Setup ⚙️
1. **Clone the repository:**
```
git clone https://github.com/yourusername/amazon-soft-toys-analysis.git
```
2. **Navigate to the project directory:**
```
cd amazon-soft-toys-analysis
```
3. **Install dependencies:**
```
pip install -r requirements.txt
```
## How to Run ▶️
1. **Data Cleaning:**
```
python data_cleaning.py
```
- This script will preprocess the data by handling missing values, converting columns to appropriate data types, and cleaning up the dataset 🧹.

2. **Exploratory Data Analysis (EDA):**
```
python eda.py
```
- Generates visualizations of price distribution, rating distribution, and more 📈.

3. **Recommendation System:**
```
python recommendation.py
```
- This script recommends the top-rated soft toys based on customer ratings and reviews ⭐.

## Example Output 📝
- **Price Distribution Chart:** A bar chart displaying how soft toy prices vary 📉.

- **Rating Distribution:** A graph showing the distribution of ratings given by customers ⭐.

- **Top-Rated Products:** A list of the highest-rated soft toys, along with their key details such as price and rating 🏆.

## Example Query 💬:
- After running the scripts, the output will display the highest-rated soft toys, the price distribution, and visualizations that help understand customer preferences.

## Dependencies 📚
- **pandas:** For data manipulation and analysis 🧠.

- **numpy:** For numerical computations ➗.

- **matplotlib:** For creating static, animated, and interactive visualizations 🎨.

- **seaborn:** For data visualization based on Matplotlib 📊.

- **scikit-learn:** For any machine learning algorithms 🤖.

- **openpyxl:** For reading Excel files (if applicable) 📄.

## License 📜
This project is licensed under the MIT License.
