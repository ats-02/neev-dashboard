import pandas as pd

def load_data():
    # Read the data file safely from source directory
    df = pd.read_csv("data/machine_data.csv")

    # Wipe away any trailing unnamed index columns or formatting artifacts
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Exact expected application attributes order
    target_columns = [
        "sno", "time", "cycle", "lo_v", "hi_v", 
        "v_rise", "intensify", "p_rise", "biscuit_thick", 
        "cast_pressure", "cycle_time"
    ]

    # Map headers dynamic-safely by positional indexes to prevent length check crash
    rename_mapping = {df.columns[i]: target_columns[i] for i in range(min(len(df.columns), len(target_columns)))}
    df = df.rename(columns=rename_mapping)

    # Perform safe data conversion types execution
    if "cycle_time" in df.columns:
        if df["cycle_time"].dtype == 'object':
            df["cycle_time"] = pd.to_timedelta(df["cycle_time"]).dt.total_seconds()
        else:
            df["cycle_time"] = pd.to_numeric(df["cycle_time"], errors='coerce')

    return df
