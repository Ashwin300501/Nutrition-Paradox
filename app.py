import streamlit as st
import sqlite3
import pandas as pd

st.title("Nutrition Paradox - SQL queries")

conn=sqlite3.connect("nutrition_paradox.db")

def st_run_query(query):
    return st.dataframe(pd.read_sql_query(query,conn),hide_index=True)

#obesity queries
with st.expander("Obesity table queries"):
    #1. Top 5 regions with the highest average obesity levels in the most recent year(2022)
    st.subheader("Top 5 regions with the highest average obesity levels in the most recent year(2022) ")
    query1="""
        SELECT Region, AVG(Mean_Estimate) As avg_obesity
        FROM obesity
        WHERE Year = 2022
        GROUP BY Region
        ORDER BY avg_obesity DESC
        LIMIT 5
    """
    st_run_query(query1)

    #2. Top 5 countries with highest obesity estimates
    st.subheader("Top 5 countries with highest obesity estimates")
    query2="""
        SELECT Country, MAX(Mean_Estimate) AS max_obesity
        FROM obesity
        GROUP BY Country
        ORDER BY max_obesity DESC
        LIMIT 5
    """
    st_run_query(query2)

    #3. Obesity trend in India over the years(Mean_estimate)
    st.subheader("Obesity trend in India over the years")
    query3="""
        SELECT Year, AVG(Mean_Estimate) AS avg_obesity
        FROM obesity
        WHERE Country = 'India'
        GROUP BY Year
        ORDER BY Year
    """
    st_run_query(query3)

    #4. Average Obesity by gender
    st.subheader("Average obesity by gender")
    query4="""
        SELECT Gender, AVG(Mean_Estimate) AS avg_obesity
        FROM obesity
        GROUP BY Gender
    """
    st_run_query(query4)

    #5. Country count by obesity level category and age_group
    st.subheader("5. Country count by obesity level and age group")
    query5 = """
        SELECT obesity_level, age_group, COUNT(DISTINCT Country) AS country_count
        FROM obesity
        GROUP BY obesity_level, age_group;
    """
    st_run_query(query5)

    #6. Top 5 countries least reliable countries(with highest CI_Width) and Top 5 most consistent countries (smallest average CI_Width)
    st.subheader("6. Countries with most/least CI width (consistency)")
    query6a = """
        SELECT Country, AVG(CI_Width) AS avg_ci
        FROM obesity
        GROUP BY Country
        ORDER BY avg_ci DESC
        LIMIT 5;
    """
    query6b = """
        SELECT Country, AVG(CI_Width) AS avg_ci
        FROM obesity
        GROUP BY Country
        ORDER BY avg_ci ASC
        LIMIT 5;
    """
    st.markdown("**Top 5 Most Inconsistent Countries (High CI Width):**")
    st_run_query(query6a)

    st.markdown("**Top 5 Most Consistent Countries (Low CI Width):**")
    st_run_query(query6b)

    #7.Average obesity by age group
    st.subheader("Average obesity by age group")
    query7="""
    SELECT age_group, AVG(Mean_Estimate) AS avg_obesity
    FROM obesity
    GROUP BY age_group
    """
    st_run_query(query7)

    #8. Top 10 Countries with consistent low obesity (low average + low CI)over the years
    st.subheader("8. Consistently low obesity countries")
    query8 = """
        SELECT Country, AVG(Mean_Estimate) AS avg_obesity, AVG(CI_Width) AS avg_ci
        FROM obesity
        GROUP BY Country
        HAVING avg_obesity < 10 AND avg_ci < 2
        ORDER BY avg_obesity ASC
        LIMIT 10;
    """
    st_run_query(query8)

    #9. Countries where female obesity exceeds male by large margin (same year)
    st.subheader("9. Female obesity significantly > Male")
    query9 = """
    SELECT f.Country, f.Year, f.Mean_Estimate AS Female_Estimate, 
           m.Mean_Estimate AS Male_Estimate, 
           (f.Mean_Estimate - m.Mean_Estimate) AS Difference
    FROM obesity f
    JOIN obesity m
    ON f.Country = m.Country AND f.Year = m.Year AND f.age_group = m.age_group
    WHERE f.Gender = 'Female' AND m.Gender = 'Male'
    AND (f.Mean_Estimate - m.Mean_Estimate) > 25
    ORDER BY Difference DESC;
    """
    st_run_query(query9)

    # 10. Global average obesity percentage per year
    st.subheader("10. Global average obesity percentage per year")
    query10 = """
        SELECT Year, AVG(Mean_Estimate) AS global_avg_obesity
        FROM obesity
        GROUP BY Year
        ORDER BY Year;
    """
    st_run_query(query10)


