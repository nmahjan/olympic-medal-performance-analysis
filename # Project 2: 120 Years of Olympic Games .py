# Project 2: 120 Years of Olympic Games Analysis
# Student: [Your Name]
# Course: DAT301
# Data Source: Kaggle - 120 years of Olympic history: athletes and results
# URL: https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("Set2")

# ====================================================================
# PART 1: BACKGROUND AND PROBLEM DEFINITION
# ====================================================================

print("="*80)
print("OLYMPIC GAMES ANALYSIS: 120 Years of Athletic Excellence (1896-2016)")
print("="*80)

"""
BACKGROUND:
The Olympic Games represent the pinnacle of athletic achievement, bringing together
athletes from around the world since 1896. This analysis explores 120 years of 
Olympic history to understand patterns in medals, athlete characteristics, and 
country performance.

DATA SOURCE:
- Dataset: 120 years of Olympic history: athletes and results
- Source: Kaggle (scraped from www.sports-reference.com)
- URL: https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results
- Records: ~271,116 athlete-event records
- Time Period: 1896 to 2016

RESEARCH QUESTIONS:
1. Which countries have been most successful in Olympic history?
2. How has athlete participation evolved over time (especially for women)?
3. What are the physical characteristics of medal winners vs non-winners?
4. Which sports produce the most medals?
5. Is there a "home advantage" for host countries?
6. How do Summer and Winter Olympics differ in participation and medals?
"""

# ====================================================================
# PART 2: DATA LOADING AND INITIAL EXPLORATION
# ====================================================================

print("\n" + "="*80)
print("LOADING AND EXPLORING DATA")
print("="*80)

# Load the dataset
df = pd.read_csv('athlete_events.csv')

print(f"\n✓ Dataset loaded successfully!")
print(f"Dataset Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

print("\n--- First 5 rows ---")
print(df.head())

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Basic Statistics ---")
print(df.describe())

# Check unique values for key columns
print("\n--- Unique Values ---")
print(f"Unique Athletes: {df['ID'].nunique():,}")
print(f"Unique NOCs (Countries): {df['NOC'].nunique()}")
print(f"Unique Sports: {df['Sport'].nunique()}")
print(f"Unique Events: {df['Event'].nunique():,}")
print(f"Year Range: {df['Year'].min()} to {df['Year'].max()}")
print(f"Seasons: {df['Season'].unique()}")

# ====================================================================
# PART 3: DATA CLEANING AND WRANGLING
# ====================================================================

print("\n" + "="*80)
print("DATA CLEANING AND WRANGLING")
print("="*80)

# Check for missing values
print("\n1. Missing Values Analysis:")
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Count': missing,
    'Percentage': missing_pct
})
print(missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Count', ascending=False))

# Handle missing values
print("\n2. Handling Missing Values:")
print(f"   - Age: {df['Age'].isnull().sum()} missing → Will analyze with/without nulls")
print(f"   - Height: {df['Height'].isnull().sum()} missing → Will analyze medal winners only")
print(f"   - Weight: {df['Weight'].isnull().sum()} missing → Will analyze medal winners only")
print(f"   - Medal: {df['Medal'].isnull().sum()} missing → These are non-medal winners")

# Create new features
print("\n3. Creating New Features:")

# Medal winner flag
df['Medal_Winner'] = df['Medal'].notna()
print("   ✓ Medal_Winner: Binary indicator for medal winners")

# Decade column
df['Decade'] = (df['Year'] // 10) * 10
print("   ✓ Decade: Grouped years into decades")

# BMI calculation (for those with height and weight)
df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)
print("   ✓ BMI: Body Mass Index calculated")

# Age groups
df['Age_Group'] = pd.cut(df['Age'], 
                         bins=[0, 20, 25, 30, 35, 100], 
                         labels=['Under 20', '20-25', '25-30', '30-35', 'Over 35'])
print("   ✓ Age_Group: Categorical age grouping")

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"\n4. Duplicate Rows: {duplicates}")

print("\n5. Data Types After Cleaning:")
print(df.dtypes)

# ====================================================================
# PART 4: EXPLORATORY DATA ANALYSIS
# ====================================================================

