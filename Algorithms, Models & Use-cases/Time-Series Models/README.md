# 📈 Comprehensive Overview of Time-Series Models

This document presents a **comprehensive list of time-series models**, with an overview of each and a detailed comparative analysis of their strengths, limitations, and use cases.

---

## 🧩 Time-Series Models Overview

Below is a concise description of the most commonly used time-series forecasting models:

| Model | Brief Description |
| :--- | :--- |
| **ARIMA** (AutoRegressive Integrated Moving Average) | A statistical model that uses past values of the time series, past forecast errors, and differencing to capture trends, seasonality (with SARIMA), and correlation. |
| **Bagged ETS** | An **ensemble method** that generates multiple forecasts using bootstrap samples of the data and then averages them. It's often applied to the ETS model. |
| **BATS** (BATS and TBATS) | A complex exponential smoothing model designed for series with **multiple seasonal patterns** (e.g., daily and yearly) that also have non-integer seasonal periods or complex seasonal patterns. |
| **CNN** (Convolutional Neural Network) | A **Deep Learning** model primarily used for image processing but adapted for time series by treating data as a 1D sequence or 2D image. Excellent at learning local patterns. |
| **Croston** | A specialized statistical method for forecasting **intermittent demand** (when demand is zero for many periods, and non-zero demand occurs randomly). |
| **ETS** (Error, Trend, Seasonality) | Also known as **Exponential Smoothing**, it assigns exponentially decreasing weights to older observations and can handle additive or multiplicative trend and seasonality. |
| **Facebook Prophet** | A flexible, automated procedure for time series forecasting by Facebook. It uses a decomposable model with components for trend, seasonality, and holidays/events. |
| **Holt-Winters** | An extension of the ETS model that explicitly includes **trend and seasonality** components. Effective for series that exhibit both. |
| **Linear SVM** (Support Vector Machine) | A machine learning model (SVR - Support Vector Regression) that finds a hyperplane best fitting the data. Linear SVR uses a linear kernel. |
| **LSTM** (Long Short-Term Memory) | A **Recurrent Neural Network (RNN)** model that captures long-term dependencies and mitigates the vanishing gradient problem. Ideal for sequential data. |
| **MLP** (Multi-Layer Perceptron) | A **Neural Network** with one or more hidden layers. It’s a general-purpose function approximator for non-linear relationships. |
| **Naive** (Random Walk) | The simplest model — the forecast for the next period is simply the **last observed value** ($\hat{y}_{t+1} = y_t$). |
| **Neural Network** | A broad term for architectures (MLP, CNN, LSTM) inspired by the human brain. They learn non-linear data relationships through interconnected nodes. |
| **Random Forest** | An **ensemble learning** method that builds multiple decision trees and averages their outputs for regression/forecasting. |
| **RWF** (Random Walk Forecast) | Another name for the **Naive** forecasting method. |
| **Seasonal Naive** | The forecast for the next period equals the value from the **same period in the last season** ($\hat{y}_{t+h} = y_{t+h-m}$, where $m$ is the seasonal period). |
| **SES** (Simple Exponential Smoothing) | A simple ETS variant used for series with **no trend or seasonality**. Smooths only the level of the series. |
| **Spline** | A non-parametric method that fits piecewise low-degree polynomials to ensure smoothness at connection points (knots). Useful for curve fitting. |
| **StructTS** (Structural Time Series) | A **State Space Model** that decomposes time series into unobserved components like trend, seasonality, and irregular components. |
| **TBATS** (Trigonometric BATS) | Extends BATS with **trigonometric terms** to model complex seasonality more flexibly. |
| **TSLM** (Time Series Linear Model) | A **Multiple Linear Regression** model using time, trend, seasonality, or external factors (e.g., price, weather) as predictors. |
| **XGBoost** (eXtreme Gradient Boosting) | A scalable **Gradient Boosting Decision Tree** model that builds trees sequentially to minimize residual errors. |

---

## ⚖️ Comparative Analysis of Time-Series Models

The models can be broadly categorized into three groups:

- **Statistical / Econometric Models**
- **Machine Learning & Ensemble Models**
- **Neural Network / Deep Learning Models**

---

### I. 📊 Statistical / Econometric Models  
*(ARIMA, ETS, Holt-Winters, Naive, Seasonal Naive, StructTS, BATS/TBATS, Croston, SES, TSLM)*

