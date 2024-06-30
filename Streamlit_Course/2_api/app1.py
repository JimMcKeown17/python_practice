import streamlit as st
import pandas as pd
import numpy as np
import os

data = pd.read_csv('tips.csv')

def display_data_random(df):
    sample = df.sample(5)
    return sample

# button widget
st.subheader('Displaying Random 5 Rows')
st.caption('click below to display')
button = st.button('Display Random 5 Rows')
if button:
    sample = display_data_random(data)
    st.dataframe(sample)

# Checkbox
st.markdown('---')
st.subheader('st.checkbox')
agree = st.checkbox('I agree to terms and conditions') #return boolean

st.write('checkbox status = ', agree)

## Multiple Checkbox
with st.container():
    st.info('What technologies do you know:')
    python = st.checkbox('Python')
    datascience = st.checkbox('Data Science')
    ai_ml = st.checkbox('AI/ML')
    android = st.checkbox('Android')
    react = st.checkbox('React JS')
    java = st.checkbox('Core Java')
    javascript = st.checkbox('JavaScript')
    tech_button = st.button('Submit')
    if tech_button:
        tech_dict = {
            'Python': python,
            'Data Science': datascience,
            'AI/ML': ai_ml,
            'Android': android,
            'React JS': react,
            'Core Java': java,
            'JavaScript': javascript
        }
        st.json(tech_dict)

