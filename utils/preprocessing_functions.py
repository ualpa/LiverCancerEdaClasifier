import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype

def nan_replace_df(t: pd.DataFrame) -> pd.DataFrame:
    for coloana in t.columns:
        if t[coloana].isna().any():
            if is_numeric_dtype(t[coloana]):
                t[coloana].fillna(t[coloana].mean(), inplace=True)
            else:
                t[coloana].fillna(t[coloana].mode()[0], inplace=True)