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
    #Creating columns
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age= st.text_input('Age')
    
    with col2:
        sex = st.text_input('Sex')
        
    with col3:    
        cp = st.text_input('Chest Pain types')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar >129 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electronicdiographic Results')
        
    with col2: 
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2: 
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal:0=normal; 1=fixed defect; 2=reversable defect')
        
    
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

    
    
    
    
    