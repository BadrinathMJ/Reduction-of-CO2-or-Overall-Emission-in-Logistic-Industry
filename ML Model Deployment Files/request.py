import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url, json={'year':, 'Jet Fuel_avi_BTU':, 'Gasoline_avi_BTU':, 'LDV_SWB_road_BTU':,
       'LDV_LWB_road_BTU':, 'Combination_Truck_road_BTU':, 'Bus_Road_BTU':,
       'Passenger_Car_EFF':, 'Passenger_Car_Age':,
       'Demand_Petro':,
       'Avg_MC':, 'CO2_emission_million_metric_tons':,
       'CO_emission_million_shots_tons':, 'NOx_emission_million_shots_tons':,
       'SOx_emission_million_shots_tons':,
       'Volatile_compound_million_shots_tons':})

print(r.json())