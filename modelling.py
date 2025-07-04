import pandas as pd
import sklearn as sk
import streamlit as st
import numpy as np


def prepare_data(data, info_dictionary):
    """
    Prepares the data for modeling by cleaning and transforming it.
    
    Steps:
    - Numerical values as floats or ints, whichever is most appropriate
    - Categorical variables as strings or integers, depending on the model
    - Dates as datetime objects
    - Some columns are recorded as lists, so we would need to split these into separate columns

    Parameters:
    - data: pandas DataFrame containing the raw data.
    - info_dictionary: dictionary containing information about the dataset, including
      categorical and numerical column names.

    Returns:
    - cleaned_data: pandas DataFrame with cleaned and transformed data.
    """
    # Example of cleaning: removing NaN values
    cat_cols = info_dictionary["categorical_cols"]
    num_cols = info_dictionary["numerical_cols"]
    id_col = info_dictionary["id_col"]
    date_cols, date_format = info_dictionary["date_cols"], info_dictionary["date_format"]

    cleaned_data = data.copy()

    # Convert date columns to datetime
    for col in date_cols:
        cleaned_data[col] = pd.to_datetime(cleaned_data[col], format=date_format, errors="coerce")

    cleaned_data[num_cols] = cleaned_data[num_cols].apply(pd.to_numeric, errors='coerce')
    cleaned_data[id_col] = cleaned_data[id_col].astype(int)

    # Encode categorical variables
    for col in cat_cols:
        if cleaned_data[col].dtype == 'object':
            cleaned_data[col] = cleaned_data[col].astype('category')
        else:
            cleaned_data[col] = cleaned_data[col].astype('int')

    return cleaned_data


def train_test_split(data, target, test_size=0.2, random_state=42):
    """
    Splits the data into training and testing sets.
    
    Parameters:
    - data: pandas DataFrame containing the cleaned data.
    - target: string, the name of the target column.
    - test_size: float, proportion of the dataset to include in the test split.
    - random_state: int, controls the shuffling applied to the data before applying the split.

    Returns:
    - X_train: training features.
    - X_test: testing features.
    - y_train: training labels.
    - y_test: testing labels.
    """
    from sklearn.model_selection import train_test_split

    # Assuming 'target' is the label column
    X = data.drop(columns=[target])
    y = data[target]
    
    positives = y.value_counts().get(1, 0)
    negatives = y.value_counts().get(0, 0)

    return X_train, X_test, y_train, y_test