Source: https://vaers.hhs.gov/docs/VAERSDataUseGuide_November2020.pdf

# VData (source file: 2021VAERSDATA.csv)

Name | SQLite Data Type | Description
---------|----------|---------
VAERS_ID | TEXT | A sequentially assigned number used for identification purposes.  It serves as a link between the three data files.
RECVDATE | TEXT (_Date_) | The date the VAERS form information was received to our processing center.
STATE | TEXT | The two-letter US Postal Service abbreviation for the home state of the vaccinee. Please note that all foreign reports are contained in a separate data file.
AGE_YRS | REAL | The recorded vaccine recipient's age in years.
CAGE_YR | INTEGER | Age of patient in years calculated by (vax_date-birthdate).
CAGE_MO | REAL | Age of patient in months calculated by (vax_date-birthdate). The values for this variable range from 0 to <1.  It is only calculated for patients age 2 years or less. The summation of the two variables CAGE_YR and CAGE_MO provide the calculated age of a person. For example, if CAGE_YR=1 and CAGE_MO=.5 then the age of the individual is 1.5 years or 1 year 6 months.
SEX | TEXT | Sex of the vaccine recipient (M = Male, F = Female, Unknown = Blank).
RPT_DATE | TEXT (_Date_) | Date the VAERS form was completed by the reporter as recorded on the specified field of the form.  This is a VAERS 1 form field only.
SYMPTOM_TEXT | TEXT | This is the symptom text recorded in the form.  MedDRA Terms are derived from this text and placed in the VAERSSYMPTOMS file.
DIED | TEXT | If the vaccine recipient died a "Y" is used; otherwise the field will be blank.
DATEDIED | TEXT (_Date_) | If the vaccine recipient died there is space in this field to record the date of death; otherwise the field will be blank.
L_THREAT | TEXT | If the vaccine recipient had a life-threatening event associated with the vaccination a "Y" is placed is used; otherwise the field will be blank.
ER_VISIT | TEXT | If the vaccine recipient required an emergency room or doctor visit a "Y" is placed in this field; otherwise the field will be blank.  If this is the only option checked the report is not considered serious. This is a VAERS 1 form field only.
HOSPITAL | TEXT | If  the  vaccine  recipient  was  hospitalized  as  a result of the vaccination a "Y" is used; otherwise the field will be blank.
HOSPDAYS | INTEGER | If the reporter checked that the vaccine recipient was hospitalized a space is provided in this field to record the number of days hospitalized; otherwise the field will be blank.
X_STAY | TEXT | If a patient's hospitalization is prolonged as a result of the adverse event associated with the vaccination a "Y" will be placed in this field; otherwise the field will be blank.
DISABLE | TEXT | If the vaccine recipient was disabled as a result of the vaccination a "Y" is placed in this field; otherwise the field will be blank.
RECOVD | TEXT | A "Y" is placed in the field if the vaccine recipient recovered from the adverse event.  "N" indicates that the vaccinee has not recovered from the adverse event.  "U" or blank indicates that the vaccine recipient's recovery status is unknown.
VAX_DATE | TEXT (_Date_) | The date of vaccination as recorded in the specified field of the form.
ONSET_DATE | TEXT (_Date_) | The date of the onset of adverse event symptoms associated with the vaccination as recorded in the specified field of the form.
NUMDAYS | INTEGER | The calculated interval (in days) from the vaccination date to the onset date.
LAB_DATA | TEXT | This text field contains narrative about any relevant diagnostic tests or laboratory results as recorded on the specified field of the form.
V_ADMINBY | TEXT | The reporter may note on the VAERS form the type of facility administering the vaccine.  The options are different depending on the form version; additional options were added on the VAERS 2 form.
V_FUNDBY | TEXT | This is a VAERS 1 field only. The reporter may note in Box 16 on the VAERS form which type of funds were used to purchase the vaccines administered in Box 13 (PUB=Public, PVT=Private, MIL=Military; OTH=Other/Unknown).
OTHER_MEDS | TEXT | This text field contains narrative about any prescription or non-prescription drugs the vaccine recipient was taking at the time of vaccination as recorded on the specified field of the form.
CUR_ILL | TEXT | This text field contains narrative about any illnesses at the time of the vaccination as noted on the specified field of the form.
HISTORY | TEXT | This text field contains narrative about any pre-existing physician-diagnosed birth defects or medical condition that existed at the time of vaccination as noted on the specified field of the form. For the VAERS 1 form, this field also includes pre-existing physician-diagnosed allergies. 
PRIOR_VAX | TEXT | This field provides prior vaccination event information as recorded on the specified field of the form.
SPLTTYPE | TEXT | Manufacturer number or Immunization Project number as recorded on the specified field of the form.
FORM_VERS | INTEGER | VAERS form version 1 or 2.
TODAYS_DATE | TEXT (_Date_) | Date form was completed.
BIRTH_DEFECT | TEXT | If the vaccine recipient had a congenital anomaly or birth defect associated with the vaccination, a "Y" is used; otherwise the field will be blank. This is a VAERS 2 form field only.
OFC_VISIT | TEXT | If the vaccine recipient had a doctor or other healthcare professional office/clinic visit associated with the vaccination a "Y" is used; otherwise the field will be blank. This is a VAERS 2 form field only.
ER_ED_VISIT | TEXT | If the vaccine recipient had an emergency room/department or urgent care visit associated with the vaccination a "Y" is used; otherwise the field will be blank. This is a VAERS 2 form field only.
ALLERGIES | TEXT | This text field contains narrative about any pre-existing physician-diagnosed allergies that existed at the time of vaccination as noted in the specified field of the form. This is a VAERS 2 form field only.

# Symptoms (source file: 2021VAERSSYMPTOMS.csv)

Name | SQLite Data Type | Description
---------|----------|---------
VAERS_ID | INTEGER | A sequentially assigned number used for identification purposes. It serves as a link between the three data files.
SYMPTOM1 | TEXT | **MedDRA Term (SYMPTOM1-5):** The data in these fields are equivalent to the PT TERM from the MedDRA codebook. MedDRA terms are extracted from the narrative text in VAERS 2 (Item 18 and 19) and VAERS 1 (Box 7 and 12). Duplicates may appear in data and terms are listed in alphabetical order.  In case a report has more than 5 terms multiple rows with 5 terms each will be listed for that VAERS ID. 
SYMPTOMVERSION1 | REAL | **MedDRA Term Version (SYMPTOMVERSION1-5):** Version of MedDRA dictionary from which the MedDRA term was first created.
SYMPTOM2 | TEXT | 
SYMPTOMVERSION2 | REAL | 
SYMPTOM3 | TEXT | 
SYMPTOMVERSION3 | REAL | 
SYMPTOM4 | TEXT | 
SYMPTOMVERSION4 | REAL | 
SYMPTOM5 | TEXT | 
SYMPTOMVERSION5 | REAL | 

# Vaccines (source file: 2021VAERSVAX.csv)

Name | SQLite Data Type | Description
---------|----------|---------
VAERS_ID | INTEGER | A sequentially assigned number used for identification purposes. It serves as a link between the three data files.
VAX_TYPE | TEXT | The data list the vaccines group name by code. Similar vaccines are grouped together (e.g., FLU, DTAP).
VAX_MANU | TEXT | This field identifies the manufacturer of each of the vaccines listed.
VAX_LOT | TEXT | This field identifies the lot number of the vaccines listed.
VAX_DOSE_SERIES | TEXT | This field identifies the vaccine dose of the recorded vaccines listed. The VAERS 1 field VAX_DOSE was discontinued in the VAERS 2 form; when a value exists, a 1 is added to equate to the VAX_DOSE_SERIES field. 
VAX_ROUTE | TEXT | This field identifies the vaccine route of administration.
VAX_SITE | TEXT | This field identifies the anatomic site where the vaccination was administered.
VAX_NAME | TEXT | This field provides the brand name of the vaccine administered.
