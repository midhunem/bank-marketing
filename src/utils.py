import sys
import pandas as pd
import numpy as np
import pickle

def custom_imputation(bank_df_unique):
    """
    Perform custom imputation for education and job missing values in the input DataFrame.
    Parameters:
    - bank_df_unique : The input DataFrame.

    Returns:
    - pandas.DataFrame: The DataFrame with missing values imputed based on custom rules.
    """
    bank_df_unique.loc[(bank_df_unique['age']>60) & (bank_df_unique['job']=='unknown'), 'job'] = 'retired'

    bank_df_unique.loc[(bank_df_unique['education']=='unknown') & (bank_df_unique['job']=='management'), 'education'] = 'university.degree'
    bank_df_unique.loc[(bank_df_unique['education']=='unknown') & (bank_df_unique['job']=='services'), 'education'] = 'high.school'
    bank_df_unique.loc[(bank_df_unique['education']=='unknown') & (bank_df_unique['job']=='housemaid'), 'education'] = 'basic.4y'
    bank_df_unique.loc[(bank_df_unique['education']=='unknown') & (bank_df_unique['job']=='admin'), 'education'] = 'university.degree'
    bank_df_unique.loc[(bank_df_unique['education']=='unknown') & (bank_df_unique['job']=='technician'), 'education'] = 'professional.course'

    bank_df_unique.loc[(bank_df_unique['job'] == 'unknown') & (bank_df_unique['education']=='basic.4y'), 'job'] = 'blue-collar'
    bank_df_unique.loc[(bank_df_unique['job'] == 'unknown') & (bank_df_unique['education']=='basic.6y'), 'job'] = 'blue-collar'
    bank_df_unique.loc[(bank_df_unique['job'] == 'unknown') & (bank_df_unique['education']=='basic.9y'), 'job'] = 'blue-collar'
    bank_df_unique.loc[(bank_df_unique['job']=='unknown') & (bank_df_unique['education']=='professional.course'), 'job'] = 'technician'
    bank_df_unique.loc[(bank_df_unique['job']=='unknown') & (bank_df_unique['education']=='university.degree'), 'job'] = 'management'
    bank_df_unique.loc[(bank_df_unique['job']=='unknown') & (bank_df_unique['education']=='high.school'), 'job'] = 'services'
    bank_df_unique.loc[(bank_df_unique['job']=='unknown') & (bank_df_unique['education']=='basic.4y'), 'job'] = 'housemaid'
    return bank_df_unique

def transform_pdays(bank_df_unique):
    """
    Transform the 'pdays' column in the input DataFrame into categorical values.
    Parameters:
    - bank_df_unique : The input DataFrame containing the 'pdays' column.

    Returns:
    - pandas.DataFrame: The DataFrame with the 'pdays' column transformed into categorical values.

    This function transforms the 'pdays' column in the input DataFrame into categorical values based on the following criteria:
    - If 'pdays' is 999, it is categorized as 'not_contacted'.
    - If 'pdays' is between 0 and 5 , it is categorized as 'contacted_less_than_5day'.
    - If 'pdays' is between 6 and 15 , it is categorized as 'contacted_5_15day'.
    - If 'pdays' is greater than 15, it is categorized as 'contacted_greaterthan_15day'.
    The transformed DataFrame includes a new column 'pdays_category' containing the categorical values, and the original 'pdays' column is dropped.
    """

    conditions = [
    (bank_df_unique['pdays'] == 999),
    (bank_df_unique['pdays'] >= 0) & (bank_df_unique['pdays'] <= 5),
    (bank_df_unique['pdays'] > 5) & (bank_df_unique['pdays'] <= 15),
    (bank_df_unique['pdays'] > 15)
    ]
    values = ['not_contacted', 'contacted_less_than_5day', 'contacted_5_15day', 'contacted_greaterthan_15day']
    bank_df_unique['pdays_category'] = np.select(conditions, values)
    bank_df_unique = bank_df_unique.drop('pdays', axis=1)
    return bank_df_unique

def categorical_encoding(bank_df_unique):
    """
    Apply categorical encoding to the input for inference.
    Parameters:
    - bank_df_unique : The input DataFrame.

    Returns:
    - pandas.DataFrame: The DataFrame with categorical variables encoded using one-hot encoding.

    """
    bank_df_unique = pd.get_dummies(bank_df_unique)
    with open('models/encoded_columns.pkl', 'rb') as f:
        encoded_columns = pickle.load(f)
    bank_df_unique_encoded = bank_df_unique.reindex(columns=encoded_columns, fill_value=0)
    return bank_df_unique_encoded

def preprocess_input(data):
    df = pd.DataFrame(data)
    df_duration_dropped = df.drop(['duration'],axis=1)
    df_custom_imputed = custom_imputation(df_duration_dropped)
    df_pday_transformed = transform_pdays(df_custom_imputed)
    df_processed = categorical_encoding(df_pday_transformed)
    return df_processed