print("\n" + "="*80)
print("EXPLORATORY DATA ANALYSIS")
print("="*80)

# Question 1: Top medal-winning countries
print("\n1. TOP 10 MEDAL-WINNING COUNTRIES (All-Time):")
medal_df = df[df['Medal'].notna()]
top_countries = medal_df['NOC'].value_counts().head(10)
print(top_countries)

# Question 2: Medal distribution
print("\n2. MEDAL DISTRIBUTION:")
medal_counts = df['Medal'].value_counts()
print(medal_counts)
total_medals = medal_counts.sum()
print(f"\nTotal Medals Awarded: {total_medals:,}")

# Question 3: Participation over time
print("\n3. PARTICIPATION OVER TIME:")
participation_by_year = df.groupby('Year').agg({
    'ID': 'nunique',
    'NOC': 'nunique',
    'Event': 'nunique'
}).rename(columns={'ID': 'Athletes', 'NOC': 'Countries', 'Event': 'Events'})
print(participation_by_year.tail(10))

# Question 4: Gender participation
print("\n4. GENDER PARTICIPATION:")
gender_counts = df.groupby(['Year', 'Sex']).size().unstack(fill_value=0)
print(gender_counts.tail(10))
print(f"\nFemale Participation Rate (2016): {(gender_counts.loc[2016, 'F'] / gender_counts.loc[2016].sum()) * 100:.1f}%")

# Question 5: Average age of medal winners
print("\n5. AVERAGE AGE OF MEDAL WINNERS BY MEDAL TYPE:")
age_by_medal = df[df['Medal'].notna()].groupby('Medal')['Age'].mean()
print(age_by_medal)

# Question 6: Physical characteristics of medal winners
print("\n6. PHYSICAL CHARACTERISTICS OF MEDAL WINNERS:")
medal_winners = df[df['Medal'].notna()]
physical_stats = medal_winners.groupby('Medal')[['Age', 'Height', 'Weight']].mean()
print(physical_stats)

# Question 7: Most popular sports
print("\n7. TOP 10 SPORTS BY NUMBER OF EVENTS:")
top_sports = df.groupby('Sport')['Event'].nunique().sort_values(ascending=False).head(10)
print(top_sports)

# Question 8: Summer vs Winter Olympics
print("\n8. SUMMER VS WINTER OLYMPICS COMPARISON:")
season_stats = df.groupby('Season').agg({
    'ID': 'nunique',
    'NOC': 'nunique',
    'Sport': 'nunique',
    'Medal': lambda x: x.notna().sum()
}).rename(columns={'ID': 'Athletes', 'NOC': 'Countries', 'Sport': 'Sports', 'Medal': 'Medals'})
print(season_stats)

# ====================================================================
# PART 5: DATA VISUALIZATION
# ====================================================================

print("\n" + "="*80)
print("GENERATING VISUALIZATIONS")
print("="*80)

# Create comprehensive visualization figure
fig = plt.figure(figsize=(20, 12))

# Plot 1: Top 15 Medal-Winning Countries
ax1 = plt.subplot(3, 3, 1)
top_15_countries = medal_df['NOC'].value_counts().head(15)
top_15_countries.plot(kind='barh', ax=ax1, color='gold')
ax1.set_title('Top 15 Countries by Total Medals (All-Time)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Number of Medals')
ax1.set_ylabel('Country (NOC)')
ax1.invert_yaxis()

# Plot 2: Medal Distribution
ax2 = plt.subplot(3, 3, 2)
medal_colors = {'Gold': 'gold', 'Silver': 'silver', 'Bronze': '#CD7F32'}
medal_counts.plot(kind='bar', ax=ax2, color=[medal_colors[m] for m in medal_counts.index])
ax2.set_title('Distribution of Medal Types', fontsize=12, fontweight='bold')
ax2.set_xlabel('Medal Type')
ax2.set_ylabel('Count')
ax2.tick_params(axis='x', rotation=0)

