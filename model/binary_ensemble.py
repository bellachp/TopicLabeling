# binary ensemble.py


class BinaryEnsemble:
    """
    class for modeling individual binary models per label for fitting
    multiple independent models. works to avoid noise introduced by
    automatic ensembles of features such as in RF.
    """

    def __init__(self, x_data, y_data, threshold=0.8):

        self.threshold = threshold
        self.df_ensemble = []

        self.set_ensemble(x_data, y_data)


    # function to process full dataframe into smaller chunks
    def set_ensemble(self, X, Y):

        # example
        # topic_dict = {}
        # features = []
        # topic_dict["X"] = X[features]
        # topic_dict["Y"] = Y["some_label"]
        # topic_dict["metadata"] = "something"
        # self.df_ensemble.append(topic_dict)
        pass


    # getter
    def get_ensemble(self):

        return self.df_ensemble


# testdev case
if __name__ == '__main__':
    print("test")
