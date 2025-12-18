# Data cleaning and preprocessing
import pandas as pd
import re

def clean_text(text):
    """Clean and normalize text"""
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower().strip()
    return text

def clean_catalog(input_path, output_path):
    """Clean the scraped catalog data"""
    df = pd.read_csv(input_path)
    df['description'] = df['description'].apply(clean_text)
    df.to_csv(output_path, index=False)

if __name__ == '__main__':
    clean_catalog('data/raw_catalog.csv', 'data/shl_catalog.csv')
