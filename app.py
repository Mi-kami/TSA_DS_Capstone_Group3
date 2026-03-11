import streamlit as st
import pandas as pd

# Title and description of the deployment app
st.title("Early Warning Food Price Monitor - Northeast Nigeria")
st.write("This tool forecasts retail food prices three months ahead for five key commodities across Adamawa, Borno, and Yobe — three conflict-affected states in Northeast Nigeria where food insecurity is most acute. Three months of advance warning is not just a number. It is enough time for policymakers, traders, aid organisations and food security agencies to see what is coming and act before the crisis arrives.")

#reading in the needed datasets
model_comparison = pd.read_csv('data/model_data/model_comparison_final.csv')
best_models = pd.read_csv('data/model_data/best_model_per_combination.csv')
prophet_horizons = pd.read_csv('data/model_data/prophet_horizon_results.csv')
xgb_horizons = pd.read_csv('data/model_data/xgb_horizon_results.csv')

# creating sidebar for navigation
page = st.sidebar.selectbox(
  "Navigate",
  ["Model Comparison", "Forecast Explorer"]
)

# -- CREATING PAGE 1 AND PAGE 2 --
# page 1
if page == "Model Comparison":
  st.header("Model Comparison")
  st.subheader("All Model Results")
  st.dataframe(model_comparison)
  st.subheader("Best Model Per Combination")
  st.write("The table below shows the wnning forecasting model for each state and commodity combination, selected based on lowest average MAPE across all three forecast horizons.")
  st.dataframe(best_models)

#page 2
elif page == "Forecast Explorer":
  st.header("Forecast Explorer")
  # dropdown with state options
  state = st.selectbox(
    "Select a State",
    ["Adamawa", "Borno", "Yobe"]
  )

  # dropdown with commodity options
  commodity = st.selectbox(
    "Select a Commodity",
    ["Rice (imported)", "Rice (local)", 
     "Beans (white)", "Yam", "Tomatoes"]
  )

  #filters the model to get the dataset that the user prompted
  filtered_best = best_models[
    (best_models['state'] == state) & (best_models['commodity'] == commodity) 
  ]

  if len(filtered_best) == 0:
    st.warning("No results found for this combination.")
  else:
    st.success(f"Best model for {commodity} in {state}: {filtered_best['best_model'].values[0]}")
    best_model_name = filtered_best['best_model'].values[0]

    filtered_metrics = model_comparison[
      (model_comparison['state'] == state) & 
      (model_comparison['commodity'] == commodity) &
      (model_comparison['best_model'] ==  best_model_name)
    ]
  
    st.subheader("Model Performance Metrics")
    st.dataframe(filtered_metrics[['best_model', 'MAPE', 'MAE', 'RMSE', 'H1_MAPE', 'H2_MAPE', 'H3_MAPE']])

    if best_model_name == "Prophet":
      price_data = prophet_horizons[
        (prophet_horizons['state'] == state) &
        (prophet_horizons['commodity'] == commodity)
      ]
    elif best_model_name == "XGBoost":
      price_data = xgb_horizons[
        (xgb_horizons['state'] == state) &
        (xgb_horizons['commodity'] == commodity)
      ]
    elif best_model_name == "SARIMA":
      price_data = prophet_horizons[
        (prophet_horizons['state'] == state) &
        (prophet_horizons['commodity'] == commodity)
      ]
      st.info("Note: SARIMA does not support 3-month forecasts. Showing Prophet predictions for this combination.")
    

    latest_date = price_data['date'].max()

    recent_predictions = price_data[
      price_data['date'] == latest_date
    ].sort_values('horizon')

    recent_predictions = recent_predictions[
      ['horizon', 'actual', 'predicted', 'error_pct']
    ].rename(columns={
            'horizon'   : 'Months Ahead',
            'actual'    : 'Actual Price (NGN)',
            'predicted' : 'Predicted Price (NGN)',
            'error_pct' : 'Error (%)'
        })

    st.subheader("Predicted Prices - 3 Months Ahead")
    st.dataframe(recent_predictions)
    
    
    

   
