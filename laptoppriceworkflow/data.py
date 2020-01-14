def get_json_data(filname = 'data\public-dataset.json'):
    """Download and cache the laptop-dataset
    Parameters
    ====
    filename : string
        Name of data
    Returns
    ====
    data : pandas.DataFrame
        The laptop price data
    """
    import pandas as pd
    dataset = pd.read_json(filname)
    df = pd.DataFrame(dataset)
    return dataset
	