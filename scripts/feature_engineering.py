def cal_SOi(so2):
    """Calculate SO2 index."""
    # Logic for SO2
    # ...
    return si

def cal_Noi(no2):
    """Calculate NO2 index."""
    # Logic for NO2
    # ...
    return ni

def cal_RSPMI(rspm):
    """Calculate RSPM index."""
    # Logic for RSPM
    # ...
    return rpi

def cal_SPMi(spm):
    """Calculate SPM index."""
    # Logic for SPM
    # ...
    return spi

def cal_aqi(si, ni, rspmi, spmi):
    """Calculate AQI."""
    # Logic for AQI
    # ...
    return aqi

def apply_feature_engineering(df):
    """Apply all feature engineering steps to the dataframe."""
    df['SOi'] = df['so2'].apply(cal_SOi)
    df['Noi'] = df['no2'].apply(cal_Noi)
    df['Rpi'] = df['rspm'].apply(cal_RSPMI)
    df['SPMi'] = df['spm'].apply(cal_SPMi)
    df['AQI'] = df.apply(lambda x: cal_aqi(x['SOi'], x['Noi'], x['Rpi'], x['SPMi']), axis=1)
    return df

