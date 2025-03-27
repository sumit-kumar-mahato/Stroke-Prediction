# -*- coding: utf-8 -*-
"""stroke_prediction_streamlit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1scjgHaYiHSCfxcyVdOehw-HV6a_IlQrw
"""

!pip install streamlit-option-menu

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

stroke_prediction_model = pickle.load(open('stroke_prediction_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:

    selected = option_menu('Stroke Prediction System',

                          ['Stroke Prediction'],
                          icons=['activity'],
                          default_index=0)

# Diabetes Prediction Page
if (selected == 'Stroke Prediction'):

    # page title
    st.title('Stroke Prediction using ML')


    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        gender = st.text_input('Gender')

    with col3:
        bmi = st.text_input('BMI')

    with col1:
        residence_type = st.text_input('Residence_Type')


    # code for Prediction
    stroke_diagnosis = ''

    # creating a button for Prediction

    if st.button('Stroke Test Result'):
        stroke_prediction = stroke_prediction_model.predict([[age, gender, bmi, residence_type]])

        if (stroke_prediction[0] == 1):
          stroke_diagnosis = 'The person is diabetic'
        else:
          stroke_diagnosis = 'The person is not diabetic'

    st.success(stroke_diagnosis)

