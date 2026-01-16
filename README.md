🚗 FastAPI Car Price Predictor
Description
An AI-powered Car Price Prediction System built with FastAPI and Streamlit, offering real-time used car price estimation using Machine Learning. This full-stack application combines a robust REST API backend with a stunning, modern, animated frontend interface.

✨ Features
-🤖 Machine Learning Model: Random Forest Regressor with 500+ estimators for accurate price predictions
-🚀 FastAPI Backend: High-performance REST API with automatic documentation (Swagger/OpenAPI)
-🎨 Beautiful Streamlit Frontend: Modern UI with smooth animations, gradient backgrounds, and interactive elements
-📊 Real-time Predictions: Get instant car price estimates in under 1 second
-📈 Detailed Analytics: View depreciation rates, average kilometers per year, and car age metrics
-🔒 Type Safety: Pydantic schemas for robust data validation
-💾 Persistent Model: Pre-trained model with feature alignment for consistent predictions
-📱 Responsive Design: Works seamlessly on desktop and mobile devices


🛠️ Tech Stack
-Backend:
  FastAPI (REST API framework)
  Scikit-learn (Machine Learning)
  Pandas & NumPy (Data processing)
  Pydantic (Data validation)
  Joblib (Model serialization)
  
-Frontend:
  Streamlit (Web UI)
  Custom CSS with animations
  Google Fonts (Poppins)
  Gradient backgrounds & glassmorphism
  
-Model:
  Random Forest Regressor
  One-hot encoding for categorical features
  Feature alignment for production deployment


📂 Project Structure:-

fastapi_car_price/
│
├── car_price_api/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application & routes
│   │   ├── model.py          # ML model loading & prediction logic
│   │   └── schemas.py        # Pydantic models for validation
│   │
│   ├── cardekho_data (1).csv # Training dataset
│   ├── train.py              # Model training script
│   ├── random_forest_model.pkl        # Trained ML model
│   ├── feature_columns.pkl   # Feature columns for alignment
│   └── requirements.txt      # Python dependencies
│
├── streamlit_app.py          # Frontend UI application
└── .venv/                    # Virtual environment


🚀 Quick Start



































































































































