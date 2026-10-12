import pandas as pd

data = {
    'Department': ['CSE', 'CSE', 'ECE'],
    'Marks': [ 75, 85, 95],
    'Attendance': [ 75, 95, 100]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

result = df.groupby('Department').aggregate({
    'Marks': ['sum', 'mean', 'std'],
    'Attendance': ['sum', 'mean', 'std']
})

print("\nSummary Statistics:")
print(result)