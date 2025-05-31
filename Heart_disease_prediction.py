# -*- coding: utf-8 -*-
"""
Heart Disease Prediction Model
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the model

heart_disease_model= pickle.load(open('heart_disease_model.sav','rb'))


#sidebar for navigator

with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                           ['Heart Disease Prediction'],
                           icons=['heart-pulse-fill'])
    
    
# heart Disease pred page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using Ml')
    
    #Getting input from user
    # page title
    st.title('Heart Disease Prediction using Ml')
    age= st.text_input('Age')
    sex = st.text_input('Sex  ( 0 = Female || 1 = Male )')
    cp = st.text_input('Chest Pain types  ( 0 = Typical angina || 1 = Atypical || 2 = Non-anginal || 3 = Asymptomatic)')
    trestbps = st.text_input('Resting Blood Pressure ( Range = 94 – 200 mm Hg )')
    chol = st.text_input('Serum Cholestrol in mg/dl ( Range = 126 – 564 mg/dl )')
    fbs = st.text_input('Fasting Blood Sugar >120 mg/dl ( 0 = No || 1 = Yes )')
    restecg = st.text_input('Resting Electronicdiographic Results ( 0 = Normal || 1 = ST-T abnormality || 2 = Left ventricular hypertrophy)')
    thalach = st.text_input('Maximum Heart Rate achieved ( 71 – 202 bpm )')
    exang = st.text_input('Exercise Induced Angina ( 0 = No || 1 = Yes )')
    oldpeak = st.text_input('ST depression induced by exercise ( Range = 0.0 – 6.2 )')
    slope = st.text_input('Slope of the peak exercise ST segment ( 0 = Upsloping || 1 = Flat || 2 = Downsloping )')
    ca = st.text_input('Major vessels colored by flourosopy ( Range = 0 – 3 )')
    thal = st.text_input('Blood disorder type  ( 1 = Normal || 2 = Fixed defect || 3 = Reversible defect )')
        
    
    #code for prediction 
    heart_diagnosis = ''    
    
    # creating Button for result 
    
    if st.button('Heart Disease Test Result'):
        try:
            # Ensure all inputs are converted to float
            input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol),float(fbs), float(restecg), float(thalach), float(exang),float(oldpeak), float(slope), float(ca), float(thal)]

            # Predict
            heart_prediction = heart_disease_model.predict([input_data])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person has Heart Disease'
            else:
                heart_diagnosis = 'The person does not have Heart Disease'
                
            st.success(heart_diagnosis)
        except ValueError:
            st.error("Please make sure all inputs are valid numbers.")

    
    
    
    
    
