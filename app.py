import streamlit as st
import numpy as np
import pandas as pd
import joblib
import altair as alt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title=" AI Student Travel Budget Planner",
    page_icon="🎒",
    layout="wide"
)

# ---------------- CSS THEME ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
.page { padding: 40px; border-radius: 25px; width: 90vw; margin:auto; }
.title { font-size: 3.5rem; font-weight: 700; color: white; }
.subtitle { font-size: 1.4rem; color: gold; }
.center { text-align: center; }
.card { background: #f9f9f9; padding: 35px; border-radius: 20px; box-shadow: 0 15px 30px rgba(0,0,0,0.15); }
.stButton>button { background-color: #1f77b4; color: white; border-radius: 20px; font-size: 1.2rem; padding:0.6em 1.5em; }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------------- LOAD MODEL ----------------
model = joblib.load("model2.pkl")  # Replace with actual student budget model

# ---------------- ENCODINGS ----------------
gender_map = {"M":0,"F":1}
interest_map = {"Beach":0,"Adventure":1,"Culture":2,"Nature":3,"Hill Station":4,"Shopping":5,"Food & Cuisine":6}
companion_map = {"Solo":0,"Friends":1,"Family":2}
accommodation_map = {"Budget":0,"Standard":1,"Luxury":2}

# ---------------- STATE DATA ----------------
state_data = {
    "Tamil Nadu":{"cities":["Chennai","Ooty","Madurai"],"food":["Idli","Dosa","Chettinad Chicken"],"hotels":{"Budget":"Student Hostels","Standard":"Mid-range Hotel","Luxury":"Taj Coromandel"}},
    "Kerala":{"cities":["Kochi","Munnar","Varkala"],"food":["Sadya","Appam & Stew"],"hotels":{"Budget":"Hosteller","Standard":"Abad Hotels","Luxury":"Kumarakom Lake Resort"}},
    "Karnataka":{"cities":["Bangalore","Mysore","Coorg"],"food":["Bisi Bele Bath","Mysore Pak"],"hotels":{"Budget":"Zostel Bangalore","Standard":"Royal Orchid","Luxury":"Taj West End"}},
    "Goa":{"cities":["Panaji","Calangute","Baga Beach"],"food":["Goan Fish Curry","Bebinca"],"hotels":{"Budget":"Pappi Chulo Hostel","Standard":"Resort Rio","Luxury":"The Leela Goa"}},
    "Maharashtra":{"cities":["Mumbai","Pune","Aurangabad"],"food":["Vada Pav","Pav Bhaji","Misal Pav"],"hotels":{"Budget":"Zostel Mumbai","Standard":"Hotel Shreeram","Luxury":"Taj Mahal Palace"}},
    "Rajasthan":{"cities":["Jaipur","Udaipur","Jodhpur"],"food":["Dal Baati Churma","Laal Maas"],"hotels":{"Budget":"Zostel Jaipur","Standard":"Trident Udaipur","Luxury":"Rambagh Palace"}},
    "Uttar Pradesh":{"cities":["Agra","Varanasi","Lucknow"],"food":["Tunday Kababi","Petha","Galouti Kebab"],"hotels":{"Budget":"Zostel Varanasi","Standard":"Ramada Lucknow","Luxury":"Taj Mahal Hotel Agra"}},
    "West Bengal":{"cities":["Kolkata","Darjeeling","Shantiniketan"],"food":["Rosogolla","Mishti Doi","Fish Curry"],"hotels":{"Budget":"Zostel Kolkata","Standard":"The Peerless Inn","Luxury":"The Oberoi Grand"}},
    "Gujarat":{"cities":["Ahmedabad","Vadodara","Dwarka"],"food":["Dhokla","Undhiyu"],"hotels":{"Budget":"Zostel Ahmedabad","Standard":"Courtyard by Marriott","Luxury":"The House of MG"}},
    "Punjab":{"cities":["Amritsar","Chandigarh"],"food":["Butter Chicken","Makki di Roti"],"hotels":{"Budget":"Zostel Amritsar","Standard":"Hyatt Chandigarh","Luxury":"Taj Swarna"}},
    "Himachal Pradesh":{"cities":["Shimla","Manali"],"food":["Sidu","Chha Gosht"],"hotels":{"Budget":"Zostel Manali","Standard":"The Oberoi Cecil Shimla","Luxury":"Wildflower Hall"}},
    "Telangana":{"cities":["Hyderabad","Warangal"],"food":["Hyderabadi Biryani","Mirchi ka Salan"],"hotels":{"Budget":"Zostel Hyderabad","Standard":"Taj Krishna","Luxury":"ITC Kohenur"}},
    "Madhya Pradesh":{"cities":["Bhopal","Indore","Gwalior"],"food":["Poha","Dal Bafla"],"hotels":{"Budget":"Zostel Bhopal","Standard":"Radisson Indore","Luxury":"Taj Gwalior"}},
    "Bihar":{"cities":["Patna","Gaya"],"food":["Litti Chokha","Sattu Paratha"],"hotels":{"Budget":"Zostel Patna","Standard":"Hotel Patliputra","Luxury":"Clarks Hotel"}},
    "Odisha":{"cities":["Bhubaneswar","Puri"],"food":["Dalma","Rasgulla"],"hotels":{"Budget":"Zostel Bhubaneswar","Standard":"Mayfair Lagoon","Luxury":"Trident Bhubaneswar"}},
    "Assam":{"cities":["Guwahati","Kaziranga"],"food":["Assamese Thali","Masor Tenga"],"hotels":{"Budget":"Zostel Guwahati","Standard":"Hotel Brahmaputra","Luxury":"Vivanta Guwahati"}},
    "Jharkhand":{"cities":["Ranchi","Jamshedpur"],"food":["Thekua","Malpua"],"hotels":{"Budget":"Zostel Ranchi","Standard":"Ginger Hotel Jamshedpur","Luxury":"The Patliputra"}}
}

# ---------------- DAILY PLAN FUNCTION ----------------
def generate_daily_plan(state, days):
    cities = state_data[state]["cities"]
    plan = []
    for i in range(days):
        city = cities[i % len(cities)]
        plan.append({
            "Day": f"Day {i+1} 🎒",
            "City": city,
            "Activities": f"Student-friendly activities: sightseeing, cultural walks, cafes ☕, and local attractions 🏛️"
        })
    return pd.DataFrame(plan)

# ===================== PAGE LOGIC =====================
# PAGE 1 : TITLE
if st.session_state.page == 1:
    st.markdown("""
    <div class="page center" style="background:linear-gradient(90deg,#1f4068,#162447);">
        <div class="title">🎒 AI Student Travel Budget Planner</div>
        <div class="subtitle">Budget-friendly trips for students ✨ Explore cities 🏙️, taste local food 🍲, save money 💰!</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("👉 Start Planning Your Travel Destination ", use_container_width=True):
        st.session_state.page = 2
        st.rerun()

# PAGE 2 : INPUTS
elif st.session_state.page == 2:
    st.markdown("""
    <div class="page" style="background:linear-gradient(90deg,#0f3460,#1c3c72);">
        <div class="title">📝 Travel Preferences</div>
        <div class="subtitle">Fill your details to generate a student-friendly trip 🚌📚</div>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    age = col1.number_input("Age", 15, 60, 20)
    gender = col1.selectbox("Gender", list(gender_map.keys()))
    state = col1.selectbox("State", list(state_data.keys()))
    days = col1.number_input("Number of Days", 1, 50, 3)
    p_interest = col2.selectbox("Primary Interest", list(interest_map.keys()))
    s_interest = col2.selectbox("Secondary Interest", list(interest_map.keys()))
    companion = col2.selectbox("Travel Companion", list(companion_map.keys()))
    accommodation = col2.selectbox("Accommodation Type", list(accommodation_map.keys()))
    if st.button("💰 Predict Budget", use_container_width=True):
        X = np.array([[age, gender_map[gender], interest_map[p_interest], interest_map[s_interest], companion_map[companion], accommodation_map[accommodation], days]])
        st.session_state.prediction = model.predict(X)[0]
        st.session_state.days = days
        st.session_state.state = state
        st.session_state.page = 3
        st.rerun()

# PAGE 3 : RESULTS
elif st.session_state.page == 3:
    total_budget = st.session_state.prediction
    days = st.session_state.days
    per_day = total_budget/days
    state = st.session_state.state

    st.markdown(f"""
    <div class="page center" style="background:linear-gradient(90deg,#ff8c42,#ff3c38);">
        <div class="title">🎯 Budget & Daily Plan</div>
        <div class="subtitle">Student-friendly plan for {days} days in {state} 🎒💡</div>
    </div>
    """, unsafe_allow_html=True)

    # Budget Card
    st.markdown(f"""
    <div class="card center">
        <h2>Total Budget</h2>
        <h1 style="color:#FF6B6B;">$ {total_budget:,.2f}</h1>
        <p><b>{days}</b> days • <b>$ {per_day:,.2f}</b> per day</p>
    </div>
    """, unsafe_allow_html=True)

    # Daily Plan
    st.subheader("📅 Daily Plan")
    plan_df = generate_daily_plan(state, days)
    st.table(plan_df)

    # Hotels & Food
    st.subheader("🏨 Accommodation & 🍽️ Food")
    hotels = state_data[state]["hotels"]
    st.write(f"- Budget: {hotels['Budget']}\n- Standard: {hotels['Standard']}\n- Luxury: {hotels['Luxury']}")
    for food in state_data[state]["food"]:
        st.write(f"• {food}")

    # Student Tips
    st.subheader("💡 Student Travel Tips")
    tips = [
        "Book hostels or shared accommodations 🛏️",
        "Use public transport 🚌 instead of cabs",
        "Try local street food 🍲 for budget-friendly taste",
        "Travel during semester breaks 📚",
        "Carry student ID 🎓 for discounts",
        "Pack light 🎒 to avoid extra costs"
    ]
    for t in tips:
        st.write(f"• {t}")

    # Budget Split Chart using Altair
    st.subheader("📊 Budget Split")
    split_df = pd.DataFrame({
        "Category":["Stay","Food","Travel","Activities"],
        "Amount":[total_budget*0.35, total_budget*0.35, total_budget*0.35, total_budget*0.25]
    })
    chart = alt.Chart(split_df).mark_bar(cornerRadiusTopLeft=5, cornerRadiusTopRight=5).encode(
        x=alt.X('Category', sort=None),
        y='Amount',
        color=alt.Color('Category', scale=alt.Scale(range=['#1f77b4','#ff7f0e','#2ca02c','#d62728']))
    )
    st.altair_chart(chart, use_container_width=True)

    if st.button("✅ Finish Trip"):
        st.session_state.page = 4
        st.rerun()

# PAGE 4 : THANK YOU + DOWNLOAD
elif st.session_state.page == 4:
    total_budget = st.session_state.prediction
    days = st.session_state.days
    state = st.session_state.state
    plan_df = generate_daily_plan(state, days)
    hotels = state_data[state]["hotels"]
    foods = state_data[state]["food"]
    
    tips = [
        "Book hostels or shared accommodations 🛏️",
        "Use public transport 🚌 instead of cabs",
        "Try local street food 🍲 for budget-friendly taste",
        "Travel during semester breaks 📚",
        "Carry student ID 🎓 for discounts",
        "Pack light 🎒 to avoid extra costs"
    ]
    
    # Create text content
    text_content = f"🎒 Student Travel Plan for {days} Days in {state}\n"
    text_content += "======================================\n\n"
    text_content += "📅 Daily Plan:\n"
    for i, row in plan_df.iterrows():
        text_content += f"{row['Day']}: {row['City']} - {row['Activities']}\n"
    text_content += "\n🏨 Accommodation:\n"
    text_content += f"Budget: {hotels['Budget']}\nStandard: {hotels['Standard']}\nLuxury: {hotels['Luxury']}\n"
    text_content += "\n🍽️ Famous Local Food:\n"
    for food in foods:
        text_content += f"- {food}\n"
    text_content += f"\n💰 Total Budget: ₹ {total_budget:,.2f}\nPer Day Budget: ₹ {total_budget/days:,.2f}\n"
    text_content += "\n💡 Student Travel Tips:\n"
    for t in tips:
        text_content += f"- {t}\n"
    text_content += "\n======================================\nHave a safe and memorable trip! ✨\n"

    # Download Button
    st.download_button(
        label="📥 Download Your Destination trip",
        data=text_content,
        file_name=f"Student_Travel_Plan_{state}.txt",
        mime="text/plain"
    )

    # Thank You message
    st.markdown("""
    <div class="page center" style="background:linear-gradient(90deg,#162447,#1f4068);">
        <div class="title">🎉 Thank You, and come back make your Own travel trip</div>
        <div class="subtitle">
        Traveling as a student is more than sightseeing 🌏—it's about learning independence 🧭, budgeting 💰, exploring culture 🎶, and making memories 📸. Discover new cities 🏙️, try local cuisines 🍲, meet fellow students 🤝, and enjoy the freedom of travel 🎒. Every trip is a classroom of experiences, so travel smart, explore wisely, and make every moment unforgettable! ✨
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    if col1.button("🔁 Plan Another Trip"):
        st.session_state.page = 2
        st.rerun()
    if col2.button("🏠 Exit "):
        st.session_state.page = 1

        st.rerun() 
