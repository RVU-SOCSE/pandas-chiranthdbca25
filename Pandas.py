Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
##### Write a Python program that creates a Pandas DataFrame from scratch using a dictionary. Display the DataFrame
import pandas as pd

data = {'Product': ['Laptop', 'Smartphone', 'Tablet', 'Monitor'],'Price': [1200, 800, 450, 300],'Quantity_Sold': [5, 12, 8, 15]}
df = pd.DataFrame(data)
print(df)
      Product  Price  Quantity_Sold
0      Laptop   1200              5
1  Smartphone    800             12
2      Tablet    450              8
3     Monitor    300             15
>>> ########add a new column with calculated values
>>> df['Total_Revenue'] = df['Price'] * df['Quantity_Sold']
>>> print(df)
      Product  Price  Quantity_Sold  Total_Revenue
0      Laptop   1200              5           6000
1  Smartphone    800             12           9600
2      Tablet    450              8           3600
3     Monitor    300             15           4500
>>> ######## Write a Python program to load a CSV file (Mcd) into a Pandas DataFrame,identify missing values, and fill them with a specific value (e.g., the mean of a column).
>>> import pandas as pd
>>> path = r'C:\Users\CHIRANTH D\OneDrive\Desktop\BCA Hons\SEM - 02\PYTHON LAB\Github Assingment\Data1.csv'
>>> df = pd.read_csv(path)
>>> print(df.isnull().sum())
Year                          0
McDonalds_Revenue_$Billion    0
Growth_rate_percent           1
Q1                            4
Q2                            4
Q3                            4
Q4                            3
dtype: int64
>>> df.fillna('NaN')
    Year  McDonalds_Revenue_$Billion Growth_rate_percent   Q1   Q2   Q3   Q4
0   1999                        13.3                 NaN  NaN  NaN  NaN  NaN
1   2000                        14.2                 7.0  NaN  NaN  NaN  NaN
2   2001                        14.9                 4.0  NaN  NaN  NaN  NaN
3   2002                        15.4                 4.0  NaN  NaN  NaN  3.0
4   2003                        17.1                11.0  3.8  4.3  4.5  4.6
5   2004                        18.6                 8.0  4.4  4.7  4.9  4.5
6   2005                        19.1                 3.0  4.8  5.1  5.3  3.9
7   2006                        20.9                 9.0  4.9  5.4  5.5  5.1
8   2007                        22.8                 9.0  5.3  5.8  5.9  5.8
9   2008                        23.5                 3.0  5.6  6.1  6.3  5.6
10  2009                        22.7                -3.0  5.1  5.6  6.0  6.0
11  2010                        24.1                 6.0  5.6  5.9  6.3  6.2
12  2011                        27.0                12.0  6.1  6.9  7.2  6.8
13  2012                        27.6                 2.0  6.5  6.9  7.2  7.0
14  2013                        28.1                 2.0  6.6  7.1  7.3  7.1
15  2014                        27.4                -2.0  6.7  7.2  7.0  6.6
16  2015                        25.4                -7.0  6.0  6.5  6.6  6.3
17  2016                        24.6                -3.0  5.9  6.3  6.4  6.0
18  2017                        22.8                -7.0  5.7  6.0  5.8  5.3
19  2018                        21.3                -7.0  5.1  5.4  5.4  5.4
20  2019                        21.4                 1.0  5.0  5.3  5.6  5.4
21  2020                        19.2               -10.0  4.7  3.8  5.4  5.3
22  2021                        23.2                21.0  5.1  5.9  6.2  6.0
23  2022                        23.2                 0.0  5.7  5.7  5.9  5.9
df.isnull()
     Year  McDonalds_Revenue_$Billion  Growth_rate_percent  ...     Q2     Q3     Q4
0   False                       False                 True  ...   True   True   True
1   False                       False                False  ...   True   True   True
2   False                       False                False  ...   True   True   True
3   False                       False                False  ...   True   True  False
4   False                       False                False  ...  False  False  False
5   False                       False                False  ...  False  False  False
6   False                       False                False  ...  False  False  False
7   False                       False                False  ...  False  False  False
8   False                       False                False  ...  False  False  False
9   False                       False                False  ...  False  False  False
10  False                       False                False  ...  False  False  False
11  False                       False                False  ...  False  False  False
12  False                       False                False  ...  False  False  False
13  False                       False                False  ...  False  False  False
14  False                       False                False  ...  False  False  False
15  False                       False                False  ...  False  False  False
16  False                       False                False  ...  False  False  False
17  False                       False                False  ...  False  False  False
18  False                       False                False  ...  False  False  False
19  False                       False                False  ...  False  False  False
20  False                       False                False  ...  False  False  False
21  False                       False                False  ...  False  False  False
22  False                       False                False  ...  False  False  False
23  False                       False                False  ...  False  False  False

[24 rows x 7 columns]
