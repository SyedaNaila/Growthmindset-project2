#Streamlit
#Import
import streamlit as st
st.set_page_config(page_title= "Growth mindset project" , project_icon="🌙")
st.title("Growth Mindset AI Project: Web App With streamlit")

st.header ("🚀 Welcome to your Growth Journey!")
st.write("A growth mindset is the belief that abilities can be developed through dedication and hard work. It encourages embracing challenges, learning from mistakes, and viewing effort as a path to success and improvement ★.")


#quote section
st.header("💡 Growth Mindset Quote")
st.write("'Failure is not the opposite of success; it’s part of success.' — Arianna Huffington")

st.header("💪 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#Condition
if user_input:
    st.success(f"💪you are facing: {user_input}.
Keep pushing, because every step forward, no matter how small, brings you closer to your goal")
else:
    st.warning("Tell me about your Challenge to get started!")

    #reflexing
    st.header(" Reflect on Your Learning")
    reflection = st.text_area("Write Your out come here")

    if reflection:
        st.success(f"🌟 Great Insight! Your reflecton: {reflection}🌟")
    else:
        st.info("Reflection on past experience help you grow! share your difficulities")   

        #acheivements
    st.header("Celebrate Your Wins!")   
    acheivment = st.text_input("Share something you have recently accomplished:") 

    if acheivment:
         st.success(f"🎉 Amazing! Your achieved: {acheivment}")
    else:
        st.info("Big acheivment count! share one  now!🌟") 

       
       
#footer
st.write("___")    
st.write("Success is the sum of small efforts, repeated day in and day out.")
st.write("😇⭐⭐⭐ Created By Syeda Naila⭐⭐⭐")
        



