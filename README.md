# Olympic Medal Performance Analysis (1896-2016)

Statistical analysis of 120 years of Olympic Games data examining medal distribution patterns, athlete demographics, and competitive trends across 230+ countries and 66 sports.

## 📊 Project Overview

This project analyzes historical Olympic Games data to uncover insights into:
- Medal distribution patterns across countries and time periods
- Evolution of athlete participation (especially gender representation)
- Physical characteristics of medal winners vs non-winners
- Sport-specific trends and patterns
- Summer vs Winter Olympics comparisons

## 🎯 Key Findings

### Dominant Nations
- **USA leads** with 5,637 total medals across Olympic history
- Top 5 countries (USA, URS, GER, GBR, FRA) account for significant portion of all medals
- Traditional powerhouses maintain consistency over decades

### Participation Evolution
- Dramatic growth: **176 athletes (1896) → 11,179 athletes (2016)** (63.5x increase)
- Female participation: **0% → 45.5%** by 2016
- Participating countries increased from handful to **207 nations**

### Athlete Characteristics
- Average age of medal winners: **~26 years**
- Physical characteristics vary significantly by sport
- Height and weight show positive correlation among medal winners

### Sport Trends
- **Athletics** (Track & Field) produces the most medals
- Swimming and Gymnastics are high-medal sports
- Winter Olympics have fewer participants but high competitiveness

## 📁 Project Structure

```
olympic-medal-performance-analysis/
├── olympic_analysis.py           # Main Python analysis script
├── olympics.ipynb                # Jupyter notebook version
├── olympics_medal_winners.csv    # Medal winners dataset (39,783 records)
├── olympics_summary.csv          # Summary statistics
├── olympics_analysis_main.png    # 9-panel visualization dashboard
├── olympics_top5_trends.png      # Top 5 countries medal trends
└── README.md                     # This file
```

## 🛠️ Technologies Used

- **Python 3.x**
- **pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization

## 📥 Data Source

**Dataset:** 120 years of Olympic history: athletes and results  
**Source:** [Kaggle](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)  
**Records:** ~271,116 athlete-event records  
**Time Period:** 1896 to 2016  
**Coverage:** Summer and Winter Olympics

### Dataset Features:
- Athlete ID, Name, Sex, Age, Height, Weight
- Team, NOC (National Olympic Committee)
- Year, Season, City (host city)
- Sport, Event, Medal (Gold/Silver/Bronze/NA)

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Download the Dataset

1. Visit the [Kaggle dataset page](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)
2. Download `athlete_events.csv`
3. Place it in the project directory

### Run the Analysis

**Option 1: Run the Python script**
```bash
python olympic_analysis.py
```

**Option 2: Run the Jupyter notebook**
```bash
jupyter notebook olympics.ipynb
```

## 📈 Visualizations

The analysis generates comprehensive visualizations including:

1. **Top 15 Countries by Total Medals** - All-time medal rankings
2. **Medal Distribution** - Gold, Silver, Bronze breakdown
3. **Athlete Participation Over Time** - Historical growth trends
4. **Gender Participation Trends** - Evolution of female athletes
5. **Top 10 Sports by Medal Count** - Most competitive sports
6. **Medals by Decade** - Temporal distribution
7. **Age Distribution of Medal Winners** - Demographic analysis
8. **Summer vs Winter Olympics** - Comparative analysis
9. **Height vs Weight of Medal Winners** - Physical characteristics
10. **Medal Trends for Top 5 Countries** - Time-series analysis

## 📊 Analysis Highlights

### Research Questions Explored

1. ✅ Which countries have been most successful in Olympic history?
2. ✅ How has athlete participation evolved over time?
3. ✅ What are the physical characteristics of medal winners?
4. ✅ Which sports produce the most medals?
5. ✅ How do Summer and Winter Olympics differ?
6. ✅ What are the age patterns across different sports?

### Statistical Methods

- Descriptive statistics and aggregations
- Time-series analysis
- Comparative analysis (medal winners vs non-winners)
- Demographic pattern analysis
- Physical characteristics correlation

## 🔍 Key Statistics

- **Total Athletes Analyzed:** 135,571 unique athletes
- **Countries Represented:** 230 NOCs
- **Sports Included:** 66 different sports
- **Total Events:** 765 competitive events
- **Total Medals Awarded:** 39,783
- **Time Span:** 124 years (1896-2016)

## 📝 Data Cleaning & Processing

The analysis includes comprehensive data cleaning:
- Handling missing values (Age: 3.5%, Height: 22%, Weight: 23%)
- Creating derived features (Medal_Winner, Decade, BMI, Age_Group)
- Removing duplicates (1,385 duplicate rows)
- Type conversions and categorical encoding

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- **Data Analysis:** Exploratory data analysis, statistical summarization
- **Data Visualization:** Multi-panel dashboards, trend analysis
- **Python Programming:** pandas, NumPy, matplotlib, seaborn
- **Statistical Thinking:** Hypothesis generation, pattern recognition
- **Data Communication:** Creating insights from large datasets

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements!

## 📧 Contact

**Neil Mahajan**  
[Your LinkedIn] | [Your Email] | [Your Portfolio]

---

*Analyzing 120 years of Olympic excellence through data science*
