from flask import Flask,render_template,request
import numpy as np
from source.main_project.pipeline.predict_pipeline import UserData,PredicPipeline

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('consumer.html')

@app.route('/predict',methods=['POST'])
def do_prediction():
    # instantiating the UseData column
    data = UserData(
        productcategory=request.form.get('cat'),
        productbrand=request.form.get('brand'),
        productprice=request.form.get('price'),
        customerage=request.form.get('age'),
        customergender=request.form.get('gender'),
        purchasefrequency=request.form.get('frequency'),
        customersatisfaction=request.form.get('rating')
    )
    # accessing its method
    user_df = data.get_data_as_df()
    #instantiating predictpipeline class
    predict_pipe = PredicPipeline()
    #accessing its method
    result = predict_pipe.predict(user_df)
    
    msg = 'Customer has an intention of purchasing the product' if result == 1 else 'Customer has no intention of purchasing the product'
    
    return render_template('consumer.html',text=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0")