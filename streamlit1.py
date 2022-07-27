import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Simple App with Streamlit')
st.header('Welcome')
st.subheader('This is a subheader')
st.markdown('This is markdown')

st.write('''
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
''')

st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.checkbox('I agree to the rules')
st.write('''
st.checkbox(): This function returns a Boolean value. 
When the box is checked, it returns a True value, otherwise a False value.''')

st.button('button')
st.write('This function is used to display a radio button widget.')

st.radio('radio',['Male','Female'])

st.multiselect('multiselect',['Low','Medium', 'High'])
st.selectbox('select_box',['Male','Female'])
st.select_slider('select_slider', ['A', 'B', 'C'])
st.slider('slider', 0, 100)

st.write('text_input')
st.text_input('Enter text')


num1 = st.number_input('Enter first number')
num2 = st.number_input('Enter second number')

button = st.button('Add')
if button == True:
    st.write(num1 + num2)

text = st.text_area('Text Area')
st.write(text)

st.file_uploader('Upload a photo')
st.color_picker('color_picker')

st.button('Complete')