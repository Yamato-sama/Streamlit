import streamlit as st

emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]

st.sidebar.title(emojis[7]+"SUN CHETRA")

st.title(emojis[1]+"Welcome to my Personal Website.")
st.write("Before you take a look at my project I will give you an introduction. I create this website to move my project"
         "python. That means the website itself is also my project using streamlit to create.")
st.write("The Framework that I use is Pandas, Streamlit, Matplotlib.")

st.write("Place of Birth :Samraong Village,Chum riel Commune,Tuek Chhou Dtrict,Kampot Province.")
st.write("Date Of Birth : 3-Sep-2000")
st.write("Nationality : Cambodian")

st.subheader("Linkin : https://www.linkedin.com/in/chetra-sun")
st.subheader("Gmail  : sunchetra907@gmail.com")
st.sidebar.color_picker('Pick a color')

