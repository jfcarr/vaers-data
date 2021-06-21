#!/usr/bin/python3

import pandas as pd
import sqlite3

conn = sqlite3.connect('vaers.db')
query = "SELECT D.STATE,D.AGE_YRS,D.CAGE_YR,D.CAGE_MO,D.SEX FROM VData AS D INNER JOIN Vaccines AS V ON V.VAERS_ID = D.VAERS_ID WHERE V.VAX_TYPE = 'COVID19' AND NOT D.AGE_YRS = '' AND NOT D.CAGE_YR = '';"

df = pd.read_sql_query(query,conn)

print(df)

print(f"Correlation between AGE_YRS and CAGE_YR: {df['AGE_YRS'].astype(float).corr(df['CAGE_YR'].astype(float))}")
