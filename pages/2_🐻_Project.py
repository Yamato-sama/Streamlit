import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]
st.sidebar.title(emojis[7]+"SUN CHETRA")
st.title("Project Preview")
st.header("More Projects will be added. Stay Tune")

option = st.selectbox(
                     'Please Select Project you want to see.',
                    ('Supermarket Analysis', 'IMPORT & EXPORT (Sql server)','Personal Website Project'))

if option == "Supermarket Analysis":
    st.subheader("About Project")
    st.write("About Project visualize and analysis ")
    st.write("Explore Product Supermarket")
    st.write("Understand Which Product Category Should get Promotion.")
    st.write("Know about the the most sold product")
    st.write("Discover about the city that generation a lot of profit")

    st.subheader("Link to the project")
    st.write("https://github.com/Yamato-sama/Supermarket_Sale_Analysis-Excelv")

if option == "IMPORT & EXPORT (Sql server)":

    st.subheader("About Project")
    st.write("The Data that use in this project from sql server. and we visualize on google spreadsheet")
    st.write("  .Product that we need to focus.")
    st.write("  .Customer that buy our product the most.")
    st.write("  .Top 3 Employees.")
    st.write("  .Performance of the Shipper.")

    st.subheader("Link to Project")
    st.write("https://github.com/Yamato-sama/IMPORT-EXPORT-Sql")

if option == "Personal Website Project":
    st.subheader("Streamllit Framework")
    st.write("This website also my own project that create from streamlit framework.")
    st.write("Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes")

    st.subheader("Link to Project")
    st.write("https://github.com/Yamato-sama/Streamlit")






