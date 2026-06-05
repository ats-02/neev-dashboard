import pandas as pd

def load_data():
    # Read the data file
    df = pd.read_csv("data/machine_data.csv")

    # Drop any completely empty columns or unnamed index columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # Your 11 explicit process parameters
    target_columns = [
        "sno",
        "time",
        "cycle",
        "lo_v",
        "hi_v",
        "v_rise",
        "intensify",
        "p_rise",
        "biscuit_thick",
        "cast_pressure",
        "cycle_time"
    ]

    # Map headers by index position to prevent strict length crash
    rename_mapping = {df.columns[i]: target_columns[i] for i in range(min(len(df.columns), len(target_columns)))}
    df = df.rename(columns=rename_mapping)

    # Convert cycle_time safely to numerical float seconds
    if "cycle_time" in df.columns:
        if df["cycle_time"].dtype == 'object':
            # Converts time strings like "00:01:23" to raw seconds
            df["cycle_time"] = pd.to_timedelta(df["cycle_time"]).dt.total_seconds()
        else:
            # Handles columns that are already numeric numbers safely
            df["cycle_time"] = pd.to_numeric(df["cycle_time"], errors='coerce')

    return df
