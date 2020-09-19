from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='homepage',status='')

@app.route('/about')
def about():
    return render_template('about.html',title='about',status='')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html',title='Predictor',status='')

@app.route('/forest_fire')
def forest_fire():
    return render_template('forest_fire.html', title='homepage', status='')

@app.route('/services')
def services():
    return render_template('services.html',title='services',status='')

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    else:
        return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True)
