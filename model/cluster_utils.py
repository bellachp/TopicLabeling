# cluster_utils.py

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class ClusterUtils:
    """
    utility class with clustering & plotting methods
    """

    def __init__(self):

        self.idx = 0


    def scree_plot(self, df, title_in="", drop_index=False):

        X = df_in.drop(df_in.columns[0], axis=1)
        X_std = StandardScaler().fit_transform(X)
        pca = PCA().fit(X_std)
        plt.plot(pca.singular_values_)
        plt.xlabel("num components")
        plt.ylabel("singular values")
        title_str = title_in + " " + "scree plot"
        plt.title(title_str)
        plt.show()


    def kmeans(self):

        pass


    def kmeans3d(self):

        pass