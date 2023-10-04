# import library
import pandas as pd
import numpy as np
import streamlit as st
import pickle
import os

# clicking on link 
url="https://raw.githubusercontent.com/anishkatoch/Zomato-Recommendation-Model/main/Datasets/Zomato%20CSV.csv"
df=pd.read_csv(url)

feedback_file_path = "feedback.xlsx"
feedback_data = pd.DataFrame()  

# Feedback 
def save_feedback(name, feedback):
    global feedback_data
    new_feedback = pd.DataFrame({"Name": [name], "Feedback": [feedback]})
    feedback_data = pd.concat([feedback_data, new_feedback], ignore_index=True)
    feedback_data.to_excel(feedback_file_path, index=False)
    print("Feedback saved successfully.")


def load_feedback_data():
    global feedback_data
    try:
        feedback_data = pd.read_excel(feedback_file_path)
    except FileNotFoundError:
        feedback_data = pd.DataFrame({"Name": [], "Feedback": []})

# designing the webpage
page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"]
    {
    background-image: url("https://plus.unsplash.com/premium_photo-1663852297801-d277b7af6594?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80");
    background-size: cover;
    }
    </style>
    ''' 
st.markdown(page_bg_img, unsafe_allow_html=True)

# main function to call other function 
def main():
    global feedback_data
    feedback_data = load_feedback_data()
    # ...
    try:
        save_feedback(name, feedback)
    except Exception as e:
        print(f"Error occurred while saving feedback: {str(e)}")
        
    st.markdown("<h1 style='text-align: center; color: Chartreuse; padding: 20px; background-color: #F06292;'>RECOMMENDATION MODEL</h1>", unsafe_allow_html=True)
    # making the feedback colourful
    html_temp = """
    <div style = 'background-color: orange ; padding : 0px ; max-width: 400px; margin: 20px auto;'>
    <h1 style = "color:red;text-align:center;"><b>ZOMATO</b></h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html = True)
    
    # logics 
    cuisines = df['Cuisine'].unique()
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'><b>Cuisine:</b></h2>", unsafe_allow_html=True)
    Cuisine = st.selectbox("",cuisines) 

    locations = df['Location'].unique()
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'>Preferred Location:</h2>", unsafe_allow_html=True)
    Preferred_Location = st.selectbox("",locations) 

    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'>Preferred Price For One:</h2>", unsafe_allow_html=True)
    Preferred_Price_For_1 = st.text_input("", key="price_input")

    # creating button
    if st.button("Predict"):

        avg = round(df[(df['Cuisine'] == Cuisine) | (df['Location'] == Preferred_Location)]['Price_For_One'].mean())
        a = df[(df['Location'] == Preferred_Location)]

        Pop_Cuis = a[a['Rating'] == a['Rating'].max()]["Cuisine"].to_string().split()[1:]
        Pop_Cuis= " ".join(Pop_Cuis)

        Most_Popular_Rest = a[a["Delivery_Review_Number"] == a["Delivery_Review_Number"].max()]["Restaurant_Name"].to_string().split()[1:]
        Most_Popular_Rest= " ".join(Most_Popular_Rest)

        Serves = a[a["Delivery_Review_Number"] == a["Delivery_Review_Number"].max()]["Cuisine"].to_string().split()[1:]
        Serves= " ".join(Serves)

        b = a[(a['Cuisine'] == Cuisine)]
        Popular_Rest_Serving_Your_Cuisine = b[b["Delivery_Review_Number"] == b["Delivery_Review_Number"].max()]['Restaurant_Name'].to_string().split()[1:]
        Popular_Rest_Serving_Your_Cuisine= " ".join(Popular_Rest_Serving_Your_Cuisine)


        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Average Price for 1:   {}</span>".format(avg), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Popular Cuisine:   {}</span>".format(Pop_Cuis), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Most Popular Restaurant:  {}</span>".format(Most_Popular_Rest), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Serves:  {}</span>".format(Serves), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Popular Restaurant that serves your Cuisine: {}</span>".format(Popular_Rest_Serving_Your_Cuisine), unsafe_allow_html=True)
       
    
    # Add feedback section
    load_feedback_data()
    st.markdown("<h1 style='text-align: center; color: DarkGoldenrod;'>FEEDBACK</h1>", unsafe_allow_html=True)

    
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'><b>Name</b></h2>", unsafe_allow_html=True)
    name = st.text_input("")
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'>Feedback</h2>", unsafe_allow_html=True)
    feedback = st.text_area("")


    if st.button("Submit"):
        
        st.markdown("<span style='color: green; font-weight: bold; font-size: 35px;'>Feedback submitted successfully!</span>", unsafe_allow_html=True)
    
# constructor          
if __name__ == '__main__':
    main()
