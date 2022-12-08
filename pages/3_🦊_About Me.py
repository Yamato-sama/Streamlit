import streamlit as st

emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]
st.sidebar.title(emojis[7]+"SUN CHETRA")



st.header(emojis[2]+"Skill Set")
st.slider("Python",1,100,70,disabled=True)
st.slider("SSIS",1,100,60,disabled=True)
st.slider("Power BI",1,100,65,disabled=True)
st.slider("SQL",1,100,60,disabled=True)
st.slider("Microsoft Excel",1,100,60,disabled=True)


st.header(emojis[0]+"My Experience")
st.write("My name is Sun Chetra. You can call me Chet or Tra for short. I came from Kampot Province. Now I live in Phnom Penh.I graduated with my degree in Computer Science 5 months ago. I choose that field of study because I have always been interested in technology. when I was studying in my fourth year, it was time for me to choose a career path and I pick the Data Science field because the most company have a ton of data, and people who work in the Data Science field play an important role to make those Data useful for business.After that, I join the  DATA SPECIALIST TRAINING PROGRAMME. after I finish the program I went to intern at Japan Company in Cambodia. And then I started a new position at ABA Bank as Compliance Analytic Specialist.")

