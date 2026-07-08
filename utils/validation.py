# utils/validation.py
import pandas as pd

def validate_dataframe(df: pd.DataFrame) -> bool:
    """Valida que el dataframe no esté vacío y tenga las columnas esperadas."""
    required_columns = ['species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']
    if df.empty:
        return False
    return all(col in df.columns for col in required_columns)

def validate_no_nulls(df: pd.DataFrame, columns: list) -> int:
    """Retorna la cantidad de nulos en las columnas especificadas."""
    return df[columns].isnull().sum().sum()   
