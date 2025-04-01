## Project Objective
The objective of this project was to develop a **binary classifier** trained and tested on **self-collected** data obtained via web scraping. Additionally, the project aimed to provide experience in **data processing and preparation**, including handling incomplete or corrupted data. Finally, the project also focused on exploring **machine learning model optimization techniques**.

---

## Data
The dataset consists of applications from **Google Play**. To collect the data, I developed a **[custom scraper](https://github.com/wiktork77/Google-Play-App-Scraper)**, which utilizes an **[external scraper](https://github.com/facundoolano/google-play-scraper)** written by **[facundoolano](https://github.com/facundoolano)**.

The scraper outputs raw data into the file **`raw_data/apps_data.csv`**, which is then processed to generate **`raw_data/apps_data_complete.csv`**. The latter serves as the final dataset used for training and testing the model.

### **Model Input - Feature Vector:**
- Number of installs
- Google Play score
- Number of score ratings
- Number of reviews
- Probability of being a paid app within its category

### **Model Output - Prediction:**
- **Paid or free** classification of the app

---

## Model Training
The entire process, from **data analysis** to **model training** and **optimization**, is documented in the provided Jupyter **[notebook](model.ipynb)** as well as in the project documentation:
- 📄 [**Documentation**](documentation/Documentation.pdf)
- 📄 [**Documentation (Polish)**](documentation/Documentation_Polish.pdf)

---

## Optimization
An optimization script is available to fine-tune the model based on the **F1 score**. The script can be found at **`optimizers/rbf_opt.py`**.

🔧 **Optimization Process:**
- The script evaluates different **gamma** and **C** parameter values.
- For a given **gamma** value, the script iterates over a **predefined set** of **C** values.
- The exact formula for **C values** and details about the optimization process are described in **[Documentation, Section 5.5](documentation/Documentation.pdf)**.

---

## Running the Project
### **Prerequisites:**
- **Python 3.10 or later is required**
- **Recommended version: Python 3.10.9**

### **Running the Jupyter Notebook**
Navigate to the project’s root directory and execute the following commands:
```bash
pip install -r requirements.txt
jupyter notebook model.ipynb
```
📌 **Note:** **You can also open the notebook to read it and see the results of my calculations on github by clicking on `model.ipynb` or [here](model.ipynb)**

### **Running the Optimizer Script**
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Navigate to the **`optimizers`** directory.
3. Run the optimization script:
```bash
python rbf_opt.py [gamma]
```
📌 **Note:** `gamma` is a numerical value representing a model parameter. The script evaluates different values of **C** for the given `gamma`. 

📝 **Results** are saved in the **`optimizers/data`** folder under filenames corresponding to the selected `gamma` value.
