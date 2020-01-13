def get_data():
    """Download and cache the laptop-dataset
    Parameters
    ====
    Returns
    ====
    data : pandas.DataFrame
        The laptop price data
    """
    import pandas as pd
    dataset = pd.read_json("laptoppriceworkflow/public-dataset.json")
    df = pd.DataFrame(dataset)
    return df