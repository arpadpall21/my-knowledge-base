# import pandas as pd

# coffe_shop = pd.DataFrame({
#     'Coffe Category': ['A', 'A', 'B', 'B', 'C', 'C', 'C'],
#     'Price': [54, 44, 32, 25, 19, 16, 20],
#     'Sold': [24, 12, 73, 88, 54, 19, 30]
# })


# print(
#     coffe_shop["Sold"].sum()    # total sold across all categories
# )

# print(
#     coffe_shop.groupby("Coffe Category")["Price"].mean()      # average price for each coffee category
# )
# print(
#     coffe_shop.groupby("Coffe Category")["Sold"].sum()        # total sold for each coffee category
# )



###########################################################
### Complex example
###########################################################
import pandas as pd

company_data = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy'],
    'Age': [25, 30, 35, 45, 40, 50, 28, 32, 38],
    'Salary': [50000, 60000, 70000, 80000, 90000, 100000, 75000, 65000, 85000],
    'Years_of_Experience': [1, 5, 10, 15, 20, 25, 3, 7, 12]
})

aggregated_data = company_data.groupby('Department').agg({
    'Salary': ['mean', 'max', 'min'],
    'Years_of_Experience': 'mean',
    'Employee': 'count',
    'Age': 'mean'
}).reset_index()

aggregated_data.columns = [
    'Department', 
    'Average_Salary', 'Max_Salary', 'Min_Salary', 
    'Average_Years_of_Experience', 
    'Total_Employees', 
    'Average_Age'
]

print(aggregated_data)









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
