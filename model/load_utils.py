# load_utils.py

import pandas as pd
import numpy as np

from .struct_data import StructData


class DataLoader:
    """
    class to load & preprocess data with utility functions
    """

    def __init__(self):

        self.data_list = []


    def load_csv_data(self, filepath, column_list=[]):

        df = pd.read_csv(filepath)

        if column_list:
            df = df[column_list]

        return df


    def generate_data(self, df):

        some_columns_list = ["cols"]
        reduced_data = df[df[some_columns_list]].drop_duplicates()

        for k, row in reduced_data.iterrows():
            this_event = StructData()

            # do work

            # could add feature compute class


            self.data_list.append(this_event)


    def create_dummy_variables(self, df, column_list, prefix_list):

        return pd.get_dummies(df, columns=column_list, prefix=prefix_list)


    def incolumn_category_to_numeric(self, df, column_name):

        new_col = df[column_name].astype("category").cat.codes
        df[column_name] = new_col
