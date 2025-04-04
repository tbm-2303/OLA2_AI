# OLA2_AI

## Moving the Solution from Notebook to Application

- Interactive web application using **Streamlit** — a lightweight framework ideal for turning data science notebooks into user-friendly interfaces.

### ✅ Why Streamlit?

- **Fast Prototyping**
- **User-Friendly**
- **Perfect for ML Demos**: Seamlessly integrates with Python and supports real-time predictions.

### 🛠️ What We Did

1. **Trained and Saved the Model**  
   I selected the best-performing Random Forest model (Tuned 444) and saved it using `joblib`:

   ```python
   joblib.dump(rf_13, 'diabetes_model.pkl')

2. **Wrap solution in local prototype app**

3. **Lanch it locally**

4. **Deploy using python friendly hosting options or maybe streamlit cloud(build in option)**