# 🎓 Student Performance Prediction System

A full-stack Machine Learning application that predicts student **Performance Index** based on academic and lifestyle factors using a trained regression model, FastAPI backend, and modern interactive frontend.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Project Overview

This system predicts student performance using key academic and lifestyle indicators:
- **Hours Studied**
- **Previous Scores**
- **Extracurricular Activities**
- **Sleep Hours**
- **Sample Question Papers Practiced**

The trained ML model achieves **R² ≈ 0.988** with minimal error rates, deployed via FastAPI for real-world usage.

---

## ✨ Features

- 🤖 **High-Accuracy ML Model** - Regression-based prediction with R² score of 0.9884
- ⚡ **FastAPI Backend** - RESTful API with automatic documentation
- 🎨 **Interactive Frontend** - User-friendly interface for easy predictions
- 🔄 **CORS-Enabled** - Seamless browser integration
- 📊 **Swagger UI** - Built-in API testing interface
- 📈 **Low Error Rates** - MAE: 1.64, RMSE: 2.07

---

## 🧠 Model Performance

| Metric | Score |
|--------|-------|
| **R² Score (Test)** | 0.9884 |
| **Mean Absolute Error** | 1.64 |
| **Root Mean Squared Error** | 2.07 |
| **Training vs Test Gap** | Minimal (no overfitting) |

---

## 📊 Dataset Features

| Feature | Description | Type |
|---------|-------------|------|
| Hours Studied | Weekly study hours | Integer |
| Previous Scores | Last exam percentage | Integer (0-100) |
| Extracurricular Activities | Participation status | Binary (0/1) |
| Sleep Hours | Average daily sleep | Integer |
| Sample Papers Practiced | Practice papers solved | Integer |
| **Performance Index** | *Target variable* | Float |

---

## 🏗️ Project Structure
```
student-performance-predictor/
│
├── main.py                 # FastAPI backend server
├── student.pkl            # Trained ML model (serialized)
├── index.html             # Frontend interface
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
├── train_model.ipynb      # Training Code 
└── .gitignore             # Git ignore file
```

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.8+
- FastAPI
- Uvicorn
- Scikit-learn
- Joblib

**Frontend:**
- HTML
- CSS
- JavaScript

**Machine Learning:**
- Regression Model (Linear)
- Scikit-learn Pipeline

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/KALYANSAI-3114/Student_Performance_Prediction_System.git
cd student-performance-predictor
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start the FastAPI Server
```bash
uvicorn main:app --reload
```

Server runs at: **http://127.0.0.1:8000**

### 4️⃣ Access the Application

**Frontend:** Open `index.html` in your browser

**API Documentation:** http://127.0.0.1:8000/docs

**Alternative Docs:** http://127.0.0.1:8000/redoc

---

## 📡 API Usage

### Endpoint
```
POST /predict
```

### Request Example
```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [5, 80, 1, 7, 10]}'
```

### Request Body (JSON)
```json
{
  "features": [5, 80, 1, 7, 10]
}
```

**Order:** `[Hours Studied, Previous Scores, Extracurricular (0/1), Sleep Hours, Sample Papers]`

### Response
```json
{
  "prediction": 88.42
}
```

---

## 💻 Frontend Usage

1. Open `index.html` in a web browser
2. Enter student details in the form:
   - Hours Studied (e.g., 5)
   - Previous Scores (e.g., 80)
   - Extracurricular Activities (Yes/No)
   - Sleep Hours (e.g., 7)
   - Sample Papers Practiced (e.g., 10)
3. Click **"Predict Performance"**
4. View the predicted Performance Index

---

## 📈 Understanding Predictions

- **Performance Index:** Continuous value representing predicted academic performance
- **Range:** Typically 10-100, but may exceed 100 due to regression extrapolation
- **Interpretation:** Higher values indicate better predicted performance
- **Note:** Values >100 are mathematically valid in regression models

---

## 🎯 Use Cases

- 📚 **Academic Planning** - Identify factors affecting student performance
- 🏫 **Educational Analytics** - Data-driven insights for institutions
- 🎓 **Student Counseling** - Personalized improvement recommendations
- 💼 **ML Portfolio Project** - Demonstrate end-to-end ML deployment skills

---

## 🔮 Future Enhancements

- [ ] Deploy on cloud platforms (AWS/Azure/Heroku)
- [ ] Add performance category classification (Excellent/Good/Average)
- [ ] Implement model versioning and A/B testing
- [ ] Create database integration for prediction history
- [ ] Add user authentication system
- [ ] Dockerize the application
- [ ] Build mobile app version
- [ ] Implement real-time model retraining pipeline

---

## 🐛 Known Issues & Limitations

- Predictions may exceed 100 (mathematical behavior of regression)
- Model trained on specific dataset - performance may vary with different demographics
- No input validation on frontend (implement before production use)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


---

## 👨‍💻 Author

**A. Kalyan Sai**  
AI Full Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/KALYANSAI-3114)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/kalyan-sai-atchi-45539926a)

---

## 🙏 Acknowledgments

- Dataset inspiration from educational research
- FastAPI documentation and community
- Scikit-learn contributors
- Open-source ML community

---

## 📧 Contact

For questions or feedback:
- **Email:** kalyansai0909@gmail.com

---

<div align="center">

### ⭐ If you found this project helpful, please give it a star!

**Made with ❤️ and Python**

</div>
