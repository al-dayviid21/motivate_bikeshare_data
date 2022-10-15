import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(
        "What city data are you interested in? (chicago, new york city, washington): \n"
    ).lower()
    cities = ["chicago", "new york city", "washington"]
    while city not in cities:
        print("Wrong input! \nTry again.")
        city = input(
            "What city data are you interested in? (chicago, new york city, washington): \n"
        ).lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        "Which month are you interested in? (all, january, february, ... , june): \n"
    ).lower()
    months = ["all", "january", "february", "march", "april", "may", "june"]
    while month not in months:
        print("Wrong input! \nTry again.")
        month = input(
            "Which month are you interested in? (all, january, february, ... , june): \n"
        ).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Which day of the week are you intereted in? (all, monday, tuesday, ... sunday): \n"
    ).lower()
    days_in_a_week = [
        "all", "monday", "tuesday", "wednesday", "thursday", "friday",
        "saturday", "sunday"
    ]
    while day not in days_in_a_week:
        print("Wrong input! \nTry again.")
        day = input(
            "Which day of the week are you intereted in? (all, monday, tuesday, ... sunday): \n"
        ).lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df["month"].mode()
    print("The most common month:", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df["day_of_week"].mode()
    print("The most common day of the week:", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df["Start Time"].dt.hour.mode()
    print("The most common start hour:", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print(
        f"The most commonly used start station is {most_common_start_station}")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print(f"The most commonly used start station is {most_common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df["Start Station"] + " & " + df["End Station"]
    most_common_station_combination = df['Station Combination'].mode()
    print(f"The most frequent combination of start and end station is {most_common_station_combination}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f"The total travel time is {total_travel_time}")
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time is {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type'].value_counts()
        print(f"{user_type}")
    except KeyError:
        print("*" *40)
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(f"{gender}")
    except KeyError:
        print("*" * 40)
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df["Birth Year"].min()
        print(f"The earliest year of birth is {earliest_year}")
    
        latest_year = df["Birth Year"].max()
        print(f"The earliest year of birth is {latest_year}")
    
        common_year = df["Birth Year"].mode()
        print(f"The earliest year of birth is {common_year}")
    except KeyError:
        print('*' * 40)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
