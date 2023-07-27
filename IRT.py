
import pandas as pd
import streamlit as st
from PIL import Image
import random

#st.set_page_config(page_title='IRT-MODEL',page_icon = Image.open('./static/images/s-irt.jpeg'),layout = "wide")
#st.sidebar.image('./static/images/adapt.jpg')


with st.sidebar.expander("About this App"):
     st.write("""This App is build for K 12-Computerized Adaptive Testing""")
with st.sidebar.expander("Upload Question Dataset here", True):
    uploaded_file = st.file_uploader("Upload input CSV file here", type=["csv"])
        
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        hard_que = df.loc[df['Type']== 'D']
        mid_que = df.loc[df['Type']== 'M']
        easy_que = df.loc[df['Type']== 'E']
        
        easy_que_list = easy_que['ID'].to_list()
    
        mid_que_list = mid_que['ID'].to_list()
    
        hard_que_list = hard_que['ID'].to_list()
        
    else:
        st.info('Awaiting for CSV file to be uploaded.')

    
#Add the title for this App
st.markdown(""" <style> .font {
    font-size:40px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p {text-align: center;} class="font">Computerized Adaptive Testing</p>', unsafe_allow_html=True)

st.markdown(
        """
    - 🗂️ Read the Question carefully and Answer it from available options
    - ⚙️  This is a Computerized Adaptive Testing with Easy, Medium And Difficulty Level Question
    - 📉 Answer all Questions
    - 🩺 There is no negative Marking
    -----
    """
    )



def IRT(df):
    type_of_question = 'E'
    response_list = ['A','B', 'C', 'D']
    count = 0
    score= 0 
    while count < 50 :
        if type_of_question == 'E' : 
            if len(easy_que_list)==0:
                #st.write("you have attempted all Easy Questions")
                #st.write('*************************************')
                type_of_question = 'M'
                continue
            que_to_ask_id =  random.choice(easy_que_list)   
            st.write("Question-No.",que_to_ask_id)
            que_row = df.loc[df['ID']== que_to_ask_id]     
            que_dict = que_row.to_dict(orient='records')  
            col1,col2=st.columns(2)  
            st.write()
            with col1:
                st.write("Q. ",que_dict[0]['Question'])
                option_A = st.write("A: ",que_dict[0]['A'])
                option_B = st.write("B: ",que_dict[0]['B'])
                option_C = st.write("C: ",que_dict[0]['C'])
                option_D = st.write("D: ",que_dict[0]['D'])
                st.write()
                #st.write(len(easy_que_list),'Easy Question Remaining')


            with col2: 
                st.write('Item Difficulty= ',que_dict[0]['Difficulty'])
                st.write('Item Discrimination= ',que_dict[0]['Discrimination'])
                st.write('Marks allotted:', que_dict[0]['Marks'])
            st.write()
            ans1 = input('please provide your answer:- ')
            #ans1= random.choice(response_list)
            if ans1 == que_dict[0]['Answer']:      
                score += 1
                st.success('its correct')
                st.write()
                type_of_question ='M'                   
            else:
                type_of_question ='E'
                st.error('incorrect :(')
                st.write()
            
            easy_que_list.remove(que_to_ask_id)

        
        
        elif type_of_question == 'M' : 
            st.write()
            if len(mid_que_list)==0:
                #st.write("you have attempted all Mid Questions")
                #st.write('*************************************')
                type_of_question = 'D'
                continue
            que_to_ask_id =  random.choice(mid_que_list)
            st.write("Question-No.",que_to_ask_id)

            que_row = df.loc[df['ID']== que_to_ask_id]

            que_dict = que_row.to_dict(orient='records')
            col1,col2=st.columns(2)  
            st.write()
            with col1:
                st.write("Q. ",que_dict[0]['Question'])
                option_A = st.write("A: ",que_dict[0]['A'])
                option_B = st.write("B: ",que_dict[0]['B'])
                option_C = st.write("C: ",que_dict[0]['C'])
                option_D = st.write("D: ",que_dict[0]['D'])
                st.write()
                #st.write(len(mid_que_list),'Medium-Level Question Remaining')

            with col2: 
                st.write('Item Difficulty= ',que_dict[0]['Difficulty'])
                st.write('Item Discrimination= ',que_dict[0]['Discrimination'])
                st.write('Marks allotted:', que_dict[0]['Marks'])
            st.write()
            ans = input('please provide your answer:- ')
            #ans= random.choice(response_list)

            if ans == que_dict[0]['Answer']:
                score += 1
                st.success('its correct')
                st.write()
                type_of_question ='D'
            else:
                type_of_question ='E'
                st.error('incorrect :(')
                st.write()
            mid_que_list.remove(que_to_ask_id)
        
  
        elif type_of_question == 'D' : 
            st.write()
            if len(hard_que_list)==0:
                #st.write("you have attempted all Diff Questions")
                #st.write('*************************************')
                type_of_question = 'E'
                continue

            que_to_ask_id =  random.choice(hard_que_list)
            st.write("Question-No.",que_to_ask_id)

            que_row = df.loc[df['ID']== que_to_ask_id]

            que_dict = que_row.to_dict(orient='records')
            col1,col2=st.columns(2)  
            st.write()
            with col1:
                st.write("Q. ", que_dict[0]['Question'])
                option_A = st.write("A: ",que_dict[0]['A'])
                option_B = st.write("B: ",que_dict[0]['B'])
                option_C = st.write("C: ",que_dict[0]['C'])
                option_D = st.write("D: ",que_dict[0]['D'])
                st.write()
                #st.write(len(hard_que_list),'Difficulty-Level Question Remaining')


                #submitbutton
            with col2: 
                st.write('Item Difficulty= ',que_dict[0]['Difficulty'])
                st.write('Item Discrimination= ',que_dict[0]['Discrimination'])
                st.write('Marks allotted:', que_dict[0]['Marks'])
            st.write()
            ans2 = input('please provide your answer:- ')
            #ans2= random.choice(response_list)

            if ans2 == que_dict[0]['Answer']:
                score += 1
                st.success('its correct')
                st.write()
                type_of_question ='D'
            else:
                type_of_question ='M'
                st.error('incorrect :(')
                st.write()
            hard_que_list.remove(que_to_ask_id)
        count +=1
        #st.write('you have attempted', count)
        # if count == 50:
        #     break   
        

    st.write("your score: ", score)
    st.write("you have attempted: ", count)

if uploaded_file is not None:

    IRT(df) 
                              
st.markdown(
        """<hr <footer >© Copyright 2022,Extramarks Education India Pvt Ltd</footer> """,
        unsafe_allow_html=True) 
  
with st.sidebar:
    st.markdown(
        """<hr <footer >Work Under Progress</footer> """, unsafe_allow_html=True)

























