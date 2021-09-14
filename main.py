import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("Affairs.pkl","rb"))


def predict_affair(rate_marriage,yrs_married,children,educ):
    input=np.array([[rate_marriage,yrs_married,children,educ]]).astype(np.float64)
    prediction = model.predict(input)

    return int(prediction)

def main():
    st.title("Affair Prediction")
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Affair Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)

    rate_marriage = st.text_input("Rate your Marriage(1 = very poor, 5 = very good)")
    yrs_married = st.text_input("Years Married")
    children = st.text_input("Number of Children")
    educ = st.text_input("Highest Education(9 = grade school, 12 = high school, 14 = some college, 16 = college graduate, 17 = some graduate school, 20 = advanced degree)")

    safe_html = """  
      <div style="background-color:#80ff80; padding:10px >
      <h2 style="color:white;text-align:center;"> You Don't have a Affair</h2>
      </div>
    """
    warn_html ="""  
      <div style="background-color:#F4D03F; padding:10px >
      <h2 style="color:white;text-align:center;"> You have a Affair</h2>
      </div>
    """

    if st.button("Predict the Affair"):
        output =predict_affair(rate_marriage,yrs_married,children,educ)
        st.success('{}'.format(output))

        if output == 0:
            st.markdown(safe_html,unsafe_allow_html=True)
        elif output == 1:
            st.markdown(warn_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
        




