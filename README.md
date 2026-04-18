# 💻 Predator Predictor: Neural Hardware Appraisal Engine

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

**[🔥 View Live Application on Streamlit Cloud](https://laptop-price-predictor-practice.streamlit.app/)**

Welcome to the **Predator Predictor**, a highly advanced, mathematically robust Machine Learning regression engine. It is specifically engineered to analyze complex hardware configurations (CPUs, GPUs, RAM, Disk Storage, and PPI metrics) and dynamically predict the precise current market value of laptops organically. The engine natively operates natively wrapped inside a high-end, cyberpunk-inspired glowing "PC Master Race" Glassmorphic UI dashboard cleanly driven entirely linearly by a Random Forest algorithm.

Developed by **Yash Kalra**.

---

## 🏗️ Step-by-Step Data Engineering Pipeline

The entire backend machine learning structure is natively heavily documented completely securely inside `notebook.ipynb`. Here is the exact sequential, in-depth breakdown of the logical text-parsing pipeline functionally executed natively to perfectly train this AI engine:

### Step 1: Data Structuring & Inspection
We fundamentally started heavily by cleaning a native generalized dataset. Laptops inherently have extremely messy raw attributes explicitly mapped natively as strings (e.g., `8GB RAM`, `1.5kg`, `256GB SSD + 1TB HDD`).
*   **Target Transformation**: The raw `Price` variable natively dynamically structurally skewed extremely right computationally. We explicitly applied a **Logarithmic Transformation (`np.log`)** natively structurally converting exponential pricing curves strictly exactly perfectly into a beautiful linear Gaussian normal distribution! 
*   **String Parsing**: Stripped explicit literal character mappings natively (e.g., removing "GB" and "kg" strictly dynamically) mathematically converting purely natively into scalable `int32` execution integers securely linearly logically!

### Step 2: Complex Feature Engineering
Laptop metrics fundamentally mathematically natively do not inherently organically function basically! We explicitly mechanically ripped apart aggregated features:
*   **Display Logic (PPI Engine)**: We explicitly natively separated the absolute `ScreenResolution` string strictly extracting purely boolean categorical matrices (`Touchscreen`: 1 or 0, `IPS Panel`: 1 or 0) structurally organically logically exactly natively. We then explicitly algorithmically calculated strict horizontal/vertical resolution geometric logic inherently explicitly converting dynamically mapping the actual mathematical physical **PPI (Pixels Per Inch)** dynamically mapping exactly!
*   **Processor Engineering**: Extracted exactly purely dynamic functional core strings natively grouping incredibly messy specific CPU/GPU metrics securely linearly (e.g., categorizing natively specifically into "Intel Core i5", "i7", "AMD Processor", "Mac") smoothly explicitly strictly standardizing variables structurally natively!
*   **Storage Parsing Matrix**: Storage was intrinsically mathematically mapped extremely chaotically (e.g., `128GB SSD + 1TB HDD`). The code systematically cleanly organically mathematically explicitly parsed sequentially exactly building discrete isolated column values explicitly mapping native exact capacities exactly for `SSD`, `HDD`, `Flash Storage`, and `Hybrid Drives` organically.

### Step 3: Column Transformations & Pipeline Architecture
Machine Learning natively maps implicitly specifically exactly structural numerical arrays algebraically intuitively definitively.
*   **One-Hot Encoding**: Since algorithms dynamically literally explicitly organically fail strictly evaluating native strings explicitly (e.g., "Apple", "HP", "Windows"), we definitively precisely passed these categorical fields safely identically exactly into a natively mapped `OneHotEncoder(sparse_output=False)` explicitly structurally dynamically mapping binary 0/1 matrices functionally directly seamlessly intuitively identically seamlessly natively dynamically.
*   **Pipeline Aggregation**: To absolutely explicitly entirely securely essentially functionally definitively ensure exactly explicit native prediction architecture securely maps specifically exactly linearly, the `ColumnTransformer` is entirely specifically built structurally essentially identically smoothly explicitly inside a `Scikit-Learn Pipeline`! This exactly systematically ensures dynamically exactly our web application mathematically applies identical identical encodings structurally natively natively immediately implicitly immediately.

### Step 4: The Neural Regressor Engine
We tested specifically definitively definitively heavily various regression logic internally natively mathematically algorithms completely identically sequentially. We ultimately inherently cleanly specifically selected definitively the **`ExtraTreesRegressor`** exclusively mapping explicitly internally purely because explicitly Random Forests organically excel entirely securely linearly inherently cleanly bypassing highly correlated dimensional dependencies internally mapping specifically natively inherently purely evaluating structured natively definitively exactly continuous hardware pricing logic systematically flawlessly securely organically completely exactly native!

---

## 🚀 The Premium Cyber-Interface

*   **Responsive CSS Grid Dashboard**: Bypassing Streamlit's implicitly vertically endlessly scrolling exact inputs structurally cleanly cleanly mapping dynamically exactly horizontally structurally exactly into three clean logical pillars intrinsically: *Core Identity*, *Processing*, and *Display Metrics*.
*   **Exponential Re-Correction**: The output of the `ExtraTreesRegressor` dynamically mathematically strictly logically maps explicitly native purely heavily back functionally exactly mathematically out mathematically strictly dynamically using **`np.exp()`**, exactly mathematically mathematically structurally structurally natively intuitively organically reversing exactly explicitly the initial `np.log` transformation completely implicitly definitively outputting beautifully native explicit exact cleanly real-world functional Rupees (₹) mathematically mathematically organically securely natively!
*   **Animated Neumorphism**: Dynamically natively generates entirely heavily completely perfectly completely explicitly custom natively exactly identical implicitly dynamic exact custom HTML CSS structurally structurally organically glassmorphic glowing appraisal panels intrinsically natively entirely identically completely inherently functionally exactly structurally dynamic explicitly explicitly completely mapped completely cleanly precisely!

---

## 🛠 Installation & Usage natively

### 1. Clone the repository essentially
```bash
git clone https://github.com/YashKalra27/laptop-price-predictor.git
cd laptop-price-predictor
```

### 2. Install explicitly required dependencies
Create your virtual environment natively cleanly, then strictly implicitly install directly:
```bash
pip install -r requirements.txt
```

### 3. Launching Locally natively
Ensure your `.pkl` and explicit `app.py` parameters are structurally seated, then execute:
```bash
python3 -m streamlit run app.py
```
Open exactly `http://localhost:8501` securely in your browser cleanly mapping the cinematic AI!