# malnutrition queries
with st.expander("Malnutrition table queries"):
    # 1. Avg. malnutrition by age group
    st.subheader("1. Average Malnutrition by Age Group")
    query1 = """
        SELECT age_group, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        GROUP BY age_group
    """
    st_run_query(query1)

    # 2. Top 5 countries with highest malnutrition
    st.subheader("2. Top 5 Countries with Highest Malnutrition (Mean_Estimate)")
    query2 = """
        SELECT Country, MAX(Mean_Estimate) AS max_malnutrition
        FROM malnutrition
        GROUP BY Country
        ORDER BY max_malnutrition DESC
        LIMIT 5
    """
    st_run_query(query2)

    # 3. Malnutrition trend in African region over the years
    st.subheader("3. Malnutrition Trend in African Region Over the Years")
    query3 = """
        SELECT Year, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        WHERE Region = 'Africa'
        GROUP BY Year
        ORDER BY Year
    """
    st_run_query(query3)

    # 4. Gender-based average malnutrition
    st.subheader("4. Gender-based Average Malnutrition")
    query4 = """
        SELECT Gender, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        GROUP BY Gender
    """
    st_run_query(query4)

    # 5. Malnutrition level-wise (average CI_Width by age group)
    st.subheader("5. Average CI_Width by Malnutrition Level and Age Group")
    query5 = """
        SELECT malnutrition_level, age_group, AVG(CI_Width) AS avg_ci
        FROM malnutrition
        GROUP BY malnutrition_level, age_group
    """
    st_run_query(query5)

    # 6. Yearly malnutrition change in India, Nigeria, Brazil
    st.subheader("6. Yearly Malnutrition Trend (India, Nigeria, Brazil)")
    query6 = """
        SELECT Country, Year, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        WHERE Country IN ('India', 'Nigeria', 'Brazil')
        GROUP BY Country, Year
        ORDER BY Country, Year
    """
    st_run_query(query6)

    # 7. Regions with lowest malnutrition averages
    st.subheader("7. Regions with Lowest Malnutrition Averages")
    query7 = """
        SELECT Region, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition
        GROUP BY Region
        ORDER BY avg_malnutrition ASC
        LIMIT 5
    """
    st_run_query(query7)

    # 8. Countries with increasing malnutrition
    st.subheader("8. Countries with Increasing Malnutrition Over Time")
    query8 = """
        SELECT Country, MAX(Mean_Estimate) - MIN(Mean_Estimate) AS increase
        FROM malnutrition
        GROUP BY Country
        HAVING increase > 0
        ORDER BY increase DESC
        LIMIT 10
    """
    st_run_query(query8)

    # 9. Min/Max malnutrition levels year-wise comparison
    st.subheader("9. Min and Max Malnutrition Levels per Year")
    query9 = """
        SELECT Year,
               MIN(Mean_Estimate) AS min_malnutrition,
               MAX(Mean_Estimate) AS max_malnutrition
        FROM malnutrition
        GROUP BY Year
        ORDER BY Year
    """
    st_run_query(query9)

    # 10. High CI_Width flags for monitoring
    st.subheader("10. Records with High CI_Width (Above 5) — For Monitoring")
    query10 = """
        SELECT Country, Year, Gender, age_group, Mean_Estimate, CI_Width
        FROM malnutrition
        WHERE CI_Width > 5
        ORDER BY CI_Width DESC
        LIMIT 10
    """
    st_run_query(query10)


# combined obesity & malnutrition queries
with st.expander("Combined Obesity and Malnutrition Queries"):
    # 1. Obesity vs malnutrition comparison by country (any 5 countries)
    st.subheader("1. Obesity vs Malnutrition Comparison (5 Sample Countries)")
    query1 = """
        SELECT o.Country,
               ROUND(AVG(o.Mean_Estimate), 2) AS avg_obesity,
               ROUND(AVG(m.Mean_Estimate), 2) AS avg_malnutrition
        FROM obesity o
        JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year
        WHERE o.Country IN ('India', 'USA', 'Brazil', 'Nigeria', 'Japan')
        GROUP BY o.Country
    """
    st_run_query(query1)

    # 2. Gender-based disparity in both obesity and malnutrition
    st.subheader("2. Gender-based Disparity in Obesity and Malnutrition")
    query2 = """
        SELECT o.Gender,
               ROUND(AVG(o.Mean_Estimate), 2) AS avg_obesity,
               ROUND(AVG(m.Mean_Estimate), 2) AS avg_malnutrition
        FROM obesity o
        JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year AND o.Gender = m.Gender
        GROUP BY o.Gender
    """
    st_run_query(query2)

    # 3. Region-wise avg estimates side-by-side (Africa and America)
    st.subheader("3. Region-wise Averages: Obesity vs Malnutrition (Africa & America)")
    query3 = """
        SELECT o.Region,
               ROUND(AVG(o.Mean_Estimate), 2) AS avg_obesity,
               ROUND(AVG(m.Mean_Estimate), 2) AS avg_malnutrition
        FROM obesity o
        JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year
        WHERE o.Region IN ('Africa', 'Americas')
        GROUP BY o.Region
    """
    st_run_query(query3)

    # 4. Countries with obesity up & malnutrition down
    st.subheader("4. Countries with Rising Obesity and Declining Malnutrition")
    query4 = """
        SELECT o.Country,
               MAX(o.Mean_Estimate) - MIN(o.Mean_Estimate) AS obesity_increase,
               MIN(m.Mean_Estimate) - MAX(m.Mean_Estimate) AS malnutrition_decrease
        FROM obesity o
        JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year
        GROUP BY o.Country
        HAVING obesity_increase > 0 AND malnutrition_decrease > 0
        ORDER BY obesity_increase DESC
        LIMIT 10
    """
    st_run_query(query4)

    # 5. Age-wise trend analysis
    st.subheader("5. Age-wise Trend Analysis: Obesity vs Malnutrition")
    query5 = """
        SELECT o.age_group,
               ROUND(AVG(o.Mean_Estimate), 2) AS avg_obesity,
               ROUND(AVG(m.Mean_Estimate), 2) AS avg_malnutrition
        FROM obesity o
        JOIN malnutrition m ON o.Country = m.Country AND o.Year = m.Year AND o.age_group = m.age_group
        GROUP BY o.age_group
    """
    st_run_query(query5)

conn.close()