import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column, xlabel, ylabel):
    """Plot histogram for a specific column."""
    plt.figure(figsize=(15, 6))
    df[column].hist()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_bar(df, x, y, xlabel, ylabel):
    """Plot bar plot for specific columns."""
    plt.figure(figsize=(30, 10))
    sns.barplot(x=x, y=y, data=df)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
