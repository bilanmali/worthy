from datetime import date 
import streamlit as st
from models.subscription import Subscription
from services.db import save_subscription, get_all_subscriptions
from services.ai import get_verdict

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Niconne&family=Elms+Sans:wght@400;600&display=swap');

    * {
        font-family: 'Elms Sans', sans-serif !important;
    }

    h1, h1 * {
        font-family: 'Niconne', cursive !important;
        color: #14B8A6 !important;
    }
    </style>
    <h1>worthy</h1>
""", unsafe_allow_html=True)
st.write("Is your subscription worth it?")

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
    

st.subheader("Your subscriptions")

subscriptions = get_all_subscriptions()

for sub in subscriptions:
    formattedRenewal = sub[2].strftime("%d/%m/%Y") if hasattr(sub[2], 'strftime') else sub[2]

    # work out how many days since it was last used
    lastUsed = sub[4]
    daysSinceUsed = (date.today() - lastUsed).days if hasattr(lastUsed, 'strftime') else "unknown"

    verdict = get_verdict(sub[0], daysSinceUsed)

    st.write(f"{sub[0]} — £{sub[1]} — renews {formattedRenewal} — {sub[3]}")
    st.caption(verdict)