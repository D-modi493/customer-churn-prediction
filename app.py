import streamlit as st
import pandas as pd
import pickle
import base64

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="logo.png",
    layout="wide"
)

model = pickle.load(open("churn_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_base64("background.png")

st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Rajdhani:wght@400;600;700&display=swap');

/* MAIN BACKGROUND */
.stApp {{
    background-image: url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Rajdhani', sans-serif;
}}

/* MAIN CONTAINER */
.main .block-container {{
    background: rgba(0, 8, 25, 0.72);
    padding: 36px 40px;
    border-radius: 18px;
    backdrop-filter: blur(14px);
    border: 1px solid rgba(0, 200, 255, 0.18);
    max-width: 1400px;
}}

/* TITLE */
.main-title {{
    font-family: 'Orbitron', sans-serif;
    font-size: 38px;
    font-weight: 900;
    color: #e6f7ff;
    text-align: center;
    letter-spacing: 2px;
    text-shadow: 0 0 20px rgba(0,200,255,0.6), 0 0 40px rgba(0,150,255,0.3);
    margin-bottom: 4px;
}}

.sub-title {{
    font-size: 16px;
    color:#e6f7ff;
    text-align: center;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 32px;
    font-family: 'Rajdhani', sans-serif;
}}

/* DIVIDER */
.neon-divider {{
    height: 2px;
    background: linear-gradient(90deg, transparent, #00c6ff, #0072ff, #00c6ff, transparent);
    margin: 8px 0 28px 0;
    border-radius: 2px;
    box-shadow: 0 0 10px rgba(0,200,255,0.5);
}}

/* PANEL HEADER */
.panel-title {{
    font-family: 'Orbitron', sans-serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 10px 16px;
    border-radius: 8px 8px 0 0;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
}}

.panel-title.blue {{
    color: #00cfff;
    background: rgba(0, 150, 255, 0.12);
    border-left: 3px solid #00cfff;
    border-bottom: 1px solid rgba(0,200,255,0.3);
    text-shadow: 0 0 10px rgba(0,200,255,0.5);
}}

.panel-title.green {{
    color: #00ffb3;
    background: rgba(0, 200, 120, 0.12);
    border-left: 3px solid #00ffb3;
    border-bottom: 1px solid rgba(0,255,150,0.3);
    text-shadow: 0 0 10px rgba(0,255,150,0.5);
}}

/* LABEL TEXT */
label, .stSelectbox label, .stSlider label, .stNumberInput label {{
    color: #b0d8f0 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
}}

/* INPUT STYLING */
.stTextInput>div>div>input,
.stNumberInput>div>div>input {{
    background-color: rgba(0, 20, 50, 0.85) !important;
    color: #e0f4ff !important;
    border: 1px solid rgba(0,180,255,0.35) !important;
    border-radius: 8px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 15px !important;
}}

.stSelectbox>div>div {{
    background-color: rgba(0, 20, 50, 0.85) !important;
    border: 1px solid rgba(0,180,255,0.35) !important;
    border-radius: 8px !important;
    color: #e0f4ff !important;
}}

/* SLIDER */
.stSlider>div>div>div>div {{
    background: linear-gradient(90deg, #00c6ff, #0072ff) !important;
}}

/* PREDICT BUTTON */
.stButton>button {{
    background: linear-gradient(135deg, #0072ff 0%, #00c6ff 50%, #0072ff 100%) !important;
    color: white !important;
    font-family: 'Orbitron', sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    border: 1px solid rgba(0,200,255,0.5) !important;
    box-shadow: 0 0 20px rgba(0,150,255,0.4), 0 4px 15px rgba(0,0,0,0.3) !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase !important;
}}

.stButton>button:hover {{
    background: linear-gradient(135deg, #00c6ff 0%, #0072ff 50%, #00c6ff 100%) !important;
    box-shadow: 0 0 35px rgba(0,200,255,0.7), 0 4px 20px rgba(0,0,0,0.4) !important;
    transform: translateY(-2px) scale(1.02) !important;
}}

/* RESULT BOX - CHURN */
.result-box {{
    border-radius: 14px;
    padding: 24px 20px;
    margin-top: 16px;
    backdrop-filter: blur(10px);
    text-align: center;
}}

.result-box.churn {{
    background: rgba(180, 20, 20, 0.18);
    border: 1px solid rgba(255, 80, 80, 0.5);
    box-shadow: 0 0 25px rgba(255,50,50,0.2), inset 0 0 40px rgba(180,0,0,0.1);
}}

.result-box.stay {{
    background: rgba(0, 180, 80, 0.15);
    border: 1px solid rgba(0, 255, 120, 0.5);
    box-shadow: 0 0 25px rgba(0,200,100,0.2), inset 0 0 40px rgba(0,150,80,0.1);
}}

.result-title {{
    font-family: 'Orbitron', sans-serif;
    font-size: 13px;
    letter-spacing: 3px;
    color: #90c8f0;
    text-transform: uppercase;
    margin-bottom: 12px;
}}

.result-verdict {{
    font-family: 'Orbitron', sans-serif;
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 10px;
    letter-spacing: 1px;
}}

.result-verdict.churn {{
    color: #ff6b6b;
    text-shadow: 0 0 15px rgba(255,80,80,0.6);
}}

.result-verdict.stay {{
    color: #00ffb3;
    text-shadow: 0 0 15px rgba(0,255,150,0.6);
}}

.result-prob {{
    font-family: 'Rajdhani', sans-serif;
    font-size: 16px;
    color: #c8e8ff;
    margin-bottom: 14px;
    font-weight: 600;
    letter-spacing: 1px;
}}

.result-bar-bg {{
    background: rgba(255,255,255,0.1);
    border-radius: 20px;
    height: 16px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.15);
}}

.result-bar-fill {{
    height: 100%;
    border-radius: 20px;
    transition: width 1s ease;
}}

.result-bar-fill.churn {{
    background: linear-gradient(90deg, #ff4444, #ff8c00);
    box-shadow: 0 0 10px rgba(255,80,0,0.6);
}}

.result-bar-fill.stay {{
    background: linear-gradient(90deg, #00b894, #00cec9);
    box-shadow: 0 0 10px rgba(0,200,150,0.6);
}}

/* WAITING PLACEHOLDER */
.waiting-box {{
    border-radius: 14px;
    padding: 40px 20px;
    margin-top: 16px;
    background: rgba(0, 30, 60, 0.4);
    border: 1px dashed rgba(0,180,255,0.25);
    text-align: center;
    color: rgba(120,180,220,0.5);
    font-family: 'Rajdhani', sans-serif;
    font-size: 15px;
    letter-spacing: 2px;
}}

/* Column separator */
.col-separator {{
    border-left: 1px solid rgba(0,180,255,0.2);
    height: 100%;
}}

/* h3 */
h3 {{
    color: white;
    font-family: 'Rajdhani', sans-serif;
}}

</style>
""", unsafe_allow_html=True)

# ── Header ──
st.markdown('<div class="main-title">Customer Churn Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">AI-Powered Telecom Churn Prediction Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

# ── 3-Column Layout ──
col1, col_mid, col2 = st.columns([1.1, 1.0, 1.1], gap="large")

# ─── LEFT: Customer Information ───
with col1:
    st.markdown('<div class="panel-title blue">👤 &nbsp; Customer Information</div>', unsafe_allow_html=True)

    tenure = st.slider("Tenure (Months)", 0, 72, 12)
    monthly_charges = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
    total_charges = st.number_input("Total Charges ($)", 0.0, 10000.0, 1000.0)
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", [0, 1])

# ─── MIDDLE: Predict Button + Result ───
with col_mid:
    st.markdown('<div class="panel-title blue">⚡ &nbsp; Prediction Engine</div>', unsafe_allow_html=True)

    st.write("")
    predict_clicked = st.button("⚡  PREDICT CHURN")
    st.write("")

    if predict_clicked:
        # Feature encoding
        input_dict = {
            "SeniorCitizen": senior,
            "tenure": tenure,
            "MonthlyCharges": monthly_charges,
            "TotalCharges": total_charges
        }
        input_df = pd.DataFrame([input_dict])

        if gender == "Male":                   input_df["gender_Male"] = 1
        if 'partner' in dir() and partner == "Yes": input_df["Partner_Yes"] = 1
        if 'dependents' in dir() and dependents == "Yes": input_df["Dependents_Yes"] = 1
        if 'internet_service' in dir():
            if internet_service == "Fiber optic": input_df["InternetService_Fiber optic"] = 1
            elif internet_service == "No":        input_df["InternetService_No"] = 1
        if 'contract' in dir():
            if contract == "One year":   input_df["Contract_One year"] = 1
            elif contract == "Two year": input_df["Contract_Two year"] = 1
        if 'paperless' in dir() and paperless == "Yes": input_df["PaperlessBilling_Yes"] = 1
        if 'payment' in dir():
            if payment == "Electronic check":          input_df["PaymentMethod_Electronic check"] = 1
            elif payment == "Mailed check":            input_df["PaymentMethod_Mailed check"] = 1
            elif payment == "Credit card (automatic)": input_df["PaymentMethod_Credit card (automatic)"] = 1

        for col in model_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[model_columns]

        prediction  = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        if prediction == 1:
            pct     = f"{probability:.2%}"
            bar_pct = f"{probability*100:.1f}%"
            st.markdown(f"""
            <div class="result-box churn">
                <div class="result-title">⚡ Prediction Result</div>
                <div class="result-verdict churn">⚠️ Customer Likely to CHURN</div>
                <div class="result-prob">Churn Probability: {pct}</div>
                <div class="result-bar-bg">
                    <div class="result-bar-fill churn" style="width:{bar_pct}"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            pct     = f"{(1-probability):.2%}"
            bar_pct = f"{(1-probability)*100:.1f}%"
            st.markdown(f"""
            <div class="result-box stay">
                <div class="result-title">⚡ Prediction Result</div>
                <div class="result-verdict stay">✅ Customer Likely to STAY</div>
                <div class="result-prob">Retention Probability: {pct}</div>
                <div class="result-bar-bg">
                    <div class="result-bar-fill stay" style="width:{bar_pct}"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="waiting-box">
            AWAITING INPUT<br><br>
            Fill in customer details and<br>press PREDICT CHURN
        </div>
        """, unsafe_allow_html=True)

# ─── RIGHT: Service Details ───
with col2:
    st.markdown('<div class="panel-title green">🛠️ &nbsp; Service Details</div>', unsafe_allow_html=True)

    contract         = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    partner          = st.selectbox("Partner", ["Yes", "No"])
    dependents       = st.selectbox("Dependents", ["Yes", "No"])
    paperless        = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment          = st.selectbox("Payment Method", [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ])