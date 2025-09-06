from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import re

app = Flask(__name__)

def get_fin_data():
    df = pd.read_csv(r'data/Company data.csv')

    # get percentage change (%)
    df['Revenue Growth (%)'] = df.groupby(['Company Name'])['Revenue'].pct_change()
    df['Net Income Growth (%)'] = df.groupby(['Company Name'])['Net Income'].pct_change()
    df['Operating Cash Flow (%)'] = df.groupby(['Company Name'])['Net Income'].pct_change()

    # formatting the percentage change columns to "%"
    df['Revenue Growth (%)'] = df['Revenue Growth (%)'].apply(lambda x: '{:.2%}'.format(x))
    df['Net Income Growth (%)'] = df['Net Income Growth (%)'].apply(lambda x: '{:.2%}'.format(x))
    df['Operating Cash Flow (%)'] = df['Operating Cash Flow (%)'].apply(lambda x: '{:.2%}'.format(x))

    # calculate debt to asset ratio
    df['Debt-to-Asset Ratio'] = df['Liabilities'] / df['Assets']

    print(df)
    print(list(df.columns))
    return df

# get_fin_data()

def extract_info(sentence):
    """
    Extracts the company name, year, and financial metric from a sentence
    based on a predefined structure.

    The expected sentence structure is:
    "Please provide the <metric> of <company> for <year>"

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary containing the extracted information.
    """
    # Initialize variables with None
    metric = None
    company = None
    year = None

    # Define regex patterns for extraction
    # The (.+) part is a capturing group that matches any character one or more times,
    # and the ? at the end makes it non-greedy, so it stops at the first 'of'.
    # re.IGNORECASE makes the search case-insensitive.
    pattern_metric = re.search(r'provide the (.+?) of', sentence, re.IGNORECASE)
    if pattern_metric:
        metric = pattern_metric.group(1).strip()

    # Pattern to find the company between "of" and "for"
    pattern_company = re.search(r'of (.+?) for', sentence, re.IGNORECASE)
    if pattern_company:
        company = pattern_company.group(1).strip()

    # Pattern to find the year after "for"
    # \d{4} matches exactly four digits.
    pattern_year = re.search(r'for\s+(\d{4})', sentence)
    if pattern_year:
        year = pattern_year.group(1).strip()

    # return {
    #     'company': company,
    #     'year': year,
    #     'metric': metric
    # }
    return company, year, metric


def get_metric_info(company_name, year, metric_found):
    result = None
    findata_df = get_fin_data()
    # print(findata_df)
    # print(findata_df.columns)
    metric_column = metric_found
    print(findata_df[(findata_df['Company Name'] == company_name) & (findata_df['Year'] == year)])
    print(len(findata_df[(findata_df['Company Name'] == company_name) & (findata_df['Year'] == year)]))
    if len(findata_df[(findata_df['Company Name'] == company_name) & (findata_df['Year'] == year)]) > 0:
        result = np.array(findata_df[(findata_df['Company Name'] == company_name) & (findata_df['Year'] == int(year))][metric_column])[0]
        print(result)
    else:
        result = None
    return result

# Route to the home page where the form is located
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle the form submission
@app.route('/result', methods=['POST'])
def result():
    input_sentence = request.form.get('user_sentence')
    company, year, metric = extract_info(input_sentence)
    result = get_metric_info(company, int(year), metric)
    return render_template('result.html', company=company, year=year, metric=metric, result=result)

if __name__ == "__main__":
    app.run(debug=True)