import pandas as pd

# Перевірка на унікальність значень в колонці, кількість повторень одного і того ж значення в колонці
def value_counts(df, column):
    counts = df[column].value_counts()
    return counts

# Середнє значення задоволенності по країнам
def mean_satisfaction_by_country(df):
    return df.groupby('country')['satisfaction_1to5'].mean()

# Базова статистика по числовим колонкам
def descriptive_stats(df):
    return df.describe()


