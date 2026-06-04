def production_summary(df):

    return {

        "total_shots": len(df),

        "avg_cycle_time":
        round(
            df["cycle_time"].mean(),
            2
        ),

        "avg_cast_pressure":
        round(
            df["cast_pressure"].mean(),
            2
        )
    }

