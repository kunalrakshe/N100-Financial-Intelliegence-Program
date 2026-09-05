import pandas as pd

from normaliser import normalize_year, normalize_ticker


def load_excel(file_path):
    df = pd.read_excel(file_path)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    if "year" in df.columns:
        df["year"] = df["year"].apply(normalize_year)

    if "ticker" in df.columns:
        df["ticker"] = df["ticker"].apply(normalize_ticker)

    return df