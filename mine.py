
# import pandas as pd
# import numpy as np
# import streamlit as st
# import pickle
# import os

# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import warnings
# from PIL import Image
# import base64
# df = pd.read_excel("F:\\Masai\\Project Webpage\\Zomato Data.xlsx")
url="https://raw.githubusercontent.com/anishkatoch/Zomato-Recommendation-Model/main/Zomato%20CSV.csv"
df=pd.read_csv(url)

feedback_file_path = "feedback.xlsx"
feedback_data = pd.DataFrame()  



# def save_feedback(name, feedback):
#     global feedback_data
#     feedback_data = feedback_data.append({"Name": name, "Feedback": feedback}, ignore_index=True)
#     feedback_data.to_excel(feedback_file_path, index=False)
#     print("Feedback saved successfully.")
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

# def save_feedback(name, feedback, feedback_data):
#     feedback_data = feedback_data.append({"Name": name, "Feedback": feedback}, ignore_index=True)
#     feedback_data.to_excel(feedback_file_path, index=False)
#     print("Feedback saved successfully.")
#     return feedback_data

# def load_feedback_data():
#     try:
#         feedback_data = pd.read_excel(feedback_file_path)
#     except FileNotFoundError:
#         feedback_data = pd.DataFrame({"Name": [], "Feedback": []})
#     return feedback_data

# feedback_data = load_feedback_data()


# def predict_price(Cuisine, Location):
#     df2=pd.read_csv(url)
#     df3=df2[['Cuisine','Location','Price_For_One']]

#     loc = ['St. Marks Road', 'Frazer Town', 'Shivajinagar', 'City Market', 'Koramangala', 'Church Street', 'Lavelle Road', 'Shanti Nagar', 'Brigade Road', 'MG Road', 'Commercial Street', 'Residency Road', 'Basavanagudi', 'Mantri Square', 'Richmond Road', 'Malleshwaram', 'Indiranagar', 'Ulsoor', 'Garuda Mall', 'Jayanagar', 'Richmond Town', 'UB City', 'Vasanth Nagar', 'Wilson Garden', 'Cunningham Road', 'Seshadripuram', 'BTM', 'Rajajinagar', 'Domlur', 'Majestic', 'Sadashiv Nagar', 'Old Madras Road', 'Hosur Road', 'Lido Mall', 'Ejipura', 'Langford Town', 'Forum Rex Walk', 'Building 105', 'RT Nagar', '1 Sobha', 'Jatti Building', 'Basaveshwara Nagar', 'Nexus', 'Race Course Road', 'Old Airport Road', 'Infantry Road', 'Prestige Trade Tower', 'Thippasandra', 'Banashankari', 'ITC Gardenia', 'Jeevan Bhima Nagar', 'Hotel Southern Star', 'Global Village', 'Nagawara', 'BluPetal Hotel', 'Mysore Road', 'Magadi Road', 'CV Raman Nagar', 'Vijay Nagar', 'Sigma Mall', 'Kammanahalli', 'Kalyan Nagar']
#     locate= sorted(loc)
#     print(locate)

#     food=['Fast Food', 'Biryani', 'Sweets', 'Desserts', 'Bengali','South Indian', 'Italian', 'Arabian', 'Mexican', 'North Indian','Street Food', 'Beverages', 'Kerala', 'Andhra', 'Chinese', 'Asian','Tibetan']
#     cus = sorted(food)
#     print(cus)

#     dict1 = {}
#     for i in range(len(locate)):
#         dict1[locate[i]] = i 

#     dict2 = {}
#     for i in range(len(cus)):
#         dict2[cus[i]] = i
    
#     lc = LabelEncoder()
#     df3['Cuisine']=lc.fit_transform(df3['Cuisine'])
#     df3['Location']=lc.fit_transform(df3['Location'])

#     f1=dict2[Cuisine]
#     l1=dict1[Location]

#     df1_new=df3[(df3['Cuisine']==f1) | (df3['Location']==l1)]
#     print(df1_new)

#     x=df1_new.drop(['Price_For_One'],axis=1)
#     y=df1_new['Price_For_One']

#     lr=LinearRegression()
#     x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=10)
#     lr.fit(x_train,y_train)

#     return round(lr.predict(x_test).mean())


# def predict_location(Cuisine, Location, Preferred_Price_For_1):
#     df = pd.read_csv(url)
#     z = pd.DataFrame({"Cuisine": [Cuisine], "Location": [Location], "Price_For_One": [Preferred_Price_For_1]})
#     df = pd.concat([df, z])
#     lst = list(df["Location"].unique())

