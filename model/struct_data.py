# struct_data.py


class StructData:
    """
    some low level data object for a data element
    """

    def __init__(self):

        self.idx = ""
        self.param = 0

        self.description = ""

        self.params = {}


    # prep for output
    def map_to_single_row(self):

        single_row = {}
        for param, val in self.params.items():
            single_row[param] = val

        return single_row


    # override repr
    def __repr__(self):

        return str(self.map_to_single_row())
