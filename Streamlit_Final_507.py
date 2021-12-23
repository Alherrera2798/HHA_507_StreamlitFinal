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
table1 = NY['hospital_overall_rating'].value_counts().reset_index()
st.header("Q1: How does Stony Brook ratings compare to NYS hospitals?")
st.write('In this sections we\'ll see how teh ratings of these 2 hospitals are compared.')
st.write('Stony Brooks Overall rating is a 4 which is more than NYS in comparison')
st.dataframe(table1)
