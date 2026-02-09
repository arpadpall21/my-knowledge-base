import pandas as pd

coffe_shop = pd.DataFrame({                                                                           
        'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'Coffee': ['Latte', 'Espresso', 'Cappuccino', 'Americano', 'Mocha', 'Flat White', 'Macchiato'],
        'Units Sold': [120, 150, 200, 180, 220, 160, 140],
    })

    ### accessing by  label
# print( coffe_shop["Units Sold"] )    # returns the 'Units Sold' column as a Series
# print( coffe_shop[["Day", "Coffee"]] )   # returns the 'Day' and 'Coffee' columns as a DataFrame

#     # indices also can be used as labels
# print( coffe_shop.loc[0])                 # returns the 1st row as a Series
# print( coffe_shop.loc[0:4])               # returns the 1st to 5th rows as a DataFrame
# print( coffe_shop.loc[[2, 3]])            # returns the 3rd and 4th rows as a DataFrame

# print( coffe_shop.loc[0, ["Day"]])        # returns the value of the 'Day' column for the 1st row
# print( coffe_shop.loc[0:2, ["Day", "Units Sold"]])   # returns the 'Day' and 'Units Sold' columns for the 1st to 3rd rows as a DataFrame (slicing data by label)

coffe_shop.rename(index=["mon", "tue", "wed", "thu", "fri", "sat", "sun"], inplace=True)
print( coffe_shop.loc["mon":"fri", ["Day", "Coffee"]] )

















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
# apply()
####################################################################
# import pandas as pd

# olympic_data = pd.read_excel("olympics-data.xlsx")

# olympic_data["medals_won"] = "Gold"   # add new column with default value



# # document this https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html (apply method)
# # def continent_condition(row):
# #     if row['born_country'] == 'USA':
# #         return 'America'
# #     else:
# #         return 'Not America'

# # olympic_data["continent"] = olympic_data.apply(continent_condition, axis=1)  # add new column based on condition

# olympic_data["height_inch"] = olympic_data.apply(lambda row: row["height_cm"] * 0.393701, axis=1)

# print( olympic_data.head() )



# # print( olympic_data.drop(columns=["died_date", "NOC"]) )  # returns a new DataFrame with specified columns dropped (does not modify original DataFrame)

# # olympic_data.drop(columns=["died_date", "NOC"], inplace=True) # drops specified columns from the original DataFrame (modifies the original DataFrame)


# print( olympic_data.head() )





####################################################################
# write to file
####################################################################
# import pandas as pd

# olympic_data = pd.read_excel("olympics-data.xlsx")
# olympic_data.to_csv("olympics-data.csv", index=False)    # write DataFrame to CSV file without the index column




####################################################################
# merge dataframes
####################################################################
# import pandas as pd

# olympic_data_short = pd.read_csv("olympics-data-short.csv")
# country_code_map = pd.read_csv("country-code-map.csv")

# print(
#     olympic_data_short
# )

# print(
#     country_code_map
# )

# # SQL style merge dataframes (join) on specified columns with left join (all rows from left DataFrame plus matching rows from right DataFrame)
# print(
#     pd.merge(olympic_data_short, country_code_map, left_on="born_country", right_on="country_code", how="left")
# )
# # SQL style merge dataframes (join) on specified columns with right join (all rows from right DataFrame plus matching rows from left DataFrame)
# print(
#     pd.merge(olympic_data_short, country_code_map, left_on="born_country", right_on="country_code", how="right")
# )
# SQL style merge dataframes (join) on specified columns with inner join (only matching rows from both DataFrames)
# print(
#     pd.merge(olympic_data_short, country_code_map, left_on="born_country", right_on="country_code", how="inner")
# )



####################################################################
# concat dataframes (do this stuff for example)
####################################################################
# import pandas as pd

# olympic_data_short = pd.read_excel("olympics-data.xlsx")

# hun_athletes = olympic_data_short[olympic_data_short["born_country"] == "HUN"].head(10)
# rou_athletes = olympic_data_short[olympic_data_short["born_country"] == "ROU"].head(10)

# hun_rou_athletes = pd.concat([hun_athletes, rou_athletes], ignore_index=True)   # concatenate two DataFrames into one, resetting the index




####################################################################
# handling null / missing values
####################################################################
# import pandas as pd

# olympic_data = pd.read_excel("olympics-data.xlsx")


# print(
#     olympic_data_short.isna()          # returns a DataFrame of the same shape with boolean values indicating presence of null values
# )

# print(
#     olympic_data_short.isna().sum()    # returns a Series with the count of null values in each column
# )

# new_olympic_data = olympic_data.head(100)

# remove rows were there's any null values
# print(
#     new_olympic_data.dropna()
# )
# remove rows where a specific column has null values
# print(
#     new_olympic_data.dropna(subset="died_date")
# )

# print(
#     new_olympic_data
# )


# # fill null values with a specified value
# print(
#     new_olympic_data.fillna("Unknown")
# )


# new_olympic_data = olympic_data.head(100)

# # print(
# #     new_olympic_data[new_olympic_data['died_date'].isna()]    # filter rows where 'died_date' is null
# # )
# print(
#     new_olympic_data[new_olympic_data['died_date'].notna()]    # filter rows where 'died_date' is not null
# )




####################################################################
# aggregation and grouping
####################################################################
# import pandas as pd

# olympic_data = pd.read_excel("olympics-data.xlsx")

# print(
#     olympic_data["born_city"].value_counts()   # returns a Series with counts of unique values in 'born_city' column
# )
# print(
#     olympic_data[olympic_data["born_country"] == "HUN"]["born_city"].value_counts()   # returns a Series with counts of unique values in 'born_city' column for athletes from Hungary
# )



# print(
#     olympic_data.groupby("born_country")["height_cm"].mean()  # returns a Series with average height for each country
# )

# DO THE PIVOT TABLE THING




####################################################################
# shift()
####################################################################
# import pandas as pd

# # Create a DataFrame for daily revenue
# data = {
#     "Date": ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"],
#     "Revenue": [200, 250, 220, 270, 300]
# }

# revenue_df = pd.DataFrame(data)

# # Convert 'Date' column to datetime for better handling
# revenue_df["Date"] = pd.to_datetime(revenue_df["Date"])

# # Shift the Revenue column by 1 day to create a "Previous Day Revenue" column
# revenue_df["Previous Day Revenue"] = revenue_df["Revenue"].shift(1)

# # Calculate the difference in revenue compared to the previous day
# revenue_df["Revenue Difference"] = revenue_df["Revenue"] - revenue_df["Previous Day Revenue"]

# # Display the DataFrame
# print(revenue_df)



####################################################################
# cumsum()
####################################################################
# import pandas as pd

# # Create a DataFrame for daily revenue
# data = pd.DataFrame({
#     "Date": ["2023-10-01", "2023-10-02", "2023-10-03", "2023-10-04", "2023-10-05"],
#     "Revenue": [200, 250, 220, 270, 300]
# })


# total_revenue = data["Revenue"].cumsum()   # returns a Series with the cumulative sum of the 'Revenue' column

# print(total_revenue)










###################################################################################
###################################################################################
###################################################################################
###################################################################################
###################################################################################
