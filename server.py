import pandas as pd
from flask import Flask, request, jsonify
from waitress import serve
import pickle
# install flask, waitress, pickle into your ananconda environment

app = Flask(__name__)
modelOne = pickle.load(open('model1.pkl', 'rb')) # load model1 to the server, 'rb' - read binary
moving_avg_50 = pd.read_pickle('50_MA.pkl') 
moving_avg_200 = pd.read_pickle('200_MA.pkl') 


@app.route('/model1', methods=['GET'])
def callModelOne():
    a = request.args.get('a', type= float)
    b = request.args.get('b', type= float)
    c = request.args.get('c', type= float)
    d = request.args.get('d', type= float)
    arr = pd.DataFrame({'sepal_length_cm': [a], 'sepal_width_cm': [b], 'petal_length_cm': [c], 'petal_width_cm':[d]})

    return str(modelOne.predict(arr)[0])

 
@app.route('/model2', methods=['GET'])
def callModelTwo():
   ma_50 = request.args.get('x', type= float)
   ma_200 = request.args.get('y', type= float)
   print(moving_avg_50(ma_50))
   
   result = str(moving_avg_50[ma_50]) + ", " + str(moving_avg_200[ma_200])
   return result

# run the server
if __name__ == '__main__':
    print("Starting the server.....")
    serve(app, host="0.0.0.0", port=8070)
