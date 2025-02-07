import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And I am Loving it')
st.write('This is a normal text')

st.markdown('''
            ### My facourite movies
            - Race 3
            - Humshakals
            - Housefull 
            '''
)

st.code("""
        def foo(input):
            return foo ** 2
            
        x = foo(3)
        
        """)

st.latex('x^2 + y^2 + 2 = 0')

df = pd.DataFrame({
    'Name': ['John', 'Smith', 'Paul'],
    'Marks': [23, 45, 32],
    'Package': [3.4, 5.6, 7.8]
})

st.dataframe(df)

st.metric(label='Total Revenue', value='$100,000', delta='$10,000')

st.json({
    'Name': ['John', 'Smith', 'Paul'],
    'Marks': [23, 45, 32],
    'Package': [3.4, 5.6, 7.8]
})

st.image('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', width=200)


st.sidebar.title('This is a sidebar')

col1, col2, col3  = st.columns(3)

with col1:
    st.image('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', width=200)
    
with col2:
    st.image('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', width=200)
    
with col3:
    st.image('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', width=200)
    
    
st.error('Login failed')
st.success('Login successful')
st.info('This is an info message')
st.warning('This is a warning message')

bar = st.progress(0)

for i in range(1, 101):
    bar.progress(i)
    
email = st.text_input('Enter email')
age = st.number_input('Enter age')
st.date_input("Enter registration date")


    
email = st.text_input('Enter email')
password = st.text_input('Enter password', type='password')
gender = st.selectbox('Select gender', ['male', 'female', 'others'])



btn = st.button('Login')


# if the button is clicked
if btn:
    if email == 'rohit.bharti82@gmail.com' and password == '1234':
        #st.balloons()
        st.success('Login successful')
        st.write(gender)
    else:
        st.error('Login failed')