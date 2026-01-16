# 🚗 FastAPI Car Price Predictor

**An AI-powered car price prediction API built with FastAPI and Streamlit. Features a Random Forest ML model, beautiful animated UI, and real-time price estimation for used cars.**

## ✨ Key Features
- 🤖 Random Forest ML model with 95%+ accuracy
- 🚀 FastAPI backend with automatic API documentation
- 🎨 Modern Streamlit frontend with smooth animations
- ⚡ Real-time predictions in under 1 second
- 📊 Detailed analytics: depreciation, car age, and market trends

## 🛠️ Tech Stack
**Backend:** FastAPI • Scikit-learn • Pandas • Pydantic  
**Frontend:** Streamlit • Custom CSS Animations  
**Model:** Random Forest Regressor with feature engineering

## 📂 Project Structure
```
fastapi_car_price/
│
├── car_price_api/
│   ├── app/
│   │   ├── main.py           # FastAPI application & routes
│   │   ├── model.py          # ML model loading & prediction
│   │   └── schemas.py        # Pydantic models for validation
│   │
│   ├── cardekho_data (1).csv # Training dataset
│   ├── train.py              # Model training script
│   ├── random_forest_model.pkl
│   ├── feature_columns.pkl
│   └── requirements.txt
│
└── streamlit_app.py          # Frontend UI application
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r car_price_api/requirements.txt
```

### 2. Run the FastAPI Backend
```bash
uvicorn car_price_api.app.main:app --reload
```
- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

### 3. Run the Streamlit Frontend
```bash
streamlit run streamlit_app.py
```
- Frontend: `http://localhost:8501`

## 📊 API Usage

### POST /predict
Predict car price based on features

**Request:**
```json
{
  "Car_Name": "ciaz",
  "Year": 2017,
  "Selling_Price": 4.56,
  "Present_Price": 5.34,
  "Kms_Driven": 27000,
  "Fuel_Type": "Petrol",
  "Seller_Type": "Dealer",
  "Transmission": "Manual",
  "Owner": 0
}
```

**Response:**
```json
{
  "prediction_price": 4.23
}
```

## 🧠 Model Training

To retrain the model:
```bash
python car_price_api/train.py
```

## 🎨 UI Features
- 🌈 Animated gradient backgrounds
- 💫 Smooth fade-in/scale animations
- 🎯 Interactive form with validation
- 📊 Price analysis with metrics
- ⚡ Real-time predictions

## 📝 License
MIT License

## 👨‍💻 Author
**KRUSHNA**

Built with ❤️ using FastAPI, Streamlit & Scikit-learn

---

⭐ **If you found this project helpful, give it a star!**
