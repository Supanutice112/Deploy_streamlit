import pickle
import warnings

import streamlit as st

warnings.filterwarnings("ignore")
from PIL import Image

pickle_in =open("model_iris.pkl","rb")
classifier = pickle.load(pickle_in)

def predictiris_variety(sepal_length,sepal_width,petal_length,petal_width):
    prediction = classifier.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    print(prediction)
    return(prediction)

def Input_Output():
    st.title("Iris Variety Prediction")
    st.image("https://hgtvhome.sndimg.com/content/dam/images/grdn/fullset/2014/2/5/0/12-waltersgardens-hi14643-irisautumn-circus.jpg.rend.hgtvcom.1280.960.suffix/1452644697576.jpeg",width=600)

    st.markdown("You are using Streamlit...",unsafe_allow_html=True)
    sepal_length = st.text_input ("Enter Sepal Length",".")
    sepal_width = st.text_input ("Enter Sepal Width",".")
    petal_length = st.text_input ("Enter Petal Length",".")
    petal_width = st.text_input ("Enter Petal Width",".")
    
    result = ""
    if st.button("Click here to predict"):
        result = predictiris_variety(sepal_length,sepal_width,petal_length,petal_width)
        st.balloons()
    st.success('The output is {}'.format(result))
if  __name__ == '__main__':
    Input_Output()