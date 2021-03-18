import pandas as pd

def value_counts(df: pd.DataFrame, 
                 col: str, 
                 *args. **kwargs) -> pd.DataFrame:
    """
    For a DataFrame (`df`): display normalized (percentage) 
    `value_counts(normalize=True)` and regular counts 
    `value_counts()` for a given `col`.
    """
    count = df[col].value_counts(*args, **kwargs).to_frame(name='count')
    perc = df[col].value_counts(normalize=True, *args,**kwargs) \
                  .to_frame(name='percentage')
    
    return pd.concat([count, perc], axis=1)