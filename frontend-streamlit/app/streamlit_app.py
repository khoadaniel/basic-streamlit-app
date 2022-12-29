import json

import requests
import streamlit as st

st.title("My First Calculator Web App")

# taking user inputs
option = st.selectbox("What operations do you want to perform",
                      ('add', 'multiply'))
# write to the "interface" of the web-app
st.write("")
st.write("Select the numbers from the slider below")
x = st.slider("x", 0, 100, 20)
y = st.slider("y", 0, 130, 10)

# converting the inputs into a json format
inputs = {"operation": option, "x": x, "y": y}

# when users click on this button, the web-app will call the API
if st.button("Calculate"):
    result = requests.post(url="http://172.17.0.1:8000/calculate",
                           data=json.dumps(inputs))
    #json.dump() will produce a .json file

    st.subheader(f"Response from API = {result.text}")
    st.subheader(f"Raw response from API = {result}")
