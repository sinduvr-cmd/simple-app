import streamlit as st

st.title("AI Traveller APP")

destination=st.text_input("Enter destination")
travel_date=st.date_input("Enter the travel Date")
budget=st.number_input("Enter budget")
hotel_required=st.selectbox("Do you need hotel stay",("Yes","No"))

if st.button("Submit"):
    st.write(f"""
    AI Travel Agent Summary
    -----------------------
    Destination \t: {destination}
    Travel Date \t: {travel_date}
    Budget  \t: {budget}
    Hotel_Required \t: {hotel_required}
    """)
    st.balloons()
