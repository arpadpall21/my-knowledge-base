import pandas as pd

df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Value': [10, 20, 15, 25, 30, 35],
    'Quantity': [1, 2, 3, 4, 5, 6]
})


print( 

df.groupby("Category")

)






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
