import numpy as np
import matplotlib as mp
import pandas as pd
import plotly as pty

fact_center = pd.read_csv('Data/cwurData.csv')
fact_times = pd.read_csv('Data/timesData.csv')
dim_school = pd.read_csv('Data/school_and_country_table.csv')
fact_shanghai = pd.read_csv('Data/shanghaiData.csv')
dim_attainment = pd.read_csv('Data/educational_attainment_supplementary_data.csv')
dim_expanditure = pd.read_csv('Data/education_expenditure_supplementary_data.csv')

