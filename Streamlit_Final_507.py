# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 01:09:14 2021

@author: Alejandro Herrera
"""
#Import packages

import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px

@st.cache
def load_hospitals():
   hospital_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
   return hospital_df

@st.cache
def load_inpatient():
    inpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')
    return inpatient_df

@st.cache
def load_outpatient():
    outpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')
    return outpatient_df

#FAKE LOADER BAR TO STIMULATE LOADING    
#my_bar = st.progress(0)
#for percent_complete in range(100):
#     time.sleep(0.1)
#     my_bar.progress(percent_complete + 1)

st.title('CMS - Hospital Data - Final Assignment')
st.title('HHA 507 - Final Assignment')
st.write('Alejandro Herrera:sunglasses:')

#st.text('For this assignment, we were tasked with doing perfoming an analysis for hospital infromation around the US.
#        For the first part, here are some transofrmation that were applied....')

add_selectbox = st.sidebar.selectbox(
    "Streamlit Owner @Alejandro Herrera Checkout:",
    ("GitHub", "LinkedIn", "WixResume")
)

#Buttons to reveal each datasets
hospital_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv')
st.header('These buttons reveal the datasets for Hospital Data, Inpatient Data, and Outpatient Data')
st.text('Click the button to reveal the Hospital Data')

result = st.button('Hospital Data')

if result:
    st.dataframe(hospital_df)

inpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv')

st.text('Click the button to reveal the Inpatient Data')

result = st.button('Inpatient Data')

if result:
    st.dataframe(inpatient_df)

outpatient_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv')

st.text('Click the button to reveal the Outpatient Data')

result = st.button('Outpatient Data')

if result:
    st.dataframe(outpatient_df)

##Create dataframe unique for Stony Brook University Hospital
SBU = hospital_df[hospital_df['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']
st.header('Stony Brook University Hospital')
st.markdown('This dataset shows information for Stony Brook University Hospital')
st.dataframe(SBU)

##Create dataframe unique for New York hospitals not including Stony Brook University Hospital
NY = hospital_df[hospital_df['state'] == 'NY']
st.header('Hospitals in New York')
st.markdown('This dataset shows hospitals located in New York, filtered out from the main hospital dataframe, excluding SBU hospital')
st.dataframe(NY)


#Answering the following questions
#Question1
table1 = NY['hospital_overall_rating'].value_counts().reset_index()
st.header("Q1: How does Stony Brook ratings compare to NYS hospitals?")
st.write('In this sections we\'ll see how teh ratings of these 2 hospitals are compared.')
st.write('Stony Brooks Overall rating is a 4 which is more than NYS in comparison')

result = st.button('Answer')
if result:
    st.dataframe(table1)

#SBU Filtered Inpatient
SBU_inpatient = inpatient_df[inpatient_df['provider_id']==330393]
st.header('Inpatient Data for Stony Brook')

#Question 2:
st.header('Inpatient DRGs Expense')
st.subheader('Q2. What is the most expensive inpatient DRGs code for Stony Brook University Hospital?')
st.subheader('Stony Brook Inpatient DRGs Pivot Table')
SBU_inpatient_DRGs_pivot = SBU_inpatient.pivot_table(index=['provider_id','provider_name','drg_definition'],values=['average_total_payments'])
SBU_inpatient_DRGs_desc = SBU_inpatient_DRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.markdown('The table reveals that the most expensive inpatient DRGs code for Stony Brook Univeristy Hospital is 003, with an average total payments of $21,667.00')
st.markdown('003 - ECMO OR TRACH W MV >96 HRS OR PDX EXC FACE, MOUTH & NECK W MAJ O.R.')

st.dataframe(SBU_inpatient_DRGs_desc)

#SBU Filtered Outpatient
SBU_outpatient = outpatient_df[outpatient_df['provider_id']==330393]
st.header('Outpatient Data for Stony Brook')
st.dataframe(SBU_outpatient)

#Question 3:
st.header('Outpatient DRGs Expense')
st.subheader('Q3. Whast is the most expensive outpatient DRGs code for Stony Brook Hospital?')
st.subheader('Outpatient Data for Stony Brook')
SBU_outpatient_DRGs_pivot = SBU_outpatient.pivot_table(index=['provider_id','provider_name','apc'],values=['average_total_payments'])
SBU_outpatient_DRGs_desc = SBU_outpatient_DRGs_pivot.sort_values(['average_total_payments'], ascending=False)
st.markdown('APCs is ambulatory payment classsifications, a classification system for outpatient services')
st.markdown('Table determines that the most expensive outpatient APCs code for Stony Brook Univeristy Hospital is 0074, with an average total payments of $2,307.21')
st.markdown('0074 - Level IV Endoscopy Upper Airway')
st.dataframe(SBU_outpatient_DRGs_desc)

#Question 4:
st.header ('Types of hospitals')
st.subheader('Q4. How many types of hospitals are there in NY?')
st.subheader('Here are the most common types of Hospitals in the US')
st.subheader('PIE Chart:')
hospital_type = hospital_df['hospital_type'].value_counts().reset_index()
fig = px.pie(hospital_type, values='hospital_type', names='index')
st.plotly_chart(fig)

