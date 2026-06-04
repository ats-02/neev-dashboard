import pandas as pd

def load_data():

    df = pd.read_csv("data/machine_data.csv")

    df.columns = [
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

    df["cycle_time"] = (
        pd.to_timedelta(df["cycle_time"])
        .dt.total_seconds()
    )

    return df
