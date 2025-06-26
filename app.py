from flask import Flask, render_template, request
import pickle
import numpy as np

app= Flask(__name__)
model=pickle.load(open('health_insurance_price.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Predict', methods=['POST'])
def predict_price():
    Age=int(request.form.get('Age'))
    BMI =float(request.form.get('BMI'))
    Children = request.form.get('Children')
    Smoker = request.form.get('Smoker')



    # Convert categorical to numeric (you must match how model was trained!)
    Smoker = 1 if Smoker.lower() == 'yes' else 0



    input_features = np.array([[Age, BMI, Children, Smoker]], dtype=np.float32)

    result = model.predict(input_features)[0]  # Take the first result


    return render_template('index.html', result=result)

if __name__=='__main__':
    app.run(debug=True)