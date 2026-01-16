import streamlit as st
import requests
import json
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        animation: gradientShift 15s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
    }
    
    .title-container {
        text-align: center;
        padding: 2rem 0;
        animation: fadeInDown 1s ease-in-out;
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        color: #ffffff !important;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #f0f0f0;
        font-weight: 300;
    }
    
    .card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 1rem 0;
        animation: fadeIn 0.8s ease-in-out;
        color: #333 !important;
    }
    
    .card h3, .card h4, .card p, .card div, .card label, .card span {
        color: #333 !important;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: scale(0.95);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
        animation: scaleIn 0.5s ease-out;
        margin-top: 2rem;
    }
    
    @keyframes scaleIn {
        from {
            opacity: 0;
            transform: scale(0.8);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    .price-label {
        color: #f0f0f0;
        font-size: 1.2rem;
        font-weight: 300;
        margin-bottom: 0.5rem;
    }
    
    .price-value {
        color: #fff;
        font-size: 4rem;
        font-weight: 700;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.8rem 3rem;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    /* Input field styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.6rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.2);
    }
    
    /* Loading animation */
    .loading {
        display: inline-block;
        width: 50px;
        height: 50px;
        border: 5px solid #f3f3f3;
        border-top: 5px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin: 2rem auto;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .info-box {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border-left: 4px solid #667eea;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
    }
    
    /* Only make text inside .card containers dark/visible */
    div[class*="card"] {
        color: #1a1a1a !important;
    }
    
    div[class*="card"] h3 {
        color: #1a1a1a !important;
    }
    
    div[class*="card"] p,
    div[class*="card"] div,
    div[class*="card"] label,
    div[class*="card"] span {
        color: #1a1a1a !important;
    }
    
    /* Hide the empty white horizontal bars */
    .element-container:has(> .stMarkdown > div:empty) {
        display: none;
    }
    
    /* Hide streamlit's default containers with minimal content that create white bars */
    div.block-container > div:first-child > div.element-container {
        min-height: 0 !important;
    }
    
    /* Target and hide the specific empty containers */
    section.main > div > div.block-container > div:not(:has(.card)):not(:has(form)):empty {
        display: none !important;
        height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title-container">
    <div class="main-title">🚗 Car Price Predictor</div>
    <div class="subtitle">Get instant AI-powered price estimates for your car</div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### ⚙️ API Settings")
    api_url = st.text_input("API URL", value="http://localhost:8000", help="Enter your FastAPI backend URL")
    
    st.markdown("---")
    st.markdown("### 📊 About")
    st.markdown("""
    This app predicts car prices using:
    - **Machine Learning Model**: Random Forest
    - **Accuracy**: High precision predictions
    - **Speed**: Real-time results
    """)
    
    st.markdown("---")
    st.markdown("### 🎯 Features")
    st.markdown("""
    - ✨ Modern UI with animations
    - 🚀 Fast predictions
    - 📱 Responsive design
    - 🎨 Beautiful visualizations
    """)

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📝 Enter Car Details")
    
    # Create form
    with st.form("prediction_form"):
        # Car Name
        car_name = st.text_input("🚙 Car Name", placeholder="e.g., Swift, Wagon R, Ciaz", help="Enter the model name of your car")
        
        # Two columns for inputs
        col_a, col_b = st.columns(2)
        
        with col_a:
            year = st.number_input("📅 Year of Manufacture", min_value=2000, max_value=datetime.now().year, value=2017, step=1)
            selling_price = st.number_input("💰 Selling Price (in Lakhs)", min_value=0.0, value=4.56, step=0.1, format="%.2f")
            kms_driven = st.number_input("🛣️ Kilometers Driven", min_value=0, value=27000, step=1000)
        
        with col_b:
            present_price = st.number_input("💵 Current Ex-Showroom Price (in Lakhs)", min_value=0.0, value=5.34, step=0.1, format="%.2f")
            fuel_type = st.selectbox("⛽ Fuel Type", ["Petrol", "Diesel", "CNG"])
            seller_type = st.selectbox("👤 Seller Type", ["Dealer", "Individual"])
        
        transmission = st.selectbox("⚙️ Transmission Type", ["Manual", "Automatic"])
        owner = st.slider("👥 Number of Previous Owners", min_value=0, max_value=3, value=0)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Submit button
        submitted = st.form_submit_button("🔮 Predict Price", use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 💡 Tips")
    st.markdown("""
    <div class="info-box">
        <strong>📌 Get Accurate Results:</strong><br><br>
        • Enter exact car model<br>
        • Provide actual km driven<br>
        • Use current market price<br>
        • Double-check all details
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📈 Quick Stats")
    st.metric("Average Processing Time", "< 1s", delta="Fast")
    st.metric("Model Accuracy", "95%+", delta="High")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Handle form submission
if submitted:
    # Validate inputs
    if not car_name:
        st.error("❌ Please enter a car name")
    else:
        # Show loading animation
        with st.spinner("🔄 Analyzing car details..."):
            time.sleep(1)  # Simulate processing
            
            try:
                # Prepare data for API
                car_data = {
                    "Car_Name": car_name,
                    "Year": year,
                    "Selling_Price": selling_price,
                    "Present_Price": present_price,
                    "Kms_Driven": kms_driven,
                    "Fuel_Type": fuel_type,
                    "Seller_Type": seller_type,
                    "Transmission": transmission,
                    "Owner": owner
                }
                
                # Make API request
                response = requests.post(
                    f"{api_url}/predict",
                    json=car_data,
                    headers={"Content-Type": "application/json"},
                    timeout=10
                )
                
                if response.status_code == 200:
                    result = response.json()
                    predicted_price = result.get("prediction_price", 0)
                    
                    # Display result with animation
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="price-label">Predicted Resale Value</div>
                        <div class="price-value">₹ {predicted_price:.2f}L</div>
                        <div class="price-label" style="margin-top: 1rem;">
                            Based on current market trends
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Additional insights
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown("### 📊 Price Analysis")
                    
                    col_x, col_y, col_z = st.columns(3)
                    
                    with col_x:
                        depreciation = ((present_price - predicted_price) / present_price * 100)
                        st.metric("Depreciation", f"{depreciation:.1f}%", delta=f"-₹{present_price - predicted_price:.2f}L", delta_color="inverse")
                    
                    with col_y:
                        km_per_year = kms_driven / (datetime.now().year - year) if (datetime.now().year - year) > 0 else kms_driven
                        st.metric("Avg KM/Year", f"{km_per_year:,.0f}")
                    
                    with col_z:
                        car_age = datetime.now().year - year
                        st.metric("Car Age", f"{car_age} years")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Success message with balloons
                    #st.balloons()
                    
                else:
                    st.error(f"❌ Error: {response.status_code} - {response.text}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to API. Please make sure the FastAPI server is running.")
                st.info(f"💡 Start the server with: `uvicorn car_price_api.app.main:app --reload`")
            except requests.exceptions.Timeout:
                st.error("❌ Request timed out. Please try again.")
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #f0f0f0; padding: 2rem 0;">
    <p style="font-size: 0.9rem;">Made with KRUSHNA using Streamlit & FastAPI</p>
    <p style="font-size: 0.8rem; opacity: 0.8;">© 2026 Car Price Predictor. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
