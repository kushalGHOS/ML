import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('random_forest_carsellModel.pkl', 'rb'))

# from joblib import load

# # Load the large dataset
# model = load('CarModel.joblib')

# Use the loaded data as needed


def main():
    st.title('Car Selling Prediction ')

    Year=st.text_input('Year')
    Present_price=st.text_input('Present_price')
    Kms_driven=st.text_input('Kms_driven')
    Owner=st.text_input('Owner')
    Fuel_Type_Diesel=st.text_input('Fuel_Type_Diesel')
    Fuel_Type_Petrol=st.text_input('Fuel_Type_Petrol')
    Seller_Type_Individual=st.text_input('Seller_Type_Individual')
    Transmission_Manual=st.text_input('Transmission_Manual')
    

    features=[Year, Present_price,Kms_driven,Owner,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]
    features = np.array(features).reshape(1, -1)
    if st.button("Predict"):
      prediction =model.predict(features)
      if prediction>0:
         output=round(prediction[0],2) 
         st.success('you can sell your car for {}'.format(output))
      else:
         st.warning('you cant sell your car')
    

if __name__=='__main__':
    main()