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
my_bar = st.progress(0)
for percent_complete in range(100):
     time.sleep(0.1)
     my_bar.progress(percent_complete + 1)