import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


# import each month data
jan = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_Jan.csv")
Feb = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_Feb.csv")
Mar = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_Mar.csv")
April = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_April.csv")
May = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_May.csv")
June = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_June.csv")
July = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_July.csv")
August = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_August.csv")
September = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_September.csv")
October = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_October.csv")
November = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_November.csv")
December = pd.read_csv("C:\\Coursera\\Capstone\\2021\\Trip_Data_December.csv")

# Aggregating all months data
All_Months_Data = [jan, Feb, Mar, April, May, June, July, August, September, October, November, December]

# keeping all months data in a dataframe
all_data_df = pd.concat(All_Months_Data)

# declaring ride duration as a time. Column shall be in hh:mm:ss format
all_data_df["ride_duration"] = pd.to_timedelta(all_data_df["ride_duration"])

# declaring starting date as a date
all_data_df["started_at_date"] = pd.to_datetime(all_data_df["started_at_date"])

# segregating summation of ride duration of different starting weekdays' data depending on member and casual
member_rides_duration = all_data_df[all_data_df["member_casual"] == "member"].groupby('started_at_weekday')[
    'ride_duration'].sum()
casual_rides_duration = all_data_df[all_data_df["member_casual"] == "casual"].groupby("started_at_weekday")[
    'ride_duration'].sum()

# plotting figure for comparison depending on ride duration(started_at_weekday)
plt.plot(member_rides_duration, color ='g', label ='member')
plt.plot(casual_rides_duration, color ='r', label ='casual')
plt.title('weekday vs rides duration')
plt.xlabel('started_at_weekday')
plt.ylabel('ride duration')
plt.legend()
plt.show()


# counting total ride id of different starting weekdays' data of member and casual
member_rides_id = all_data_df[all_data_df["member_casual"] == "member"].groupby('started_at_weekday')[
    'ride_id'].count()
casual_rides_id = all_data_df[all_data_df["member_casual"] == "casual"].groupby("started_at_weekday")[
    'ride_id'].count()

# plotting figure for comparison depending on ride duration(started_at_weekday)
plt.plot(member_rides_id, color ='g', label ='member')
plt.plot(casual_rides_id, color ='r', label ='casual')
plt.title('weekday vs total ride ID')
plt.xlabel('started_at_weekday')
plt.ylabel('total ride ID')
plt.legend()
plt.show()

# finding mean of ride duration of different starting weekdays' data of member and casual
member_rides_duration_mean = all_data_df[all_data_df["member_casual"] == "member"].groupby('started_at_weekday')[
    'ride_duration'].mean()
casual_rides_duration_mean = all_data_df[all_data_df["member_casual"] == "casual"].groupby("started_at_weekday")[
    'ride_duration'].mean()
plt.plot(member_rides_duration_mean, color ='g', label ='member')
plt.plot(casual_rides_duration_mean, color ='r', label ='casual')
plt.title('weekday vs mean rides duration')
plt.xlabel('started_at_weekday')
plt.ylabel('mean ride duration')
plt.legend()
plt.show()


# finding max of ride duration of different starting weekdays' data of member and casual
member_rides_duration_max = all_data_df[all_data_df["member_casual"] == "member"].groupby('started_at_weekday')[
    'ride_duration'].max()
casual_rides_duration_max = all_data_df[all_data_df["member_casual"] == "casual"].groupby("started_at_weekday")[
    'ride_duration'].max()

# plotting figure
plt.plot(member_rides_duration_max, color ='g', label ='member')
plt.plot(casual_rides_duration_max, color ='r', label ='casual')
plt.title('weekday vs max rides duration')
plt.xlabel('started_at_weekday')
plt.ylabel('max ride duration')
plt.legend()
plt.show()

# finding modes of ride of different starting weekdays' of member and casual
member_rides_duration_mode = all_data_df[all_data_df["member_casual"] == "member"]["started_at_weekday"].mode()
casual_rides_duration_mode = all_data_df[all_data_df["member_casual"] == "casual"]["started_at_weekday"].mode()


# finding total number of users
# finding total number of users
member_total_numbers = all_data_df[all_data_df["member_casual"] == "member"]['member_casual'].count()
casual_total_numbers = all_data_df[all_data_df["member_casual"] == "casual"]['member_casual'].count()

plt.bar('member', member_total_numbers)
plt.bar('casual', casual_total_numbers)
plt.title('No. of Total riders')
plt.show()

#drawing pie chart
member_total_numbers = all_data_df[all_data_df["member_casual"] == "member"]['member_casual'].count()
casual_total_numbers = all_data_df[all_data_df["member_casual"] == "casual"]['member_casual'].count()
total_users_number=[member_total_numbers, casual_total_numbers]
member_type=['member', 'casual']


plt.pie(total_users_number, labels=member_type, autopct= '%1.1f%%')
plt.title('total users')
plt.show()

#rideable_bike
plt.figure(figsize=(8,6))
sns.countplot(x="member_casual",hue="rideable_type", data=all_data_df)
plt.show()

#monthly_data
plt.figure(figsize=(8,6))
sns.countplot(x="member_casual",hue="started_at_month", data=all_data_df)
plt.show()




