import pandas as pd

dates = pd.to_datetime([
    '2026-02-17',
    '2026-11-05'
])

sales = pd.Series(
    [1000, 1500],
    index=dates
)

print("Original Series:")
print(sales)

period_series = sales.to_period('M')

print("\nSeries converted to Monthly Periods:")
print(period_series)

df = pd.DataFrame(
    {
        'Sales': [1000, 1500],
        'Profit': [500, 700]
    },
    index=dates
)

print("\nOriginal DataFrame:")
print(df)

period_df = df.to_period('M')

print("\nDataFrame converted to Monthly Periods:")
print(period_df)