def clean_col_meta(df):
    def clean_col(col):
        col = col.strip()
        col = col.replace("Operating System","os")
        col = col.replace(" ","_")
        col = col.replace("(","")
        col = col.replace(")","")
        col = col.lower()
        return col

    df.columns = [clean_col(_temp_column) for _temp_column in df.columns]
    return(df)
	
def simplify_gwarancja(df):
    #temp_seria =  df["gwarancja"].str.replace('brak', 'sprzedawcy')
    df.loc[df.gwarancja == 'brak', 'gwarancja'] = 'sprzedawcy'
    #df["gwarancja_t"] = temp_seria
    return df
	
def simplify_komunikacja(df):
    
    df['komunikacja_t'] = df['komunikacja'].replace(np.nan, 'komunikacja_bd')
    komunikacja_item = df["komunikacja_t"].apply(pd.Series).stack().unique().tolist()
    count_komunikacja_item = {}
    for i in komunikacja_item:
        temp_ = (df["komunikacja_t"].str.contains(i, regex=False)*1).sum()
        count_komunikacja_item[i]= temp_
    for i in komunikacja_item:
        df[i] = (df["komunikacja_t"].str.contains(i, regex=False)*1).fillna(0)
    a = []
    for i in df['komunikacja_t']:    
        a.append(len(i))

    df['count_of_komunikacja'] = a
    df.loc[df['komunikacja_bd']==1,"count_of_komunikacja"] = 0

    return(df)
	