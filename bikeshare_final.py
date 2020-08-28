import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        try:
            valid_city = ['chicago', 'new york city', 'washington']
            city = str(input('Input city: ')).lower()
            if city in valid_city:
                break
            else:
                print('Not a valid input!')
        except:
            print('Not a valid input!')



    while True:
        try:
            valid_month = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            month = str(input('Input month: ')).lower()
            if month in valid_month:
                break
            else:
                print('Not a valid month!')
        except:
            print('Not a valid month!')


    while True:
        try:
            valid_day = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            day = str(input('Input day of the week: ')).lower()
            if day in valid_day:
                break
            else:
                print('Not a valid day!')
        except:
            print('Not a valid day!')

    print('-'*40)
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    common_month = df['Month'].mode()[0]
    print('Most common month: ', common_month)


    common_day = df['Day'].mode()[0]
    print('Most common day of the week: ', common_day)


    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('Most common hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    common_start_station = df['Start Station'].mode()[0]
    print('Most common start station: ', common_start_station)


    common_end_station = df['End Station'].mode()[0]
    print('Most common end station: ', common_end_station)


    df['Combo Start/End'] = (df['Start Station'] + ' + ' + df['End Station'])
    common_combo_station = df['Combo Start/End'].mode()[0]
    print('Most common combination of station: ', common_combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_travel_time = df['Trip Duration'].sum()
    total_hours = int(total_travel_time // 3600)
    total_minutes = int((total_travel_time - (total_hours * 3600)) // 60)
    total_seconds = int(total_travel_time - (total_hours * 3600) - (total_minutes * 60))
    print('Total time traveled: {} hours, {} minutes, {} seconds'.format(total_hours, total_minutes, total_seconds))


    mean_travel_time = df['Trip Duration'].mean()
    mean_minutes = int(mean_travel_time // 60)
    mean_seconds = int(mean_travel_time % 60)
    print('Average travel time: {} minutes, {} seconds'.format(mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_types = df['User Type'].value_counts()
    print('User types:\n',user_types)


    try:
        gender_count = df['Gender'].value_counts()
        print('\nGenders:\n',gender_count)
    except:
        print('This file does not have gender data')


    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest birth year: ', earliest_year)
        print('Most recent birth year: ', recent_year)
        print('Most common birth year: ', common_year)
    except:
        print('This file does not have birth year data')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays as many rows of data as the user requests, 5 rows at a time."""

    view_data = str(input('Would you like to see 5 rows of raw trip data? Enter yes or no: ').lower())
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc : (start_loc + 5)])
        start_loc +=5
        view_data = str(input('Would you like to see the next 5 rows of data? Enter yes or no: ').lower())



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
