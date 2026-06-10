import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    #convert dictionary data to df
    df = pd.DataFrame(data)

    #initialize data dictionary
    data_dict = dict()

    #add df shape info to data_dict
    data_dict['rows'] = df.shape[0]
    data_dict['cols'] = df.shape[1]

    #add columns to data_dict as a list
    data_dict['columns'] = df.columns.tolist()

    #add dtypes to data_dict as a dict
    data_dict['dtypes'] = df.dtypes.astype(str).to_dict()

    #add size to data_dict
    data_dict['total_values'] = int(df.size)

    return data_dict