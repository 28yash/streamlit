import streamlit as st

#Title
st.title('Title -> hello world')

#Header
st.header('Header -> hello world')

#SubHeader
st.subheader('SubHeader -> hello world')

st.write('-'*20)

#Text
st.subheader('Text')
st.text('Text -> hello world')

#MarkDown
st.subheader('MarkDown')
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')
st.markdown('Hi')

st.subheader('Messages')
#Success
st.success('data is submitted')
#Info
st.info('Information')
#Warning
st.warning('Warning')
#Error
st.error('Error')
#Exception error
exp = ZeroDivisionError('Division not possible with 0')
st.exception(exp)

#Help / Documentation of the error
st.subheader('Help')
st.help(ZeroDivisionError)

#Write
st.subheader('Write')
st.write('range(1,10)')
st.write(range(1,10))

#Code
st.subheader('Code')
st.code('x=20 \n'
        'for i in range(x): \n'
        '   print(i)')

#Checkbox
st.subheader('Checkbox')
st.checkbox('Male')

#Checkbox with validation
st.subheader('Checkbox with validation')
if(st.checkbox('Adult')):
    st.write('You are 18+')
    
#RadioButton
st.subheader('RadioButton')
radioButton = st.radio('Select: ',('Male','Female' ,'Other'))
if(radioButton=='Male'):
    st.write('You are a Male')
elif(radioButton=='Female'):
    st.write('You are a Female')
else:
    st.write('You are Other')

#SelectBox
st.subheader('Select Box')
selectBox= st.selectbox("Class: " , ['A','B','C','D','E'])
st.write('You have selected class:',selectBox)

#MultiSelect box
st.subheader('MultiSelect box')
multiSelectBox= st.multiselect("Class: " , ['A','B','C','D','E'])
st.write('You have selected: ',len(multiSelectBox),'options', multiSelectBox)

#Button
st.subheader('Button')
if(st.button('Click here')):
    st.write("Thanks for clicking")

#Slider
st.subheader('Slider')
vol = st.slider('Select the Volume',1,100,step=1)
st.write('The volume is',vol)

#Input_Text
st.subheader('Text Input')
name = st.text_input('Enter username:')
password = st.text_input('Enter password:',type='password') 
if(name):
    st.write('Hii,',name)

#Input Text Area
st.subheader('Text Area')
st.text_area('Write about yourself in 50 words:')

#Input number
st.subheader('Number input')
st.number_input("Select age: ",18,50)

#Input date
st.subheader('Date input')
st.date_input('Select date:')

#Input time
st.subheader('Time input')
st.time_input('Select Time:')
