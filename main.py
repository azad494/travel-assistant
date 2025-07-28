# main.py

import streamlit as st
from prompts import build_prompt
from planner import get_itinerary

st.title("🧳 GPT-4 Travel Planner")
st.write("Personalized AI-generated travel plans.")

destination = st.text_input("🌍 Destination")
days = st.number_input("📅 Days", min_value=1, max_value=30, value=5)
budget = st.selectbox("💰 Budget", ["Low", "Medium", "Luxury"])
season = st.selectbox("☀️ Season", ["Spring", "Summer", "Monsoon", "Winter", "Other"])
interests = st.text_area("🎯 Interests", placeholder="e.g. beaches, food, museums")

if st.button("Generate Itinerary"):
    prompt = build_prompt(destination, days, budget, season, interests)
    itinerary = get_itinerary(prompt)
    st.subheader("🗺️ Itinerary:")
    st.markdown(itinerary)
