#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import joblib
import sys
import os

def predict_price(features):
    #establecemos la ruta del modelo en pkl
    regressor = joblib.load(os.path.dirname(__file__) + '/Autos_precio.pkl')
    print(regressor)
    #cargamos los datos para generar la estructura
    dataTraining = []
    dataTraining = pd.read_csv('https://raw.githubusercontent.com/albahnsen/MIAD_ML_and_NLP/main/datasets/dataTrain_carListings.zip')
    #generamos una copia del Df
    df_train_A =  dataTraining.copy()
    #creamos variable de inflexión de precio
    df_train_A['Inflexion'] = 0
    #creamos variable para fortalecer modelo sobre marcas
    df_train_A['4wd_awd'] = 0
    #generamos dummies
    df_train_A = pd.get_dummies(df_train_A)
    columnas = df_train_A.columns
    df1 = df_train_A.iloc[[0],:]
    df1[df1 > 0]= 0
    #variables de captura
    state = 'State_ '+features[2]
    make = 'Make_'+features[3]
    model = 'Model_'+features[4]
    df1['State_ FL'] = int(0)
    df1['Make_Jeep'] = int(0)
    df1['Model_Wrangler'] = int(0)
    df1['Year'] = int(features[0])
    df1['Mileage'] = int(features[1])
    df1[state] = int(1)
    df1[make] = int(1)
    df1[model] = int(1)
    #validamos si es 4x4
    if '4wd' in features[4].lower():
        df1['4wd_awd'] = 1
    #validamos el año para la inflexión:
    if int(features[0]) >=2010 and int(features[0]) <2014:
        df1['Inflexion'] = 0.5
    elif int(features[0]) >= 2014:
        df1['Inflexion'] = 1
    else:
        df1['Inflexion'] = 0
    df1 = df1.drop('Price', axis=1)
    my_list = list(df1)    
    # Se realiza la predicción
    predic = regressor.predict(df1)[0]
    return predic

#función inicializadora
if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Missing data, please check Year, Mileage, State and brand of car')
        
    else:
        lst = sys.argv[1]

        predic = predict_price([Year,Mileage,State,Make,Model])
        
        print([Year,Mileage,State,Make,Model])
        print('Probability of price: ', predic)

