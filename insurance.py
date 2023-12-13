from flask import Flask,render_template,request
import pandas as pd
import pickle

app=Flask(__name__)
data=pd.read_csv(r'C:\Users\ATHUL AKSHAY\Desktop\Insurance\insurance.csv')
model=pickle.load(open('insurance.pkl','rb'))

@app.route('/')
def home():
    return render_template('frontpage.html')
@app.route('/data')
def data():
    return render_template('insurance.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method =='POST':
        age=int(request.form['age'])
        sex=request.form['sex']
        smoker=request.form['smoker']
        bmi=request.form['bmi']
        children=int(request.form['children'])
        # input_data=pd.DataFrame([[age,sex,smoker,bmi,children]],columns=['age','sex','smoker','bmi','children'])

        prediction=model.predict([[age,sex,smoker,bmi,children]])
        prediction=(round(prediction[0],4))
        return render_template('insurance.html',predict=prediction)
    

if __name__=='__main__':
    app.run(debug=True)