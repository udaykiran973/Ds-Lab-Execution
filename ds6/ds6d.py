import pandas as pd

p = pd.Period('2026-07', freq='M')

print("Original Period:")
print(p)

print("\nAfter adding 7:")
print(p + 7)
print("\nAfter subtracting 4:")
print(p - 4)
periods = pd.period_range(
    start='2026-01',
    periods=4,
    freq='M'
)

print("\nRange of Periods:")
print(periods)