import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/ai_trends_dummy.csv')

def plot_ai_trends(df):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 2, 1)
    sns.lineplot(x='Year', y='AI_Investment_Billion', data=df, marker='o', color='blue')
    plt.title('AI Investment Growth (Billion $)')
    
    plt.subplot(2, 2, 2)
    sns.lineplot(x='Year', y='AI_Job_Postings', data=df, marker='o', color='green')
    plt.title('AI Job Postings Trend')

    plt.subplot(2, 2, 3)
    sns.lineplot(x='Year', y='AI_Patents_Filed', data=df, marker='o', color='red')
    plt.title('AI Patents Filed Over Time')

    plt.subplot(2, 2, 4)
    sns.lineplot(x='Year', y='Global_AI_Adoption_%', data=df, marker='o', color='purple')
    plt.title('Global AI Adoption % Over Time')

    plt.tight_layout()
    plt.show()

plot_ai_trends(df)

