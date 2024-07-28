import pickle
from flask import Flask, render_template, request , jsonify

app = Flask(__name__)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
    
@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    features = ['DewPointHighF', 'DewPointAvgF', 'DewPointLowF', 'HumidityHighPercent', 'HumidityAvgPercent', 'HumidityLowPercent', 'WindHighMPH', 'WindGustMPH']
    values = [request.form.get(feature) for feature in features]
    prediction = model.predict([values])
    output = round(prediction[0],2)
    print(output)
    return jsonify({'prediction' : output})

if __name__ == '__main__':
    app.run(debug=True)