#     dict1 = {}
#     for i in range(len(lst)):
#         dict1[lst[i]] = i

#     dict2 = {}
#     for i in range(len(lst)):
#         dict2[i] = lst[i]

#     df["Location"] = df["Location"].apply(lambda x: dict1[x])
#     df = df[["Cuisine", "Location", "Price_For_One"]]  # Remove "Index" from the selected columns
#     x = df.drop("Location", axis=1)
#     y = df["Location"]

#     le = LabelEncoder()
#     x["Cuisine"] = le.fit_transform(x["Cuisine"])
#     x["Price_For_One"] = MinMaxScaler().fit_transform(x[["Price_For_One"]])  # Normalize only "Price_For_One"

#     xtr, xts, ytr, yts = train_test_split(x, y, test_size=0.3)
#     model = DecisionTreeClassifier()
#     model.fit(xtr, ytr)
#     ypred = model.predict(xts)
#     return dict2[ypred[-1]]

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



def main():
    global feedback_data
    feedback_data = load_feedback_data()
    # ...
    try:
        save_feedback(name, feedback)
    except Exception as e:
        print(f"Error occurred while saving feedback: {str(e)}")
        
    st.markdown("<h1 style='text-align: center; color: Chartreuse; padding: 20px; background-color: #F06292;'>RECOMMENDATION MODEL</h1>", unsafe_allow_html=True)
    
    html_temp = """
    <div style = 'background-color: orange ; padding : 0px ; max-width: 400px; margin: 20px auto;'>
    <h1 style = "color:red;text-align:center;"><b>ZOMATO</b></h1>
    </div>
    """


    st.markdown(html_temp, unsafe_allow_html = True)

    cuisines = df['Cuisine'].unique()
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'><b>Cuisine:</b></h2>", unsafe_allow_html=True)
    Cuisine = st.selectbox("",cuisines) 

    locations = df['Location'].unique()
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'>Preferred Location:</h2>", unsafe_allow_html=True)
    Preferred_Location = st.selectbox("",locations) 

    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'>Preferred Price For One:</h2>", unsafe_allow_html=True)
    Preferred_Price_For_1 = st.text_input("", key="price_input")
    
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

        # Recomm_price = predict_price(Cuisine,Preferred_Location)
        # Recomm_location = predict_location(Cuisine,Preferred_Location,Preferred_Price_For_1)


        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Average Price for 1:   {}</span>".format(avg), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Popular Cuisine:   {}</span>".format(Pop_Cuis), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Most Popular Restaurant:  {}</span>".format(Most_Popular_Rest), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Serves:  {}</span>".format(Serves), unsafe_allow_html=True)
        
        st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Popular Restaurant that serves your Cuisine: {}</span>".format(Popular_Rest_Serving_Your_Cuisine), unsafe_allow_html=True)
       
        # st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Recommended Price:  {}</span>".format(Recomm_price), unsafe_allow_html=True)
        
        # st.markdown("<span style='color: purple; font-weight: bold; font-size: 30px;'>Recommended Location:  {}</span>".format(Recomm_location), unsafe_allow_html=True)

    
    # Add feedback section
    load_feedback_data()
    st.markdown("<h1 style='text-align: center; color: DarkGoldenrod;'>FEEDBACK</h1>", unsafe_allow_html=True)

    # st.dataframe(feedback_data)
    
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'><b>Name</b></h2>", unsafe_allow_html=True)
    name = st.text_input("")
    st.markdown("<h2 style='font-size: 24px;margin-bottom: 0px;'><span style='color: red;'>Feedback</h2>", unsafe_allow_html=True)
    feedback = st.text_area("")

    # if st.button("Submit"):
    #     try:
    #         save_feedback(name, feedback)
    #         st.markdown("<span style='color: green; font-weight: bold; font-size: 35px;'>Feedback submitted successfully!</span>", unsafe_allow_html=True)
    #     except Exception as e:
            # st.markdown("<span style='color: red; font-weight: bold; font-size: 35px;'>Error occurred while saving feedback: {}</span>".format(str(e)), unsafe_allow_html=True)

    if st.button("Submit"):
        
        st.markdown("<span style='color: green; font-weight: bold; font-size: 35px;'>Feedback submitted successfully!</span>", unsafe_allow_html=True)
    
    
        
        

    
                
if __name__ == '__main__':
    main()
