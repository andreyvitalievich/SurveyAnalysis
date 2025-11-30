import pandas as pd


# Завантаження файлу CSV
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):

    # Перевірка на пропуски в колонках
    print("Missing values per column:\n", df.isnull().sum())

    # Виявили що в колонці улюблений бренд є 8 пропусків замінюєм їх на Unknown
    df['favorite_brand'] = df['favorite_brand'].fillna("Unknown")
    print("Missing values per column:\n", df.isnull().sum())

    # Перевіримо що віковий стовпець має числовий тип данних
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    # Створення вікових категорій
    bins = [17, 24 , 34 , 44 , 54 , 60]
    labels = ['18-24', '25-34', '35-44', '45-54', '55-60']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

    return df
