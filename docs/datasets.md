*Datasets for Big Data Class Project*

This file provides **direct download sources** for datasets categorized under **Health, Commerce, and Climate**.  

Each group should choose/pick one datasets from these links and store them in the appropriate folder structure:  
All datasets contain **millions of records**, suitable for distributed processing and analysis in Spark, Dask, or Hadoop environments.  

data/
  health/
      raw/
      cleaned/
  commerce/
      raw/
      cleaned/
  climate/
      raw/
      cleaned/


Each group will:
1. **Download** raw datasets (store in `/data/<domain>/raw/`).
2. **Clean & preprocess** (store cleaned data in `/data/<domain>/cleaned/`).
3. **Use the same data throughout Weeks 3–12** of the project. check course content for details

---

## GROUP 1 — HEALTH DATA

### 1. MIMIC-IV Clinical Database
- **Description:** De-identified electronic health records of over 70,000 ICU patients.  
- **Rows:** ~40 million event-level records.  
- **Link:** https://physionet.org/content/mimiciv/3.0/  
- **Access:** Requires free PhysioNet credential (student can register).

### 2. CORD-19 (COVID-19 Open Research Dataset)
- **Description:** Over 280,000 scholarly articles related to COVID-19, SARS-CoV-2, and related coronaviruses.  
- **Rows:** Millions of text paragraphs; ideal for NLP and similarity experiments.  
- **Link:** https://www.semanticscholar.org/cord19  

### 3. Global Health Data Exchange (GHDx)
- **Description:** Health indicators and surveys from over 200 countries.  
- **Rows:** Hundreds of millions of structured and demographic entries.  
- **Link:** https://ghdx.healthdata.org/  

---

## GROUP 2 — COMMERCE DATA

### 1. Instacart Online Grocery Shopping Dataset
- **Description:** 3.4 million orders from 200,000 users and 50,000 products.  
- **Link:** https://www.instacart.com/datasets/grocery-shopping-2017  
- **Use:** Transaction-level ETL, similarity analysis, recommendation modeling.

### 2. RetailRocket E-commerce Dataset
- **Description:** 2.7 million user interactions (views, add-to-cart, purchases).  
- **Link:** https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset  

### 3. M5 Forecasting — Walmart Sales
- **Description:** 42,840 products × 6 years of daily sales data.  
- **Link:** https://www.kaggle.com/competitions/m5-forecasting-accuracy/data  
- **Use:** Time series forecasting, sales pattern similarity, and clustering.


---

## GROUP 3 — CLIMATE DATA

### 1. NOAA Global Surface Summary of the Day (GSOD)
- **Description:** Daily weather summaries from 9,000+ stations worldwide since 1929.  
- **Rows:** >100 million records.  
- **Link:** https://www.ncei.noaa.gov/data/global-summary-of-the-day/  

### 2. NASA Earth Observations (NEO)
- **Description:** Global climate and environmental indicators (temperature, rainfall, CO₂, ozone, etc.).  
- **Rows:** Millions of gridded observations across multiple years.  
- **Link:** https://neo.gsfc.nasa.gov/  

### 3. Berkeley Earth Surface Temperature Data
- **Description:** Comprehensive temperature records dating back to the 18th century.  
- **Rows:** ~1.6 billion data points across land and ocean datasets.  
- **Link:** http://berkeleyearth.org/data/  

### 4. ERA5 Reanalysis (European Centre for Medium-Range Weather Forecasts)
- **Description:** Hourly climate data combining models and observations.  
- **Rows:** Billions of grid points for global weather patterns.  
- **Link:** https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels  

---

## DATA STORAGE STRUCTURE



 **Instruction**: Download datasets manually, place them into the correct raw/ folder, and process cleaned versions into cleaned/.

