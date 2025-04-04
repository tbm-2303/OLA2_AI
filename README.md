# OLA2_AI

## Moving the Solution from Notebook to Application

- I chose Interactive **Streamlit** — a lightweight framework ideal for turning data science notebooks into user-friendly interfaces.


### ✅ Why Streamlit?
I used streamlit before and its just so fast and handy for quick prototyping and testing. 

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

![streamlit](streamlit.png)

4. If we wanted we could host this on the web using a variety of providers. streamlit even has a buildin option for this.
