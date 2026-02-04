####################################################################
# Accessing DataFrame Rows and Columns
####################################################################
# import pandas as pd

# df = pd.DataFrame(
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],
#     columns=["A", "B", "C"],
# )

# print( df.loc[0] )                 # return sthe 1st row as a Series
# print( df.loc[0:1] )               # returns the 1st and 2nd rows as a DataFrame
# print( df.loc[[0, 2, 5]] )         # returns the 1st, 3rd, and 6th rows as a DataFrame
# print( df.loc[1:4, ["A", "C"]] )   # returns rows 2 to 5 of columns A and C as a DataFrame

# print( df.iloc[0] )                  # returns the 1st row as a Series
# print( df.iloc[0:2] )                # returns the 1st and 2nd rows as a DataFrame
# print( df.iloc[[0, 2, 5]] )          # returns the 1st, 3rd, and 6th rows as a DataFrame
# print( df.iloc[1:5, [0, 2]] )        # returns rows 2 to 5 of columns A and C as a DataFrame
# print( df.iloc[0:2, 0:2])            # returns rows 1 to 2 of columns A and B as a DataFrame 


####################################################################
# Modifying data in a DataFrame
####################################################################
# import pandas as pd

# df = pd.DataFrame(
#     [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9],
#      [10, 11, 12],
#      [13, 14, 15],
#      [16, 17, 18]],
#     columns=["A", "B", "C"],
# )

# # df.loc[0, "A"] = 100        # modify single value
# # df.iloc[1, 0] = 200         # modify single value

# df.iloc[0:2, 0:2] = 300       # modify multiple values

# cofee["revenue"] = cofee["Units Sold"] * coffe["New Price"]     # add new column based on calculation (DOCU)



####################################################################
# indexing
####################################################################
# import pandas as pd

# data = {
#     'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
#     'Coffee': ['Latte', 'Espresso', 'Cappuccino', 'Americano', 'Mocha', 'Flat White', 'Macchiato'],
#     'Units Sold': [120, 150, 200, 180, 220, 160, 140]
# }
# coffe_shop = pd.DataFrame(data)

# print(coffe_shop.index)                 # indexed by default with a RangeIndex starting from 0 to 5
# coffe_shop.index = coffe_shop['Day']    # set index (which is row labels) to 'Day' column

# print(coffe_shop.loc["Wednesday"])      # access row by index label



####################################################################
# sort
####################################################################
# import pandas as pd

# coffe_shop = pd.DataFrame({
#     'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
#     'Coffee': ['Latte', 'Espresso', 'Cappuccino', 'Americano', 'Mocha', 'Flat White', 'Macchiato'],
#     'Units Sold': [120, 150, 200, 180, 220, 160, 140]
# })

# print(coffe_shop.sort_values("Units Sold"))   # returns a new DataFrame sorted by 'Units Sold' in ascending order
# print(coffe_shop.sort_values("Units Sold", ascending=False))  # returns a new DataFrame sorted by 'Units Sold' in descending order

# print(coffe_shop.sort_values(["Units Sold", "Day"]))  # sorts by 'Units Sold' and then by 'Day' for ties

# print(coffe_shop)             # original DataFrame remains unchanged



####################################################################
# filter
####################################################################
# import pandas as pd
# from pathlib import Path

# olympic_data = pd.read_excel(Path() / 'olympics-data.xlsx')

# print(
#     olympic_data[olympic_data['height_cm'] > 200]     # returns a new filtered DataFrame with rows where 'height_cm' > 200
# )

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html
# print(
#     olympic_data.query('height_cm > 200 and born_country == "FRA"')     # returns a new filtered DataFrame with rows where 'height_cm' > 200 and 'born_country' is 'FRA'
# )


# print(
#     olympic_data[(olympic_data['height_cm'] > 200) & (olympic_data['born_country'] == "FRA")]     # returns a new filtered DataFrame with rows where 'height_cm' > 200 and 'born_country' is 'FRA'
# )

# print(
#     olympic_data.loc[olympic_data['born_country'] == "USA", ["name", "born_city"]]   # returns a new filtered DataFrame with specific columns where 'born_country' is 'USA'
# )

# print(
#     olympic_data.loc[olympic_data['born_country'] == "USA"].sort_values('height_cm', ascending=False).head(5)   # returns a new filtered and sorted DataFrame 
# )

# the str.contains(regExp)    accepts regular expressions Document this
# https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html (series method to filter)
# print(
#     olympic_data.loc[olympic_data["name"].str.contains("tommy", case=False)],       # returns a new filtered DataFrame with rows where 'name' contains 'Tommy'
# )




####################################################################
# Adding new column / Drop column
####################################################################
import pandas as pd

olympic_data = pd.read_excel("olympics-data.xlsx")

# # olympic_data["medals_won"] = "Gold"   # add new column with default value



# # document this https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html (apply method)
# # def continent_condition(row):
# #     if row['born_country'] == 'USA':
# #         return 'America'
# #     else:
# #         return 'Not America'

# # olympic_data["continent"] = olympic_data.apply(continent_condition, axis=1)  # add new column based on condition

def in_column(row):
    row["height_inch"] = row["height_cm"] > 200:




# # print( olympic_data.drop(columns=["died_date", "NOC"]) )  # returns a new DataFrame with specified columns dropped (does not modify original DataFrame)

# # olympic_data.drop(columns=["died_date", "NOC"], inplace=True) # drops specified columns from the original DataFrame (modifies the original DataFrame)


# print( olympic_data.head() )



####################################################################
# rename columns
####################################################################
# import pandas as pd
# from pathlib import Path

# olympic_data = pd.read_excel(Path() / 'olympics-data.xlsx')

# print( olympic_data.rename(columns={"born_country": "country_of_birth", "born_city": "city_of_birth"}) )  # returns a new DataFrame with renamed columns (does not modify original DataFrame)

# olympic_data.rename(columns={"born_country": "country_of_birth", "born_city": "city_of_birth"}, inplace=True) # renames columns in the original DataFrame (modifies the original DataFrame)

# print( olympic_data )




####################################################################
# rename columns
####################################################################
# import pandas as pd
# from pathlib import Path

# olympic_data = pd.read_excel(Path() / 'olympics-data.xlsx')
# olympic_data["born_date"] = pd.to_datetime(olympic_data["born_date"], format="%Y-%m-%d")     # convert 'born_date' column to datetime, invalid parsing will be set as NaT

# print(
#     olympic_data.info()
# )

# print(
#     olympic_data.sample(20)
# )




####################################################################
# write to file
####################################################################
# import pandas as pd

# olympic_data = pd.read_excel("olympics-data.xlsx")
# olympic_data.to_csv("olympics-data.csv", index=False)    # write DataFrame to CSV file without the index column