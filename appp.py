import streamlit as st

st.set_page_config(page_title="Dream House Predictor", page_icon="🏠", layout="centered")

# ---------- Background + UI Style ----------
page_bg = """
<style>

/* Background */
.stApp{
background-image: url("https://images.unsplash.com/photo-1560518883-ce09059eeffa");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}

/* Header */
.header{
background:#020617;
padding:20px;
text-align:center;
font-size:36px;
font-weight:bold;
color:white;
letter-spacing:1px;
box-shadow:0 0 20px rgba(0,255,170,0.6);
}

/* Title Glow */
.title-box{
margin-top:40px;
padding:15px;
text-align:center;
font-size:28px;
font-weight:600;
color:white;
border:2px solid #00ffaa;
border-radius:12px;
box-shadow:0 0 20px rgba(0,255,170,0.6);
}

/* Input Labels */
label{
color:#f1f5f9 !important;
font-weight:600;
}

/* Input Box Glow */

div[data-baseweb="select"] > div{
background:#0f172a !important;
color:white !important;
border-radius:10px;
box-shadow:0 0 10px rgba(0,255,170,0.3);
}

input{
background:#0f172a !important;
color:white !important;
border-radius:10px;
box-shadow:0 0 10px rgba(0,255,170,0.3);
}

/* Button */

button[kind="primary"]{
background:#22c55e;
border-radius:10px;
font-weight:600;
box-shadow:0 0 10px rgba(0,255,170,0.5);
}

/* Result Card */

.result-card{
background:rgba(0,0,0,0.85);
padding:25px;
border-radius:12px;
border:2px solid #00ffaa;
box-shadow:0 0 25px rgba(0,255,170,0.7);
margin-top:30px;
text-align:center;
}

.price{
font-size:28px;
color:#00ff9d;
font-weight:bold;
}

.type{
font-size:20px;
color:#60a5fa;
margin-top:10px;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="header">🏡 DREAM HOUSE</div>', unsafe_allow_html=True)

# ---------- Title ----------
st.markdown(
'<div class="title-box">House Price & House Type Prediction</div>',
unsafe_allow_html=True
)

# ---------- Encoding ----------
city_map = {
    "Mumbai":0,
    "Pune":1,
    "Delhi":2,
    "Bangalore":3,
    "Nagpur":4,
    "Hyderabad":5,
    "Ahmedabad":6,
    "Kolkata":7,
    "Chennai":8
}

furnished_map = {
    "Unfurnished":0,
    "Semi Furnished":1,
    "Furnished":2
}

parking_map = {
    "No":0,
    "Yes":1
}

# ---------- 2 Column Layout ----------
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (Sqft)", min_value=200, max_value=10000, step=50)
    city = st.selectbox("City", list(city_map.keys()))

with col2:
    bhk = st.selectbox("BHK", [1,2,3,4,5,6])
    furnished = st.selectbox("Furnishing", list(furnished_map.keys()))

# Full width parking
parking = st.selectbox("Parking Available", list(parking_map.keys()))

# Encoding
city_encoded = city_map[city]
furnished_encoded = furnished_map[furnished]
parking_encoded = parking_map[parking]

# ---------- Button ----------
predict = st.button("Predict Price")

# ---------- Prediction ----------
if predict:

    predicted_price = area * 4500

    if area > 2000:
        predicted_type = "Independent House"
    elif bhk >= 3:
        predicted_type = "Apartment"
    else:
        predicted_type = "Builder Floor"

    st.markdown(f"""
    <div class="result-card">
        <div class="price">💰 ₹ {predicted_price:,.0f}</div>
        <div class="type">🏠 {predicted_type}</div>
    </div>
    """, unsafe_allow_html=True)