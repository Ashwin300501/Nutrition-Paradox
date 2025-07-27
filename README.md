# 🥗 Nutrition Paradox SQL Explorer

This project analyzes the global **Nutrition Paradox** — the coexistence of obesity and malnutrition — using WHO datasets. It includes data processing, a relational database, and an interactive Streamlit application to explore insights using SQL queries.

---

## 📁 Project Structure

```
nutrition-paradox/
│
├── nutrition_paradox.ipynb       # Jupyter notebook: data collection, cleaning, and analysis
├── nutrition_paradox.db          # SQLite DB storing cleaned obesity and malnutrition data
├── app.py                        # Streamlit app for interactive SQL query analysis
├── README.md                     # Project documentation (this file)
└── requirements.txt              # Required Python packages
```

---

## 🌐 Datasets Used

Sourced from the [World Health Organization's GHO API](https://www.who.int/data/gho/info/athena-api):

- Adult Obesity: `NCD_BMI_30C`
- Child Obesity: `NCD_BMI_PLUS2C`
- Adult Malnutrition: `NCD_BMI_18C`
- Child Malnutrition: `NCD_BMI_MINUS2C`

---

## 🧠 Key Features

### ✅ Jupyter Notebook (`nutrition_paradox.ipynb`)
- Downloads and combines obesity & malnutrition datasets
- Transforms country codes and standardizes formats
- Adds calculated columns like:
  - `CI_Width` (Confidence Interval range)
  - `obesity_level` & `malnutrition_level` (based on thresholds)
- Outputs clean data into a SQLite database (`nutrition_paradox.db`)
- Performs EDA using seaborn/matplotlib

### ✅ Streamlit App (`app.py`)
**🔍 Query 1: Obesity Insights**
- Regional and country trends
- Gender- and age-based analysis
- Confidence interval (CI) reliability
- Consistent low-obesity countries
- Year-wise global trends

**🔍 Query 2: Malnutrition Insights**
- Highest/lowest countries by mean estimates
- Regional/gender/age group breakdowns
- CI-based monitoring
- Time trends for India, Nigeria, Brazil
- Increasing malnutrition detection

**🔍 Query 3: Combined Analysis**
- Country-level obesity vs malnutrition
- Gender & region comparisons
- Age-group cross trends
- Countries with obesity up, malnutrition down

Each query group is collapsible using `st.expander`.

---

## 💡 Visual Insights Powered by SQL

Over 25 unique SQL-powered insights:
- Top regions & countries by obesity/malnutrition
- Gender disparities in both conditions
- Regional comparisons (Africa vs Americas)
- Cross-tabulations: Age × Gender, Region × Time
- Anomalies via CI_Width and consistency flags

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/your-username/nutrition-paradox.git
cd nutrition-paradox
```

### 2. Set Up Environment

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit App

```bash
streamlit run app.py
```

Make sure `nutrition_paradox.db` is present in the same directory.

---

## 🧾 Requirements

- Python 3.8+
- Libraries:
  - `streamlit`
  - `sqlite3`
  - `pandas`
  - `pycountry`
  - `matplotlib`, `seaborn` (for EDA)
  - `requests`, `json` (for API calls)

---

## 🧠 Potential Enhancements

- 📊 Power BI dashboard for more interactivity
- 📍 Geo-mapping visuals (e.g., via Plotly or Folium)
- 📈 Charts within Streamlit (e.g., using Altair or Plotly Express)
- 🔁 Scheduled auto-refresh from WHO APIs

---

## 📘 License

This project is for educational and research purposes. Data © WHO.