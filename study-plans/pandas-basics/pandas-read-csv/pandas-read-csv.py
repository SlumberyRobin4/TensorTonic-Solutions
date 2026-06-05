import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """

    #convert dictionary data to df
    df = pd.DataFrame(data)

    #initialize data dictionary
    data_dict = dict()

    #convert df to dictionary using col names as key and values as list of column values
    data_dict['data'] = df.to_dict('list')

    #add df shape to dictionary, 'shape' is key and df.shape is value
    data_dict['shape'] = list(df.shape)

    #add df columns to dictionary, "columns" is key and df.columns is value
    data_dict['columns'] = list(df.columns)

    return data_dict