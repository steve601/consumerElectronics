import sys
import pandas as pd
from source.commons import load_object
from source.exception import UserException
from source.logger import logging
from sklearn.preprocessing import LabelEncoder


class PredicPipeline:
    def __init__(self):
        pass
    
    logging.info('Preprocessing user input and making predictions')
    def predict(self,features):
        model_path = 'elements\model.pkl'
        scaler_path = 'elements\scaler.pkl'
        # loaeding objects
        model = load_object(model_path)
        scaler = load_object(scaler_path)
        data_scaled = scaler.transform(features)
        prediction = model.predict(data_scaled)
        
        return prediction
logging.info('This class is responsible for mapping all the inputs from html to flask')
class UserData:
    def __init__(self,
                productcategory,productbrand,productprice,customerage,
                customergender,purchasefrequency,customersatisfaction):
        self.cat = productcategory
        self.brand = productbrand
        self.price = productprice
        self.age = customerage
        self.gender = customergender
        self.freq = purchasefrequency
        self.rating = customersatisfaction
        
    # let's write a function that returns the user input as a numpy array
    def get_data_as_df(self):
        try:
            user_data = {
                'productcategory':[self.cat],
                "productbrand":[self.brand],
                "productprice":[self.price],
                "customerage":[self.age],
                "customergender":[self.gender],
                "purchasefrequency":[self.freq],
                "customersatisfaction":[self.rating]
            }
            return pd.DataFrame(user_data)
        except Exception as e:
            raise UserException(e,sys)
        