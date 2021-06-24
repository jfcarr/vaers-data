#!/usr/bin/python3

import pandas as pd

def drop_na(input_name):
	'''
	Remove rows where the column is NaN.
	'''
	df.dropna(subset=[input_name], inplace = True)

def convert_julian(df, input_name, output_name):
	'''
	Convert date from MM/DD/YYYY string format to a Julian date.
	'''
	drop_na(input_name)

	df[output_name] = pd.DatetimeIndex(df[input_name]).floor('d').to_julian_date()

if __name__ == '__main__':
	df = pd.read_csv('data_sets/2021VAERSDATA.csv')

	# Only numeric values can be correlated, so dates must be Julian
	convert_julian(df, 'RECVDATE','RECVDATE_JUL')
	convert_julian(df, 'VAX_DATE','VAX_DATE_JUL')
	convert_julian(df, 'ONSET_DATE','ONSET_DATE_JUL')
	convert_julian(df, 'TODAYS_DATE','TODAYS_DATE_JUL')

	# Generate information about the dataset.
	print(df.info())

	# Data Correlation -> relationships between columns
	print("---")
	print("All correlations:")
	print(df.corr())

	print("---")
	print("Strong correlations:")
	print(f"\tCorrelation between AGE_YRS and CAGE_YR: {df['AGE_YRS'].corr(df['CAGE_YR'])}")
	print(f"\tCorrelation between RECVDATE_JUL and VAERS_ID: {df['RECVDATE_JUL'].corr(df['VAERS_ID'])}")
	print(f"\tCorrelation between VAX_DATE_JUL and NUMDAYS: {df['VAX_DATE_JUL'].corr(df['NUMDAYS'])}")