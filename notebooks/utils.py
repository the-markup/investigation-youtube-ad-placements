import pandas as pd

def value_counts(df: pd.DataFrame, 
                 col: str, **args) -> pd.DataFrame:
    """
    For a DataFrame (`df`): display normalized (percentage) 
    `value_counts(normalize=True)` and regular counts 
    `value_counts()` for a given `col`.
    """
    count = df[col].value_counts(**args).to_frame(name='count')
    perc = df[col].value_counts(normalize=True, **args) \
                  .to_frame(name='percentage')
    
    return count.T.append(perc.T).T 