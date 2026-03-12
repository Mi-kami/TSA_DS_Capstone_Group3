## Problem Statement and Objectives

### Problem Statement

Food price volatility remains one of the most significant threats to food security and economic stability in Nigeria. Prices of staple commodities such as rice, maize and beans fluctuate sharply due to a combination of macroeconomic shocks, transportation costs, seasonal harvest cycles and conflict-related disruptions in agricultural regions. This volatility intensified following the removal of the petrol subsidy in June 2023, which created a structural break in Nigerian food markets and pushed prices to historically unprecedented levels. The consequences are severe for low-income households that spend a large proportion of their income on food, as well as for traders, farmers and policymakers who must make economic decisions under conditions of extreme uncertainty. Despite the scale of this challenge, existing food price monitoring systems in Nigeria are largely retrospective, reporting prices only after market changes have already occurred and providing little capacity to anticipate future price movements. As a result, government interventions such as food imports, subsidies and emergency assistance are typically implemented only after food price spikes have already harmed vulnerable populations. This project addresses this gap by developing a data-driven forecasting system capable of predicting monthly retail prices for key staple commodities across multiple Nigerian states up to three months in advance. By combining classical time series models with modern machine learning techniques, the system aims to provide forward-looking price intelligence that can support early warning systems, improve market planning and enable more proactive responses to food price instability.

### Research Questions

RQ1: Which forecasting model: ARIMA, SARIMA, XGBoost or Prophet, produces the most accurate predictions of monthly retail food prices across Nigerian states?

RQ2: How does forecast accuracy change across different prediction horizons of one, two and three months ahead?

RQ3: Which commodity–state combinations produce sufficiently reliable forecasts to support operational deployment in a food price early warning system?

### Project Objectives

1. To collect and preprocess monthly food price and economic indicator data covering January 2017 to December 2024 for five key commodities: rice, maize, beans, yam and tomatoes, across 13 Nigerian states.

2. To integrate multiple drivers of food price movement, including macroeconomic indicators, rainfall patterns, fuel prices, import volumes and conflict events, into a unified modelling dataset.

3. To develop and train four forecasting models: ARIMA, SARIMA, XGBoost, and Prophet, capable of generating 1-month, 2-months and 3-months ahead of retail food prices predictions.

4. To evaluate and compare model performance against a naive baseline forecast using quantitative error metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

5. To generate policy-relevant insights and recommendations demonstrating how short-term food price forecasting can support early warning systems and improve decision-making for traders, farmers and government agencies.

### Project Significance

Food price instability directly threatens the welfare of millions of Nigerian households who depend on affordable staple foods for daily consumption. A reliable forecasting system would enable policymakers and humanitarian organisations to anticipate price spikes and implement interventions before food insecurity worsens. By transforming historical price monitoring into forward-looking market intelligence, this project demonstrates how data-driven forecasting can strengthen Nigeria’s capacity to respond proactively to food price shocks. In the long term, such systems could contribute to more stable food markets and improved resilience for vulnerable populations.