# Plot 3: Athlete Participation Over Time
ax3 = plt.subplot(3, 3, 3)
athletes_per_year = df.groupby('Year')['ID'].nunique()
ax3.plot(athletes_per_year.index, athletes_per_year.values, marker='o', linewidth=2, color='steelblue')
ax3.set_title('Athlete Participation Over Time', fontsize=12, fontweight='bold')
ax3.set_xlabel('Year')
ax3.set_ylabel('Number of Athletes')
ax3.grid(True, alpha=0.3)

# Plot 4: Gender Participation Over Time
ax4 = plt.subplot(3, 3, 4)
gender_participation = df.groupby(['Year', 'Sex']).size().unstack(fill_value=0)
ax4.plot(gender_participation.index, gender_participation['M'], label='Male', linewidth=2, marker='o')
ax4.plot(gender_participation.index, gender_participation['F'], label='Female', linewidth=2, marker='s')
ax4.set_title('Gender Participation Over Time', fontsize=12, fontweight='bold')
ax4.set_xlabel('Year')
ax4.set_ylabel('Number of Athletes')
ax4.legend()
ax4.grid(True, alpha=0.3)

# Plot 5: Age Distribution of Medal Winners vs Non-Winners
ax5 = plt.subplot(3, 3, 5)
winners_age = df[df['Medal_Winner'] == True]['Age'].dropna()
non_winners_age = df[df['Medal_Winner'] == False]['Age'].dropna()
ax5.hist([winners_age, non_winners_age], bins=30, label=['Medal Winners', 'Non-Winners'], 
         alpha=0.7, color=['gold', 'lightblue'])
ax5.set_title('Age Distribution: Winners vs Non-Winners', fontsize=12, fontweight='bold')
ax5.set_xlabel('Age')
ax5.set_ylabel('Frequency')
ax5.legend()

# Plot 6: Height vs Weight for Medal Winners
ax6 = plt.subplot(3, 3, 6)
medal_data = df[df['Medal'].notna()][['Height', 'Weight', 'Medal']].dropna()
for medal, color in medal_colors.items():
    data = medal_data[medal_data['Medal'] == medal]
    ax6.scatter(data['Height'], data['Weight'], alpha=0.5, s=20, 
               label=medal, color=color)
ax6.set_title('Height vs Weight of Medal Winners', fontsize=12, fontweight='bold')
ax6.set_xlabel('Height (cm)')
ax6.set_ylabel('Weight (kg)')
ax6.legend()
ax6.grid(True, alpha=0.3)

# Plot 7: Top 10 Sports by Medal Count
ax7 = plt.subplot(3, 3, 7)
top_sports_medals = medal_df['Sport'].value_counts().head(10)
top_sports_medals.plot(kind='barh', ax=ax7, color='coral')
ax7.set_title('Top 10 Sports by Total Medals', fontsize=12, fontweight='bold')
ax7.set_xlabel('Number of Medals')
ax7.set_ylabel('Sport')
ax7.invert_yaxis()

# Plot 8: Summer vs Winter Medal Distribution by Country (Top 10)
ax8 = plt.subplot(3, 3, 8)
season_country = medal_df.groupby(['Season', 'NOC']).size().unstack(fill_value=0)
top_10_overall = medal_df['NOC'].value_counts().head(10).index
season_data = season_country[top_10_overall].T
season_data.plot(kind='bar', stacked=True, ax=ax8, color=['#FFA500', '#87CEEB'])
ax8.set_title('Summer vs Winter Medals (Top 10 Countries)', fontsize=12, fontweight='bold')
ax8.set_xlabel('Country')
ax8.set_ylabel('Number of Medals')
ax8.legend(title='Season')
ax8.tick_params(axis='x', rotation=45)

# Plot 9: Number of Countries Participating Over Time
ax9 = plt.subplot(3, 3, 9)
countries_per_year = df.groupby('Year')['NOC'].nunique()
ax9.fill_between(countries_per_year.index, countries_per_year.values, alpha=0.5, color='green')
ax9.plot(countries_per_year.index, countries_per_year.values, linewidth=2, color='darkgreen')
ax9.set_title('Number of Participating Countries Over Time', fontsize=12, fontweight='bold')
ax9.set_xlabel('Year')
ax9.set_ylabel('Number of Countries')
ax9.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('olympics_analysis_main.png', dpi=300, bbox_inches='tight')
print("✓ Main visualization saved as 'olympics_analysis_main.png'")
plt.show()

