import pandas as pd
dates=pd.to_datetime([
    '2026-11-05',
    '2026-02-17',
    '2026-07-21'
])
temperature=[26,34,28]
time_series=pd.Series(
    temperature,
    index=dates
)
print("Time Series:")
print(time_series)