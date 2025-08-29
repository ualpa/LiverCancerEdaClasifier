# LiverCancerEdaClasifier

This project explores a **synthetic, medically realistic** dataset (5,000 rows, 14 columns) to:
- Perform an **Exploratory Data Analysis (EDA)** of a synthetic liver cancer dataset (demographics, lifestyle, biomarkers).  
- Build and compare multiple **classification models** to determine the most accurate approach for liver cancer risk prediction.  
- Deliver an interactive **Streamlit application** to present results and predictions, enhanced with **SHAP-based explanations** for interpretability.  

## Dataset

- **Source:** [Synthetic Liver Cancer Dataset (CSV)](https://www.kaggle.com/datasets/miadul/predict-liver-cancer-from-and-clinical-features?resource=download)  
- **Size:** 5,000 rows × 14 columns  
- **License:** CC0 (public domain, safe for academic/commercial use)  

### Columns description
- `age` — Patient's age in years (30–85).  
- `gender` — Gender of the patient (Male, Female).  
- `bmi` — Body Mass Index (16–45).  
- `alcohol_consumption` — Alcohol use: Never, Occasional, Regular.  
- `smoking_status` — Smoking behavior: Never, Former, Current.  
- `hepatitis_b` — Presence of Hepatitis B infection (0 = No, 1 = Yes).  
- `hepatitis_c` — Presence of Hepatitis C infection (0 = No, 1 = Yes).  
- `liver_function_score` — Simulated liver function score (0–100).  
- `alpha_fetoprotein_level` — AFP biomarker levels in ng/mL.  
- `cirrhosis_history` — Past history of liver cirrhosis (0 = No, 1 = Yes).  
- `family_history_cancer` — Family history of cancer (0 = No, 1 = Yes).  
- `physical_activity_level` — Low, Moderate, High.  
- `diabetes` — Presence of diabetes (0 = No, 1 = Yes).  
- `liver_cancer` — Target variable: 0 = No Cancer, 1 = Has Liver Cancer.  

