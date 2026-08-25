import streamlit as st
from models.subscription import Subscription
from services.db import save_subscription

st.title("worthy")
st.write("A calmer way to decide what earns its place in your monthly budget.")

st.subheader("Add a subscription")

name = st.text_input("Name")
cost = st.number_input("Monthly cost (£)", min_value=0.0, step=0.01)
renewalDate = st.date_input("Renewal date", format="DD/MM/YYYY")
category = st.text_input("Category")
lastUsedDate = st.date_input("Last used date", format="DD/MM/YYYY")

if st.button("Add subscription"):
    st.write("Button clicked!")