"""This script collects data."""

import os

import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame(
        data={"voltage": np.random.randn(1000)},
        index=pd.date_range(
            "2024-08-01", "2024-08-01 00:00:01", freq="ms", inclusive="left"
        ),
    )
    df.index.name = "time"
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/data.csv", index=True)
