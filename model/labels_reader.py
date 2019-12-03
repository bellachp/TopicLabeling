# labels_reader.py

import pandas as pd
# import jellyfish


labels_word_list = ["bag of labels"]


class Label:
    """
    simple label object for nesting labels
    """

    def __init__(self, level_in):

        self.level = level_in
        self.value = 0
        self.nodes = {}


class SomeLabel:
    """
    example implementing some label structure
    """

    def __init__(self, idx):

        self.main_id = idx

        self.label = Label(0)

        self.label.nodes["subterm"] = Label(1)
        self.label.nodes["other"] = Label(1)

        self.label.nodes["subterm"].nodes["subsub"] = Label(2)


    # various process loops
    def add_label(self, tag):

        for k1, v1 in self.label.nodes.items():
            if k1 == tag:
                v1.value = 1
                return
            elif v1.nodes:
                for k2, v2 in v1.nodes.items():
                    if k2 == tag:
                        v2.value = 1
                        v1.value = 1
                        return

        # to reach here, no label. do string matching
        closest_str = self.compute_closest_string(tag)
        self.add_label(closest_str)


    # string matching function could go here
    def compute_closest_string(self, tag):

        pass


class LabelsReader:
    """
    parse excel files of labeled data into label
    heirarchy to capture usage for modeling
    """

    def __init__(self):

        self.labels = []


    # pandas excel loaders
    def load_xlsx(self, filename, sheetname=""):

        xlfile = pd.ExcelFile(filename)

        shee1 = None
        if sheetname == "":
            sheet1 = xlfile.parse(0)
        else:
            sheet1 = xlfile.parse(sheetname)

        # do parsing...


    # convert labels to dataframe
    def labels_to_dataframe(self, label_level):

        # get cols
        # labels
        # labels = [ll.get_labelrow(level=label_level) for ll in self.labels]
        # df = pd.DataFrame(labels, columns=cols)
        # return df
        pass


# testdev case
if __name__ == '__main__':

    ff = "file"

    lr = LabelsReader()
    lr.load_xlsx(ff, sheetname="bob")
    lr.load_xlsx(ff, sheetname="tony")

    df = lr.labels_to_dataframe(label_level=2)
