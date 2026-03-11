import streamlit as st
import pandas as pd

# Title and description of the deployment app
st.title("Early Warning Food Price Monitor - Northeast Nigeria")
st.write("This tool forecasts retail food prices three months ahead for five key commodities across Adamawa, Borno, and Yobe — three conflict-affected states in Northeast Nigeria where food insecurity is most acute. Three months of advance warning is not just a number. It is enough time for policymakers, traders, aid organisations and food security agencies to see what is coming and act before the crisis arrives.")

#reading in the needed datasets
model_comparison = pd.read_csv('data/model data/model_comparison_final.csv')
best_models = pd.read_csv('data/model data/best_model_per_combination.csv')
prophet_horizons = pd.read_csv('data/model data/prophet_horizon_results.csv')
xgb_horizons = pd.read_csv('data/model data/xgb_horizon_results.csv')

# creating sidebar for navigation
page = st.sidebar.selectbox(
  "Navigate",
  ["Model Comparison", "Forecast Explorer"]
)

# -- CREATING PAGE 1 AND PAGE 2 --
if page == "Model Comparison":
  st.header("Model Comparison")
  st.subheader("All Model Results")
  st.dataframe(model_comparison)
  st.subheader("Best Model Per Combination")
  st.write("The table below shows the wnning forecasting model for each state and commodity combination, selected based on lowest average MAPE across all three forecast horizons.")
  st.dataframe(best_models)

elif page == "Forecast Explorer":
  st.header("Forecast Explorer")
  state = st.selectbox(
    "Select a State",
    ["Adamawa", "Borno", Yobe]
  )

  commodity = st.selectbox(
    "Select a Commodity",
    ["Rice (imported)", "Rice (local)", 
     "Beans (white)", "Yam", "Tomatoes"]
  )

  filtered_best = best_models[
    (best_models['state'] == state) & (best_models['commodity'] == commodity) 
  ]

   
