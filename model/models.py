# models.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

from .binary_ensemble import BinaryEnsemble


class Results:

    def __init__(self):

        self.some_report_holder = {}


class Models:

    def __init__(self, model="", models=[]):

        self.models_list = []
        self.results = {}

        if models:
            self.models_list = models
        else:
            self.models_list.append(model)


    def fit_models(self, X, label_columns):

        # shuffle and separate labels
        X = X.sample(frac=1).reset_index(drop=True)
        Y = X[label_columns]
        X = X.drop(label_columns, axis=1)

        # some modeling loop


    def simple_rf(self, X, Y):

        # generate split
        x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
        cv = KFold(n_splits=5)

        # model and cross val result collection
        scores = []
        for train, test in cv.split(x_train, y_train):
            rf = RandomForestClassifier(n_estimators=100)
            rf.fit(x_train[train], y_train[train])

            score = rf.score(x_train[test], y_train[test])
            scores.append(score)

        cv_score = np.mean(scores)

        # on test set
        rf = RandomForestClassifier(n_estimators=100)
        rf.fit(x_train, y_train)
        test_score = rf.score(x_test, y_test)
        y_pred = rf.predict(x_test)
        cf_mat = confusion_matrix(y_test, y_pred)
        cf_report = classification_report(y_test, y_pred)
        cross_tab = pd.crosstab(y_test, y_pred, rownames=["True"],
                                colnames="Predicted", margins=True)

        # feature importance
        features = list(zip(list(x_test.columns), rf.feature_importances_))
        features = sorted(features, key=lambda x: x[1], reverse=True)
        fdf = pd.DataFrame(features)

        # return results somehow
