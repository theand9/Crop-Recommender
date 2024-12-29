# **Predictive Yield**

### **Overview**
Predictive Yield is a precision agriculture tool designed to empower farmers by providing customized crop recommendations. It utilizes real-world data, such as soil quality, weather history, and crop yield trends, to suggest the most profitable and suitable crops. This project aims to digitize farming and improve agricultural productivity in India, starting with Maharashtra.

---

### **Features**
- **Customized Crop Recommendations**: Tailored to local soil and climatic conditions.
- **Data-Driven Insights**: Leverages 100+ years of weather data and 15+ years of crop yield data.
- **Farmer-Friendly Interface**: Generates PDF reports with actionable crop suggestions.
- **Weather Alerts**: Automated messaging system for rainfall and temperature changes.

---

### **Technologies Used**
- **Backend**: Python, Django
- **Frontend**: HTML, CSS (Bootstrap), JavaScript (jQuery, SASS)
- **Machine Learning**: TensorFlow, Keras, NumPy
- **Database**: SQLite (lightweight and Django-compatible)
- **APIs**:
  - Dark Sky (Weather)
  - Google Translate (Multilingual Support)
  - Fast2SMS (Messaging)

---

### **System Architecture**
- **Frontend**: User interface for farmers and admins.
- **Backend**: Powered by Django, integrated with APIs for data processing.
- **Database**: Stores soil, rainfall, and crop data for 44,000+ villages.
- **Machine Learning Model**: Deep Neural Network (6 layers) with ELU activation and Adam optimizer.

Refer to the *System Architecture diagram* in the documentation for detailed workflows (page 10).

---

### **Setup and Installation**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/predictive-yield.git
   cd predictive-yield
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Database**
   - The project uses SQLite. The initial database schema is included in the repository.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

4. **Add API Keys**
   - Create a `.env` file with the following variables:
     ```
     DARK_SKY_API_KEY=your_key
     GOOGLE_TRANSLATE_API_KEY=your_key
     FAST2SMS_API_KEY=your_key
     ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   - Deploy on localhost and launch in your browser.

---

### **Usage**
1. **Input**: Enter details about soil type, temperature, humidity, and rainfall.
2. **Processing**: The system predicts profit per hectare using trained ML models.
3. **Output**: Download a PDF report with recommended crops tailored to your inputs.

---

### **Limitations**
- Currently supports only Maharashtra, India.
- Requires stable internet connectivity.
- Lacks on-field IoT-based data collection.

---

### **Future Scope**
1. Expand coverage across India.
2. Develop mobile apps for Android and iOS platforms.
3. Integrate IoT devices for real-time crop and soil monitoring.
4. Incorporate satellite imagery for enhanced analysis.
