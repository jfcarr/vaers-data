# vaers-data

How to load [Vaccine Adverse Event Reporting System (VAERS)](https://vaers.hhs.gov/) data into SQLite and pandas, for analysis.

This repo includes VAERS data, symptom information, and vaccine information files in .csv files, downloaded from the VAERS website.  Use the [download link](https://vaers.hhs.gov/data/datasets.html) if you'd like to obtain updated versions.

## Prerequisites

* Linux
* SQLite3
* Python 3
* pandas library.  (Install with: `pip3 install pandas`)

## Steps

### Extract the source data sets

```bash
make extract
```
### Load a SQLite database with VAERS data

```bash
make create
```

This will create a SQLite database named vaers.db, and load it with VAERS data.  Schema information is in docs/data_dictionary.md.

The source script is [sql_scripts/create_and_load_tables.sql](sql_scripts/create_and_load_tables.sql)

**Warning:** If a vaers.db file already exists, it will be emptied and reloaded.

### Example query

Execute a simple query against the new database:

```bash
make sql1
```

This will find COVID19 vaccination records for males 50 years old, in Ohio, who were hospitalized:

STATE | CAGE_YR | SEX | HOSPITAL | HOSPDAYS | VAX_DATE | VAX_TYPE | VAX_MANU | VAX_LOT
----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | -----
OH | 50 | M | Y | | 2021-03-19 | COVID19 | PFIZER\BIONTECH | EN6202    
OH | 50 | M | Y | 2 | 2021-04-08 | COVID19 | MODERNA | 039B21A

The source script is [sql_scripts/example_cov19_M_50yr_OH_hosp.sql](sql_scripts/example_cov19_M_50yr_OH_hosp.sql)

### pandas

The SQLite database can be used as a data source for the pandas data analysis library.

Load COVID19 vaccination data into a pandas dataframe, print a summary of the dataframe, and calculate the correlation between reported age and calculated age:

```bash
make db1
```

The source script is [panda_corr_db.py](panda_corr_db.py)

Results:

```
       STATE  AGE_YRS  CAGE_YR CAGE_MO SEX
0         TX     33.0       33           F
1         CA     73.0       73           F
2         WA     23.0       23           F
3         WA     58.0       58           F
4         TX     47.0       47           F
...      ...      ...      ...     ...  ..
305945    CA     16.0       16           M
305946    IL     16.0       16           F
305947    CA     16.0       16           F
305948    MA     32.0       32           F
305949    TX     14.0       14           M

[305950 rows x 5 columns]
Correlation between AGE_YRS and CAGE_YR: 0.9929779152633482
```

The correlation between reported age (AGE_YRS) and calculated age (CAGE_YR) is very strong, as expected.

You can also load the data directly from the source CSV, and calculate correlations:

```bash
make csv1
```
