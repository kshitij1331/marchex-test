import pandas as pd
import numpy as np
import re
import os
from os.path import exists

#Filename for CBD-1
import datetime as dt
import datetime as dt
date = dt.datetime.today() - dt.timedelta(days = 1)
file_name = f'{date.year}-{date.month}-{date.day }'
output_file_path = f'{file_name}.csv'

#Filename for CBD-2
date = dt.datetime.today() - dt.timedelta(days = 2)
file_to_remove = f'{date.year}-{date.month}-{date.day }'

remove_file=f'{file_to_remove}.csv'

if exists(remove_file)==True:
    os.remove(remove_file)


remove_file_downloaded_file=os. path. expanduser('~') + '/Downloads/Find and Reserve Booking Report.csv'

upload_file=os. path. expanduser('~') + '/home/ubuntu/Find and Reserve Booking Report.csv'
#'/Users/jiveshdhakate/Downloads/Find and Reserve Booking Report.xlsx'

# Load the Excel file into Dataframe
# df = pd.read_excel(upload_file,skiprows=11,dtype='string')
# df = df.iloc[:, 1:]  # Remove the first column

# Load the CSV file into Dataframe
df = pd.read_csv(upload_file,dtype='string')
df = df.iloc[:, 0:]  # Remove the first column



# Function to remove special characters from a specific column
# def remove_special_characters(text):
#     pattern = r'[a-zA-Z-\'"$\[\]{}(),%@*,;<>#+_!?/]'  # Add more special characters within the square brackets if needed
#     cleaned_text = re.sub(pattern, '', str(text))
#     return cleaned_text

def remove_special_characters(text):
    def is_float(string):
      try:
          float(string)
          return True
      except ValueError:
          return False
          
    pattern = r'[a-zA-Z-\'"$\[\]{}(),%@*,;<>#+_!?/]'  # Add more special characters within the square brackets if needed
    cleaned_text = re.sub(pattern, '', str(text))
    
    if cleaned_text=='':
      return cleaned_text
    elif cleaned_text.isnumeric():
        return cleaned_text
    elif is_float(cleaned_text):
      return cleaned_text
    else:
      print('Error ' + text)
      exit(0)

df['CustomerPhoneNumber'] = df['CustomerPhoneNumber'].astype('str')
df['CustomerPhoneNumber'] = df['CustomerPhoneNumber'].apply(remove_special_characters)

df['ConversionID'] = df['ConversionID'].astype('str')
df['ConversionID'] = df['ConversionID'].apply(remove_special_characters)

df['TotalSale'] = df['TotalSale'].apply(remove_special_characters)
df['Nightly_Rate'] = df['Nightly_Rate'].apply(remove_special_characters)

# #Change Departure_Date
# # current_date_format = '%m/%d/%Y'
# # required_date_format = '%d/%m/%Y'

df['Departure_Date'] = pd.to_datetime(df['Departure_Date']).dt.strftime('%m/%d/%Y')
df['Arrival_Date'] = pd.to_datetime(df['Arrival_Date']).dt.strftime('%m/%d/%Y')

#Change ConversionTimestamp
# current_timestamp_format = '%m/%d/%Y %H:%M:%S'
# required_timestamp_format = '%d/%m/%Y %H:%M:%S'
df['ConversionTimestamp'] = pd.to_datetime(df['ConversionTimestamp']).dt.strftime('%m/%d/%Y %H:%M:%S')


df=df.replace('NA', '')


df.dropna(how = 'all').to_csv(output_file_path, index=False)

if exists(remove_file_downloaded_file)==True:
	os.remove(remove_file_downloaded_file)
