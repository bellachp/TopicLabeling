# test_model.py
# script to run modeling functions

import pandas as pd
import numpy as np

from model_configs import ExConfig
from model.load_utils import DataLoader
from model.labels_reader import LabelsReader
from model.binary_ensemble import BinaryEnsemble
import model.cluster_utils as clust

import pandas_profiling

# load data

# load labels

# process data

# drop columns for modeling

# shuffle and separate labels
label_columns = labels_df.columns[1:]
X = X.sample(frac=1).reset_index(drop=True)
Y = X[label_columns]
X = X.drop(label_columns, axis=1)

# create binary ensemble to test features
be = BinaryEnsemble(X, Y)
be_dfs = be.get_ensemble()

report_path = "pandas_reports/"
for frame in be_dfs:
    pandas_report = frame["X"].profile_report()
    pandas_report.to_file(output_file=report_path + "unique name")
    clust.scree_plot(frame["X"])
    w = clust.kmeans(frame["X"], 2, title_in="some title")
