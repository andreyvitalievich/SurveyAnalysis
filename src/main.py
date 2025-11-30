from src.data_cleaning import load_data, clean_data
from src.analysis import mean_satisfaction_by_country, descriptive_stats, value_counts
from src.visualization import plot_categorical, plot_age_histogram, plot_satisfaction_box_by_country, plot_pie_favorite_brand

file_path = '../data/user_survey_50.csv'
df = load_data(file_path)
df = clean_data(df)

# Категоріальні дані
print("Gender distribution:\n", value_counts(df, 'gender'))
print("Education distribution:\n", value_counts(df, 'education'))
print("Favorite brand distribution:\n", value_counts(df, 'favorite_brand'))

# Середня задоволеність по країнах
print("Mean satisfaction by country:\n", mean_satisfaction_by_country(df))

# Статистика числових колонок
print("Descriptive statistics:\n", descriptive_stats(df))

print(df.head())

# Категоріальні графіки
plot_categorical(df, 'gender', "Gender Distribution")
plot_categorical(df, 'education', "Education Level Distribution")

# Гістограма віку
plot_age_histogram(df)

# Boxplot задоволеності по країнах
plot_satisfaction_box_by_country(df)

# Pie chart favorite brand
plot_pie_favorite_brand(df)
