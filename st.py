## streamlit
#pip install streamlit
## python lib
## webpages for ml and data sci projects
#html and css no requirement
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import time

##page configuration
st.set_page_config(
    page_title="streamlit function demo",
    page_icon="😍",
    layout="centered"
)
##title and text elements
st.title("Jai Ji Nendra")
st.header("1. Text elements")
st.subheader("markdown, code, latex")
st.markdown("**bold text**,*italic text*,`code`text")
st.code("print('hello everyone')",language = "python")
st.latex(r"a^2+b^2=c^2")

st.divider()

## metrices and messages
st.header("2. metrices and messages")
st.metric(label = "Revenue", value = 1234, delta = "+10%", delta_color="inverse")
st.error("this is an error message")
st.warning("this is a warning message ")
st.info("this is an info message ")
st.success("this is a success message")
st.exception(ValueError("this is an exception message"))

st.divider()

## data display
st.header("3. data display")
df=pd.DataFrame(np.random.randn(10,2),columns =["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict)
st.divider()

#charts
st.header("4.Charts")
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()

##widgets
st.header("5. widgets")
with st.form("Input form"):
    name = st.text_input("Enter your name", type = "password")
    age = st.number_input("Enter your age")
    mood = st.radio("Select your mood",("happy","sad","neural"))
    language = st.multiselect("Select your language",("English","French","Hindi"))
    submit = st.form_submit_button("submit")
    if submit:
        st.success(f"Name : {name}, Age : {int(age)}, Mood : {mood}, Language : {language}")



col1 , col2 , col3 = st.columns([4,1,1])
with col1:
    st.text_input("Enter your name")
    st.number_input("Enter your age")
with col2:    
    st.radio("Select your mood",("happy","sad","neural"))
    st.multiselect("Select your language",("English","French","Hindi"))
    
with col3: 
    st.title("Output") 
    
    ## we can                   
#file handling divide from into multiple columns
## for that first define form then define columns
#with st.form("Input form"):
    # col1 , col2, col3
    # name = st.text_input("Enter your name", type = "password")
    # age = st.number_input("Enter your age")
    # mood = st.radio("Select your mood",("happy","sad","neural"))
    # language = st.multiselect("Select your language",("English","French","Hindi"))
    # submit = st.form_submit_button("submit")
    # if submit:
    #     st.success(f"Name : {name}, Age : {int(age)}, Mood : {mood}, Language : {language}")



col1, col2 = st.columns(2)
with col1:
    number = st.slider ("Select a number",0,10)
with col2:
    colour = st.color_picker("Select the colour")
    

st.text_area("Enter your message")
st.date_input("Select a date")
st.time_input("Select a time")
st.file_uploader("Upload a file")
st.divider()
##media
st.header("6. media")
st.image("https://pin.it/JbjUFKKh6")
st.video(r"c:\Users\HP\Downloads\Telegram Desktop\Gangubai  Kathiawadi 2022.mp4")
st.audio(r"d:\bhajans\yeh_to_prem_ki_baat_hai.mp3")    



##sidebar and layout
st.sidebar.header("sidebar header")
st.sidebar.write("This is a sidebar text")
st.sidebar.button("click me")
option = st.sidebar.selectbox("select an option",("option 1","option 2","option 3"))

with st.container():
    st.write("this is a container")
    
with st.expander("expand header"):
    st.write("this is a expander")
    
with st.spinner("Loading data..."):
    time.sleep(10)
  # st.success("data loaded")
st.toast("toast message",icon="🎂")
  
st.markdown('[🤞 Streamlit Website](https://streamlit.io)', unsafe_allow_html=True)

  
##generator and deco
##multithreading and multiprocessing
##Overloading and overriding
