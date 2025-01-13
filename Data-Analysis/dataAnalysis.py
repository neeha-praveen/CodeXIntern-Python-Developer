import pandas as pd

df = pd.read_csv('data.csv')

# displays the first five rows of the data file
print(df.head())

# describes the numerical data with statistics
print(df.describe())

# finds missing values in each column
missingVal = df.isnull().sum()
print("missing values in each column: \n", missingVal)

# calculates the average of a column
avg = df['Age'].mean()
print(f"average of age: {avg}")

# counts the number of unique values in a column
unique = df['Age'].nunique()
print(f"unique values: {unique}")

# filters rows based on a condition
dev = df[df['Department']=='Development']
print(f"employees working in development:\n",dev)

# find max
max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary']==max_salary]
print(f"highest paid employee: \n {max_salary_emp}")

# counts frequency of each value in a column
emp_dept_count = df['Department'].value_counts()
print(f"no. of employees in each department: \n {emp_dept_count}")

# sorts data by column
sort = df.sort_values(by='Age', ascending=False)
print(f"Sorted by age: \n {sort}")

df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x>30 else 'Junior')
print("data w experience column: \n",df)