def detect_root_cause(latest):

    if latest["cast_pressure"] < 930:

        return {

            "issue": "Low Cast Pressure",

            "cause": "Accumulator Charge Drop",

            "impact": "Short Fill Risk",

            "action": "Check Nitrogen Pressure"
        }

    elif latest["hi_v"] < 3.90:

        return {

            "issue": "Low Hi-V",

            "cause": "Hydraulic Velocity Loss",

            "impact": "Incomplete Filling",

            "action": "Inspect Hydraulic Circuit"
        }

    else:

        return {

            "issue": "Healthy Process",

            "cause": "No Major Deviation",

            "impact": "Stable Production",

            "action": "Continue Monitoring"
        }

