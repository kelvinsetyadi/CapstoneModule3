# CapstoneModule3

# 🏡 California Housing Price Prediction Model

Repositori ini berisi proyek Machine Learning untuk memprediksi harga rumah di California berdasarkan fitur geografis dan demografis. Model utama yang digunakan adalah **XGBoost Regressor** dengan transformasi logaritmik pada target, preprocessing pipeline, serta hyperparameter tuning.

---

## 📊 Tujuan Proyek

Membangun model prediksi harga rumah untuk:
- Membantu stakeholder atau pengembang properti mengambil keputusan berbasis data.
- Memberikan estimasi harga rumah secara cepat berdasarkan karakteristik lokasi dan properti.
- Menunjukkan pengaruh fitur-fitur seperti income, lokasi, dan jumlah kamar terhadap harga rumah.

---

## 🧾 Dataset

- Dataset: [California Housing Dataset]
- Jumlah observasi: 14.448 baris
- Fitur penting:
  - `longitude`, `latitude`
  - `housing_median_age`
  - `total_rooms`, `total_bedrooms`
  - `population`, `households`
  - `median_income`
  - `ocean_proximity`
- Target: `median_house_value` 

---

## 📌 Proses Pengolahan

### 1. Exploratory Data Analysis (EDA)
- Distribusi harga rumah berskew ke kanan → dilakukan log-transform.
- Median income memiliki korelasi positif paling kuat dengan harga rumah.
- Outliers ekstrem dihapus untuk meningkatkan performa model dan mencegah overfitting.

### 2. Preprocessing
- Fitur numerik → Imputasi & scaling (StandardScaler)
- Fitur kategorik (`ocean_proximity`) → OneHotEncoding
- Target (`median_house_value`) → log-transformed untuk distribusi yang lebih normal

### 3. Modeling
- Model utama: **XGBoostRegressor**
- Dibungkus dengan `TransformedTargetRegressor` untuk log-transform target
- Dibuat pipeline bersama preprocessor

### 4. Hyperparameter Tuning
- RandomizedSearchCV (n_iter = 50, cv = 5)
- Parameter yang di-tune: max_depth, n_estimators, learning_rate, subsample, colsample_bytree, reg_alpha, reg_lambda, gamma

---

## 🧪 Evaluasi Model

### Metrik Evaluasi:
- **RMSE (Root Mean Squared Error)** – mengukur kesalahan absolut dengan penekanan pada outliers
- **MAE (Mean Absolute Error)** – rata-rata kesalahan absolut
- **MAPE (Mean Absolute Percentage Error)** – akurasi relatif dalam persentase

### Hasil Sebelum dan Setelah Tuning:

| Metric | Sebelum Tuning | Setelah Tuning |
|--------|----------------|----------------|
| RMSE   | 69702.12       | 46248.96       |
| MAE    | 50767.24       | 34244.59       |
| MAPE   | 26.59%         | 17.49%         |

---


