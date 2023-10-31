import pandas as pd
from plotnine import *
import matplotlib.pyplot as plt
from plotnine import ggplot, aes, geom_line, labs, facet_wrap


# df_heartrate = pd.read_csv('heartrate_seconds_merged.csv')
# heartrate_graph = ggplot(data=df_heartrate) + aes(x='Id', y='Value') + geom_boxplot() + facet_wrap('~Id')
# print(heartrate_graph)
#
df_sleep = pd.read_csv('sleepDay_merged.csv')
# sleep_graph = ggplot(data=df_sleep) + aes(x="Id", y="TotalMinutesAsleep") + geom_boxplot() + facet_wrap('~Id')
# print(sleep_graph)
#
df_step = pd.read_csv('dailySteps_merged.csv')
# step_graph = ggplot(data=df_step) + aes(x="Id", y="StepTotal") + geom_boxplot() + facet_wrap('~Id')
# print(step_graph)

# df_weight = pd.read_csv('weightLogInfo_merged.csv')
# most_freq = df_weight['Id'].value_counts()
# most_freq = most_freq.index[0]
# df = df_weight[df_weight['Id'] == most_freq]
#
# plt.plot(df['Date'], df['WeightKg'])
# plt.xlabel('Date')
# plt.ylabel('Weight(Kg)')
# plt.title('Weight Over Time')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()



# Q2
# hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
# hourly_intensities = pd.read_csv('hourlyIntensities_merged.csv')
# hourly_steps = pd.read_csv('hourlySteps_merged.csv')
#
# calories_intensities = hourly_calories.merge(hourly_intensities)
# hourly_merged = calories_intensities.merge(hourly_steps)
# pd.set_option('display.max_columns', None)
# print(hourly_merged.head())
#
# minute_calories_narrow = pd.read_csv('minuteCaloriesNarrow_merged.csv')
# minute_intensities_narrow = pd.read_csv('minuteIntensitiesNarrow_merged.csv')
# minute_METs_narrow = pd.read_csv('minuteMETsNarrow_merged.csv')
#
# narrow_calories_intensities = minute_calories_narrow.merge(minute_intensities_narrow)
# narrow_merged = narrow_calories_intensities.merge(minute_METs_narrow)
# print(narrow_merged.head())
#
#
df_sleep['Date'] = pd.to_datetime(df_sleep['SleepDay'], infer_datetime_format=True)
# daily_activity = pd.read_csv('dailyActivity_merged.csv')
# daily_activity['Date'] = pd.to_datetime(daily_activity['ActivityDate'], infer_datetime_format=True)
# hourly_merged['Date'] = pd.to_datetime(hourly_merged['ActivityHour'], infer_datetime_format=True)
# narrow_merged['Date'] = pd.to_datetime(narrow_merged['ActivityMinute'], infer_datetime_format=True)
#
# print(hourly_merged.head())
# print(narrow_merged.head())
# print(df_sleep.head())
# print(daily_activity.head())

# df_heartrate_id = list(set(df_heartrate['Id']))
# df_heartrate['Time'] = pd.to_datetime(df_heartrate['Time'], infer_datetime_format=True)
# list_df = []
# for id in range(len(df_heartrate_id)):
#     subdata = df_heartrate[df_heartrate['Id'] == df_heartrate_id[id]]
#     grouped = subdata.groupby(pd.Grouper(key='Time', freq='1Min'))
#     mean_df = grouped['Value'].mean().reset_index()
#     mean_df['Id'] = df_heartrate_id[id]
#     mean_df = mean_df[['Id', 'Time', 'Value']]
#     list_df.append(mean_df)
# df = pd.concat(list_df, ignore_index=True)
# print(df.head())


# Q3
# hourly_graph_stepcalories = ggplot(data=hourly_merged) + aes(x='StepTotal',
#                                                              y='Calories') + geom_point()
# print(hourly_graph_stepcalories)
#
# hourly_graph_intensitiescalories = ggplot(data=hourly_merged) + aes(x='TotalIntensity',
#                                                                     y='Calories') + geom_point()
# print(hourly_graph_intensitiescalories)

# sleep_graph2 = ggplot(data=df_sleep) + aes(x="TotalMinutesAsleep", y="TotalTimeInBed") + geom_point()
# print(sleep_graph2)

# for id in list(set(daily_activity['Id'])):
#     sub_df = daily_activity[daily_activity['Id'] == id]
#     print(sub_df)
#     intensity_graph = ggplot(data=sub_df) + aes(x='Date', y='VeryActiveDistance') + ggtitle(
#         'Very Active Distance of User Id: ' + str(id)) + geom_bar(stat="identity", fill="blue") + labs(x="Date",
#                                                                                                        y="Very Active Distance")
#     print(intensity_graph)


# merge_sleep_activity = daily_activity.merge(df_sleep)
# print(merge_sleep_activity)
#
# print(ggplot(data=merge_sleep_activity) + aes(x='TotalMinutesAsleep', y='SedentaryMinutes') + geom_point())


# Q4
df_step['Date'] = pd.to_datetime(df_step['ActivityDay'], infer_datetime_format=True)
calories_df = pd.read_csv('dailyCalories_merged.csv')
calories_df['Date'] = pd.to_datetime(df_step['ActivityDay'], infer_datetime_format=True)

merge_sleep_step = df_step.merge(df_sleep)
merge_sleep_step = merge_sleep_step.merge(calories_df)
pd.set_option('display.max_columns', None)

merge_sleep_step = merge_sleep_step[(merge_sleep_step != 0).all(1)]
merge_sleep_step = merge_sleep_step.dropna()
for id in list(set(merge_sleep_step['Id'])):
    sub = merge_sleep_step[merge_sleep_step['Id'] == id]
    print(sub.head())
    print(sub[['Date', 'TotalMinutesAsleep', 'StepTotal']])
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)

    ax1.plot(sub['Date'], sub['StepTotal'], color='blue', label='Graph 1')
    ax1.set_title('Total steps')
    ax2.plot(sub['Date'], sub['TotalMinutesAsleep'], color='red', label='Graph 2')
    ax2.set_title('Total Minutes Asleep')

    ax1.set_ylabel('Step Total')
    ax1.legend()
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Total Minutes Asleep')
    ax2.legend()
    plt.suptitle('Total Minutes Asleep and Total Step per date of user id: ' + str(id))
    plt.tight_layout()
    plt.show()









