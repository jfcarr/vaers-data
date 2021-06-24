SQL_APP = sqlite3
PYTHON_APP = python3
DB_NAME = vaers.db

default:
	@echo 'Targets:'
	@echo '  extract -- Extract the source .csv files'
	@echo '  create  -- Create and load SQLite database'
	@echo '  sql1    -- Example SQL query for COVID 19 vaccinations, state of Ohio, male, 50 years old, with hospitalization'
	@echo '  db1     -- Load COVID19 vaccination data into a pandas dataframe, print a summary of the dataframe, and simple correlation'
	@echo '  csv1    -- Load directly from CSV, with simple correlations'

extract:
	unzip data_sets/data_sets.zip -d data_sets/

create:
	@echo 'Creating tables and loading data...'
	$(SQL_APP) $(DB_NAME) < sql_scripts/create_and_load_tables.sql
	@echo 'Finished'

sql1:
	$(SQL_APP) $(DB_NAME) < sql_scripts/example_cov19_M_50yr_OH_hosp.sql

db1:
	$(PYTHON_APP) panda_corr_db.py

csv1:
	$(PYTHON_APP) panda_corr_csv.py
