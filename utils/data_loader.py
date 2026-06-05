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

    # --- PERFECTED CYCLE TIME CONVERSION FOR "00:00:48" ---
    if "cycle_time" in df.columns:
        # Clean up any accidental leading/trailing blank spaces in the text
        df["cycle_time"] = df["cycle_time"].astype(str).str.strip()
        
        # Convert "00:00:48" into 48.0 seconds flat safely
        df["cycle_time"] = pd.to_timedelta(df["cycle_time"], errors='coerce').dt.total_seconds()
        
        # If there are any missing rows, fallback to 0.0 so math equations don't fail
        df["cycle_time"] = df["cycle_time"].fillna(0.0)
    # -----------------------------------------------------

    return df
