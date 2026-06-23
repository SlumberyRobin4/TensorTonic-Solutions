import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    #convert data dict to df
    df = pd.DataFrame(data)

    #initialize empty dictionary 
    df_dict = dict()

    #convert column to list and add to df_dict under values key
    df_dict['values'] = df[column].tolist()

    #add length to df_dict
    df_dict['length'] = len(df[column])

    return df_dict
    