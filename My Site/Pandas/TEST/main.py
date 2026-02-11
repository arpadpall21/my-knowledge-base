import pandas as pd

comp_1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Departement': ['HR', 'IT', 'HR', 'Finance', 'IT'],
})

comp_2 = pd.DataFrame({
    'Name': ['Johon', 'Betty', 'Maggie', 'Jeny'],
    "DP": ['HR', 'Finance', 'Accounting', 'HR'],
})

comp_2_unique = comp_2.drop_duplicates(subset="DP") 

# print(
#     pd.merge(comp_1, comp_2, left_on="Departement", right_on="DP", how="left")
# )
# print(
#     pd.merge(comp_1, comp_2, left_on="Departement", right_on="DP", how="right")
# )
# print(
#     pd.merge(comp_1, comp_2, left_on="Departement", right_on="DP", how="inner")
# )
print(
    pd.merge(comp_1, comp_2, left_on="Departement", right_on="DP", how="outer")
)





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
# write to file
####################################################################
# import pandas as pd

# olympic_data = pd.read_excel("olympics-data.xlsx")
# olympic_data.to_csv("olympics-data.csv", index=False)    # write DataFrame to CSV file without the index column




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
