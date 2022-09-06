# -*- coding: utf-8 -*-
"""Module 4_Pandas_Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KMy6s3i2vwwxEw9AZJzxyLquzfkmiLkZ

<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

# Practice Lab: Selecting data in a Dataframe

Estimated time needed: **15** minutes

## Objectives

After completing this lab you will be able to:

*   Use Pandas Library to create DataFrame and Series
*   Locate data in the DataFrame using <code>loc()</code> and <code>iloc()</code> functions
*   Use slicing

### Exercise 1: Pandas: DataFrame and Series

**Pandas** is a popular library for data analysis built on top of the Python programming language. Pandas generally provide two data structures for manipulating data, They are:

*   DataFrame
*   Series

A **DataFrame** is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

*   A Pandas DataFrame will be created by loading the datasets from existing storage.
*   Storage can be SQL Database, CSV file, an Excel file, etc.
*   It can also be created from the lists, dictionary, and from a list of dictionaries.

**Series** represents a one-dimensional array of indexed data.
It has two main components :

1.  An array of actual data.
2.  An associated array of indexes or data labels.

The index is used to access individual data values. You can also get a column of a dataframe as a **Series**. You can think of a Pandas series as a 1-D dataframe.
"""

# let us import the Pandas Library
import pandas as pd

"""Once you’ve imported pandas, you can then use the functions built in it to create and analyze data.

**In this practice lab, we will learn how to create a DataFrame out of a dictionary.**

Let us consider a dictionary 'x' with keys and values as shown below.

We then create a dataframe from the dictionary using the function pd.DataFrame(dict)
"""

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

"""We can see the direct correspondence between the table. The keys correspond to the column labels and the values or lists corresponding to the rows.

#### Column Selection:

To select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.

Let's Retrieve the data present in the <code>ID</code> column.
"""

#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x

"""Let's use the <code>type()</code> function and check the type of the variable.

"""

#check the type of x
type(x)

"""The output shows us that the type of the variable is a DataFrame object.

#### Access to multiple columns

Let us retrieve the data for <code>Department</code>, <code>Salary</code> and <code>ID</code> columns
"""

#Retrieving the Department, Salary and ID columns and assigning it to a variable z

z = df[['Department','Salary','ID']]
z

"""### Try it yourself

##### Problem 1: Create a dataframe to display the result as below:

<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/images/Student_data.png" width="300" alt="Student Data"  />
</center>
"""

#EJERCICIO 1
R = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}
df = pd.DataFrame(R)
df

"""<details><summary>Click here for the solution</summary>

```python
a = {'Student':['David', 'Samuel', 'Terry', 'Evan'],
     'Age':['27', '24', '22', '32'],
     'Country':['UK', 'Canada', 'China', 'USA'],
     'Course':['Python','Data Structures','Machine Learning','Web Development'],
     'Marks':['85','72','89','76']}
df = pd.DataFrame(a)
df
    
```

</details>

##### Problem 2: Retrieve the Marks column and assign it to a variable b
"""

#EJERCICIO 2
b = df[['Marks']]
b

"""<details><summary>Click here for the solution</summary>

```python
b = df[['Marks']]
b
    
```

</details>

##### Problem 3: Retrieve the Country and Course columns and assign it to a variable c
"""

#EJERCICIO 3
c = df[['Country','Course']]
c

"""<details><summary>Click here for the solution</summary>

```python
c = df[['Country','Course']]
c
    
```

</details>

#### To view the column as a series, just use one bracket:
"""

# Get the Name column as a series Object

x = df['Name']
x

#check the type of x
type(x)

"""The output shows us that the type of the variable is a Series object.

### Exercise 2: <code>loc()</code> and <code>iloc()</code> functions

<code>loc()</code> is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. This method includes the last element of the range passed in it.

Simple syntax for your understanding:

*   loc\[row_label, column_label]

<code>iloc()</code> is an indexed-based selecting method which means that we have to pass integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it.

Simple syntax for your understanding:

*   iloc\[row_index, column_index]

<h4 id="data">Let us see some examples on the same.</h4>
"""

# Access the value on the first row and the first column

df.iloc[0, 0]

# Access the value on the first row and the third column

df.iloc[0,2]

# Access the column using the name

df.loc[0, 'Salary']

"""Let us create a new dataframe called 'df1' and assign 'df' to it. Now, let us set the "Name" column as an index column using the method set_index().

"""

df1=df
df1=df1.set_index("Name")

#To display the first 5 rows of new dataframe
df1.head()

#Now, let us access the column using the name
df1.loc['Jane', 'Salary']

"""### Try it yourself

Use the <code>loc()</code> function,to get the Department of Jane in the newly created dataframe df1.
"""

#EJERCICIO 4
df.loc[['Jane', 'Department']]

"""<details><summary>Click here for the solution</summary>

```python
df.loc[['Jane', 'Department']]
    
```

</details>

Use the <code>iloc()</code> function,to get the Salary of Mary in the newly created dataframe df1.
"""

#EJERCICIO 5
df1.iloc[3,2]

"""<details><summary>Click here for the solution</summary>

```python
df1.iloc[3,2]
    
```

</details>

### Exercise 3: Slicing

Slicing uses the \[] operator to select a set of rows and/or columns from a DataFrame.

To slice out a set of rows, you use this syntax: data\[start:stop],

here the start represents the index from where to consider, and stop represents the index one step BEYOND the row you want to select. You can perform slicing using both the index and the name of the column.

> NOTE: When slicing in pandas, the start bound is included in the output.

So if you want to select rows 0, 1, and 2 your code would look like this: df.iloc\[0:3].

It means you are telling Python to start at index 0 and select rows 0, 1, 2 up to but not including 3.

> NOTE: Labels must be found in the DataFrame or you will get a KeyError.

Indexing by labels(i.e. using <code>loc()</code>) differs from indexing by integers (i.e. using <code>iloc()</code>). With <code>loc()</code>, both the start bound and the stop bound are inclusive. When using <code>loc()</code>, integers can be used, but the integers refer to the index label and not the position.

For example, using <code>loc()</code> and select 1:4 will get a different result than using <code>iloc()</code> to select rows 1:4.

<h4 id="data">We can also select a specific data value using a row and column location within the DataFrame and iloc indexing.
"""

# let us do the slicing using old dataframe df

df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

#let us do the slicing using loc() function on new dataframe df1 where index column is Name having labels: Rose, John and Jane
df1.loc['Rose':'Jane', 'ID':'Department']

"""<h2 id="quiz">Try it yourself</h2>

using <code>loc()</code> function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3
"""

# EJERCICIO 6
df.loc[2:3,'Name':'Department']

"""<details><summary>Click here for the solution</summary>

```python
df.loc[2:3,'Name':'Department']
    
```

</details>

<h3 id="quiz">Congratulations, you have completed this lesson and the practice lab on Pandas</h3>

## Author(s):

[Appalabhaktula Hema](https://www.linkedin.com/in/hema-a-39002b128/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01)

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By          | Change Description      |
| ----------------- | ------- | ------------------- | ----------------------- |
| 2022-03-10        | 0.1     | Appalabhaktula Hema | Created initial version |

<hr/>

## <h3 align="center"> © IBM Corporation 2022. All rights reserved. <h3/>
"""