| Model Type | Advantages (Pros) | Drawbacks (Cons) | Primary Use-Cases |
| :--- | :--- | :--- | :--- |
| **ARIMA / SARIMA** | **Highly interpretable**; strong mathematical foundation; excellent for **linear correlations**. | Requires **stationarity**; model selection (ACF/PACF) is **labor-intensive**; struggles with non-linear patterns. | **Univariate forecasting**; economic or financial time series. |
| **ETS / Holt-Winters / SES** | **Simple, robust**, and data-efficient; handles **trend & seasonality** automatically. | Limited to specific functional forms; **weak for long-term forecasts**; cannot handle exogenous variables. | Retail demand; short-term planning; baseline comparisons. |
| **Naive / Seasonal Naive / RWF** | **Fast and simple**; excellent **benchmark models**; often surprisingly accurate for seasonal or volatile data. | **No explanatory power**; fails on trending data; too simplistic for complex patterns. | Baseline forecasts; volatile or highly seasonal data. |
| **BATS / TBATS** | Handles **multiple complex seasonalities** and non-integer periods; fully automated. | **Computationally heavy**; less interpretable; not standard in all libraries. | Hourly/daily/weekly seasonal data; long-term demand. |
| **Croston** | **Best for intermittent demand** (sporadic data). | **Not suitable** for continuous demand. | Inventory & spare parts forecasting. |
| **StructTS** | Clean decomposition via **State Space Models**; handles missing data. | Less commonly used; **complex parameter interpretation**. | Structural decomposition; smoothing/filtering. |
| **TSLM** | **Interpretable regression-based** approach; can include **external regressors**. | Assumes **linear relationships**; needs careful feature selection. | Marketing, pricing, and promotion forecasting. |

---

### II. 🤖 Machine Learning & Ensemble Models  
*(Random Forest, XGBoost, Linear SVM, Facebook Prophet, TSLM, Bagged ETS)*

| Model Type | Advantages (Pros) | Drawbacks (Cons) | Primary Use-Cases |
| :--- | :--- | :--- | :--- |
| **Random Forest / XGBoost** | Captures **complex non-linear relationships**; **robust to outliers**; feature importance insights. | Requires **lag feature engineering**; poor extrapolation; less interpretable. | Forecasting with exogenous variables; long-term stable data. |
| **Facebook Prophet** | **User-friendly**; automated trend/seasonality handling; integrates **holidays and events** easily. | Less accurate for simple linear series; may **overfit** if poorly tuned. | Business operations; demand spikes; event-driven data. |
| **Bagged ETS** | Reduces variance and **improves forecast stability**. | **Higher computation time**; inherits ETS limitations. | Short-term forecasting; improving ETS accuracy. |
| **Linear SVM (SVR)** | Great for **high-dimensional data**; **generalizes well**. | Parameter tuning is crucial; **slow training**; needs lagged features. | Financial forecasting; datasets with multiple predictors. |

---

### III. 🧠 Neural Network & Deep Learning Models  
*(MLP, CNN, LSTM, Neural Network)*

| Model Type | Advantages (Pros) | Drawbacks (Cons) | Primary Use-Cases |
| :--- | :--- | :--- | :--- |
| **LSTM / RNN** | **State-of-the-art** for sequence modeling; captures **long-term dependencies** without manual feature engineering. | **Data-hungry**; **black box**; computationally expensive; prone to overfitting. | High-frequency data; sensor signals; volatility forecasting. |
| **CNN** | Learns **local features** efficiently; faster than LSTMs for short sequences. | Weak for long-term dependencies; needs large data. | Signal processing; pattern extraction in short sequences. |
| **MLP / Neural Network** | Flexible non-linear modeling; can approximate any function with sufficient data. | Requires supervised transformation; less effective for sequential data; **risk of local minima**. | Non-linear regression; combined models with domain features. |

---

## 🧾 Summary

| Category | Best For | Typical Examples |
| :--- | :--- | :--- |
| **Statistical Models** | Interpretable, low-data, short-term forecasts | ARIMA, ETS, Holt-Winters |
| **Machine Learning Models** | Tabular + exogenous features, moderate data | XGBoost, Random Forest, Prophet |
| **Deep Learning Models** | Complex patterns, high-frequency data | LSTM, CNN, MLP |

---

### 🧠 Pro Tip:
Always start with **simple baseline models** (Naive, ETS, ARIMA), evaluate performance, and only then move to **advanced ML/DL models** if justified by complexity or accuracy requirements.

---
