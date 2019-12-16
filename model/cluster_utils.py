# cluster_utils.py

"""
utility file with clustering & plotting methods
"""


import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def scree_plot(df, title_in="", drop_index=False):
    """
    scree plot to view number of potentially viable components
    """

    X = df
    if drop_index:
        X = df.drop(df.columns[0], axis=1)
    X_std = StandardScaler().fit_transform(X)
    pca = PCA().fit(X_std)
    plt.plot(pca.singular_values_)
    plt.xlabel("num components")
    plt.ylabel("singular values")
    title_str = title_in + " " + "scree plot"
    plt.title(title_str)
    plt.show()


def kmeans(df, num_clusters, title_in="", drop_index=False):
    """
    2d kmeans clustering and plotting function
    plots results along 2 principal components
    """

    X = df
    if drop_index:
        X = df.drop(df.columns[0], axis=1)
    cluster_km = KMeans(n_clusters=num_clusters)
    cluster_y = cluster_km.fit_predict(X)

    # plotting
    reduced_data = PCA(n_components=2).fit_transform(X)
    results = pd.DataFrame(reduced_data, columns=["pc1", "pc2"])
    cmap = sns.color_palette(n_colors=num_clusters)
    sns.scatterplot(x="pc1", y="pc2", hue=cluster_y, palette=cmap, data=results)
    title_str = title_in + " " + str(num_clusters) + " Clusters"
    plt.title(title_str)
    plt.show()

    X["cluster"] = cluster_y
    return X


def kmeans3d(df, num_clusters, title_in="", drop_index=False):
    """
    3d kmeans clustering and plotting function
    plots results along 3 principal components
    """

    X = df
    if drop_index:
        X = df.drop(df.columns[0], axis=1)
    cluster_km = KMeans(n_clusters=num_clusters)
    cluster_y = cluster_km.fit_predict(X)

    # plotting
    reduced_data = PCA(n_components=3).fit_transform(X)
    results = pd.DataFrame(reduced_data, columns=["pc1", "pc2", "pc3"])
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(results["pc1"].values, results["pc2"].values,
               results["pc3"].values, c=cluster_y)
    title_str = title_in + " " + str(num_clusters) + " Clusters"
    plt.title(title_str)
    plt.show()

    X["cluster"] = cluster_y
    return X
