import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)


# Функція для збереження графіка у файл
def save_fig(fig, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)  # Закриваємо фігуру після збереження

# Будуємо bar plot для категоріальної колонки
def plot_categorical(df, column, title=None):
    counts = df[column].value_counts()
    fig = plt.figure()
    sns.barplot(x=counts.index, y=counts.values, color="skyblue")
    plt.title(title if title else column)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    save_fig(fig, f"../outputs/figures/{column}_barplot.png")

# Гістограма віку
def plot_age_histogram(df):
    fig = plt.figure()
    sns.histplot(df['age'], bins=10, kde=True, color="skyblue")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    save_fig(fig, "../outputs/figures/age_histogram.png")

# Boxplot: задоволеність по країнах
def plot_satisfaction_box_by_country(df):
    fig = plt.figure()
    sns.boxplot(x='country', y='satisfaction_1to5', data=df, color="lightgreen")
    plt.title("Satisfaction by Country")
    plt.ylabel("Satisfaction (1-5)")
    plt.xticks(rotation=45)
    save_fig(fig, "../outputs/figures/satisfaction_by_country.png")

# Pie chart для favorite_brand
def plot_pie_favorite_brand(df):
    counts = df['favorite_brand'].value_counts()
    fig = plt.figure()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title("Favorite Brand Distribution")
    save_fig(fig, "../outputs/figures/favorite_brand_pie.png")



