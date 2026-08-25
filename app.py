import streamlit as st
from models.subscription import Subscription
from services.db import save_subscription

st.title("worthy")
st.write("A calmer way to decide what earns its place in your monthly budget.")

st.subheader("Add a subscription")

name = st.selectbox("Name", [
    "Netflix", "Disney+", "Amazon Prime", "Spotify", "Apple Music",
    "YouTube Premium", "Now TV", "Paramount+", "Apple TV+", "BBC iPlayer",
    "Sky", "Discovery+", "Audible", "PlayStation Plus", "Xbox Game Pass",
    "Nintendo Switch Online", "iCloud+", "Google One", "Microsoft 365",
    "Adobe Creative Cloud", "ChatGPT Plus", "LinkedIn Premium", "Gym membership",
    "The Guardian","Claude" ,"Other"
])
cost = st.number_input("Monthly cost (£)", min_value=0.0, step=0.01)
renewalDate = st.date_input("Renewal date", format="DD/MM/YYYY")
category = st.selectbox("Category", ["Entertainment", "Music", "Fitness", "Software", "Cloud Storage", "News", "Other"])
lastUsedDate = st.date_input("Last used date", format="DD/MM/YYYY")

if st.button("Add subscription"):
    newSub = Subscription(name, cost, str(renewalDate), category, str(lastUsedDate))
    save_subscription(newSub)
    st.success(f"{name} added!")