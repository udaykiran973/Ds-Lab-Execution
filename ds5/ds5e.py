# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Create sample data
# data = {
#     'Department': [
#         'CSE', 'CSE', 'CSE', 'CSE', 'CSE',
#         'ECE', 'ECE', 'ECE', 'ECE', 'ECE',
#         'EEE', 'EEE', 'EEE', 'EEE', 'EEE'
#     ],
#     'Marks': [
#         78, 85, 90, 72, 88,
#         65, 70, 82, 75, 80,
#         60, 68, 72, 76, 85
#     ]
# }

# df = pd.DataFrame(data)

# print("Data:")
# print(df)

# # Create Box Plot
# plt.figure(figsize=(8, 5))

# sns.boxplot(
#     x='Department',
#     y='Marks',
#     data=df
# )

# plt.title("Marks Distribution by Department")
# plt.xlabel("Department")
# plt.ylabel("Marks")
# plt.grid(axis='y', linestyle='--', alpha=0.5)

# plt.tight_layout()
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'Department': [
        'CSE', 'CSE', 'CSE', 'CSE', 'CSE',
        'ECE', 'ECE', 'ECE', 'ECE', 'ECE',
        'MECH', 'MECH', 'MECH', 'MECH', 'MECH'
    ],
    'Marks': [
        76, 85, 91, 80, 89,
        70, 81, 92, 76, 87,
        65, 77, 87, 72, 82
    ]
}
df = pd.DataFrame(data)
print("Data:")
print(df)
plt.figure(figsize=(8, 5))
sns.boxplot(
    x='Department',
    y='Marks',
    data=df
)
plt.title("Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Marks")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