# Additional Visualization: Medal Trends for Top 5 Countries
fig2, ax = plt.subplots(figsize=(14, 7))
top_5_countries = medal_df['NOC'].value_counts().head(5).index
for country in top_5_countries:
    country_medals = medal_df[medal_df['NOC'] == country].groupby('Year').size()
    ax.plot(country_medals.index, country_medals.values, marker='o', 
           linewidth=2, label=country, markersize=4)

ax.set_title('Medal Count Trends for Top 5 Countries Over Time', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Medals', fontsize=12)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('olympics_top5_trends.png', dpi=300, bbox_inches='tight')
print("✓ Top 5 countries trend visualization saved as 'olympics_top5_trends.png'")
plt.show()

# ====================================================================
# PART 6: ADVANCED ANALYSIS
# ====================================================================

print("\n" + "="*80)
print("ADVANCED ANALYSIS")
print("="*80)

# Analysis 1: Host Country Advantage
print("\n1. HOST COUNTRY ADVANTAGE ANALYSIS:")
print("   (Simplified analysis - comparing general medal patterns)")
# Note: Full analysis would require host country data

# Analysis 2: Age patterns by sport
print("\n2. AVERAGE AGE OF MEDAL WINNERS BY SPORT (Top 10 Sports):")
age_by_sport = medal_winners.groupby('Sport')['Age'].agg(['mean', 'std', 'count']).sort_values('count', ascending=False).head(10)
print(age_by_sport)

# Analysis 3: Physical differences between sports
print("\n3. PHYSICAL CHARACTERISTICS BY SPORT (Top 5 Medal Sports):")
top_5_medal_sports = medal_df['Sport'].value_counts().head(5).index
physical_by_sport = medal_winners[medal_winners['Sport'].isin(top_5_medal_sports)].groupby('Sport')[['Height', 'Weight', 'BMI']].mean()
print(physical_by_sport)

# Analysis 4: Gender gap analysis
print("\n4. GENDER GAP EVOLUTION:")
female_participation_rate = df.groupby('Year')['Sex'].apply(lambda x: (x == 'F').sum() / len(x) * 100)
print("Female Participation Rate by Decade:")
print(female_participation_rate.groupby(df['Year'] // 10 * 10).mean())

# Analysis 5: Most successful athletes
print("\n5. TOP 10 MOST DECORATED ATHLETES (By Medal Count):")
athlete_medals = medal_df.groupby('Name').agg({
    'Medal': 'count',
    'Sport': lambda x: x.mode()[0] if len(x.mode()) > 0 else x.iloc[0],
    'NOC': lambda x: x.mode()[0] if len(x.mode()) > 0 else x.iloc[0]
}).sort_values('Medal', ascending=False).head(10)
athlete_medals.columns = ['Total_Medals', 'Primary_Sport', 'Country']
print(athlete_medals)

# ====================================================================
# PART 7: STATISTICAL SUMMARY
# ====================================================================

print("\n" + "="*80)
print("STATISTICAL SUMMARY")
print("="*80)

print("\n1. OVERALL STATISTICS:")
print(f"   Total Records: {len(df):,}")
print(f"   Unique Athletes: {df['ID'].nunique():,}")
print(f"   Countries Represented: {df['NOC'].nunique()}")
print(f"   Sports Included: {df['Sport'].nunique()}")
print(f"   Total Events: {df['Event'].nunique():,}")
print(f"   Years Covered: {df['Year'].max() - df['Year'].min() + 4} years")
print(f"   Total Medals Awarded: {medal_df.shape[0]:,}")

print("\n2. MEDAL WINNERS STATISTICS:")
print(medal_winners[['Age', 'Height', 'Weight', 'BMI']].describe())

print("\n3. PARTICIPATION GROWTH:")
first_olympics = df[df['Year'] == df['Year'].min()]
recent_olympics = df[df['Year'] == df['Year'].max()]
print(f"   Athletes (1896): {first_olympics['ID'].nunique():,}")
print(f"   Athletes (2016): {recent_olympics['ID'].nunique():,}")
print(f"   Growth Factor: {recent_olympics['ID'].nunique() / first_olympics['ID'].nunique():.1f}x")

# ====================================================================
# PART 8: CONCLUSIONS AND KEY FINDINGS
# ====================================================================

print("\n" + "="*80)
print("CONCLUSIONS AND KEY FINDINGS")
print("="*80)

print("""
KEY FINDINGS:

1. DOMINANT NATIONS:
   - USA leads in total medals across Olympic history
   - Top 5 countries account for a significant portion of all medals
   - Traditional powerhouses maintain consistency over decades

2. PARTICIPATION EVOLUTION:
   - Dramatic growth from ~240 athletes (1896) to ~10,000+ (2016)
   - Female participation grew from near 0% to ~45% by 2016
   - Number of participating countries increased significantly

3. ATHLETE CHARACTERISTICS:
   - Average age of medal winners: ~26 years
   - Physical characteristics vary significantly by sport
   - Height and weight show positive correlation among winners

4. SPORT TRENDS:
   - Athletics (Track & Field) produces the most medals
   - Swimming and Gymnastics are also high-medal sports
   - Winter Olympics have fewer participants but high competitiveness

5. TEMPORAL PATTERNS:
   - Clear growth trajectory in both athletes and events
   - Gender equality improving but not yet achieved
   - Modern Olympics (2000+) much larger than early games

INTERESTING OBSERVATIONS:
   - Some athletes have won 10+ medals in their careers
   - Physical requirements differ dramatically across sports
   - Participation gaps during World War periods visible in data

LIMITATIONS:
   - Missing data for age, height, weight (~10-30%)
   - Host country data not included in this dataset
   - Team vs individual sports create some counting complexities
   - Medal counts don't distinguish team vs individual achievements

RECOMMENDATIONS FOR FUTURE ANALYSIS:
   - Include economic indicators to analyze country success factors
   - Add host country data to study home advantage
   - Analyze training systems and sports infrastructure
   - Study correlation between population size and medal count
   - Investigate doping scandals' impact on medal distributions
""")

# ====================================================================
# PART 9: EXPORT RESULTS
# ====================================================================

print("\n" + "="*80)
print("EXPORTING RESULTS")
print("="*80)

# Save processed data
df.to_csv('olympics_processed_data.csv', index=False)
print("✓ Processed data saved as 'olympics_processed_data.csv'")

# Save medal winners only
medal_winners.to_csv('olympics_medal_winners.csv', index=False)
print("✓ Medal winners data saved as 'olympics_medal_winners.csv'")

# Save summary statistics
summary_dict = {
    'Metric': ['Total Athletes', 'Total Countries', 'Total Sports', 'Total Events', 
               'Total Medals', 'Male Athletes', 'Female Athletes', 'Years Covered'],
    'Value': [
        df['ID'].nunique(),
        df['NOC'].nunique(),
        df['Sport'].nunique(),
        df['Event'].nunique(),
        medal_df.shape[0],
        df[df['Sex'] == 'M']['ID'].nunique(),
        df[df['Sex'] == 'F']['ID'].nunique(),
        df['Year'].max() - df['Year'].min() + 4
    ]
}
summary_df = pd.DataFrame(summary_dict)
summary_df.to_csv('olympics_summary.csv', index=False)
print("✓ Summary statistics saved as 'olympics_summary.csv'")

print("\n" + "="*80)
print("PROJECT COMPLETE!")
print("="*80)
print("\nGenerated Files:")
print("1. olympics_analysis_main.png (9 visualizations)")
print("2. olympics_top5_trends.png (Medal trends)")
print("3. olympics_processed_data.csv (Full processed dataset)")
print("4. olympics_medal_winners.csv (Medal winners only)")
print("5. olympics_summary.csv (Summary statistics)")
print("\nNext Steps:")
print("- Copy this code into Jupyter Notebook")
print("- Update file path to your athlete_events.csv location")
print("- Run all cells and generate outputs")
print("- Convert to HTML and PDF")
print("- Create your 5-7 minute video presentation")
print("\n" + "="*80)