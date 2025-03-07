import pandas as pd
import numpy as np

def generate_dummy_ai_trends():
    np.random.seed(42)
    years = np.arange(2010, 2031)
    
    investment = np.cumsum(np.random.randint(5, 20, size=len(years))) * 1.5
    job_postings = np.cumsum(np.random.randint(1000, 5000, size=len(years)))
    patents = np.cumsum(np.random.randint(50, 200, size=len(years)))
    adoption_rate = np.clip(np.cumsum(np.random.uniform(1, 5, size=len(years))), 0, 100)
    
    df = pd.DataFrame({
        'Year': years,
        'AI_Investment_Billion': investment,
        'AI_Job_Postings': job_postings,
        'AI_Patents_Filed': patents,
        'Global_AI_Adoption_%': adoption_rate
    })
    
    df.to_csv('../data/ai_trends_dummy.csv', index=False)
    print("Dataset saved to 'data/ai_trends_dummy.csv'")

generate_dummy_ai_trends()

