from flask import Flask,render_template,request
from process import predict_model

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About')

@app.route('/',methods=['POST'])
def predict():

    img = request.files['imagefile']
    img_path = './static/images/' + img.filename
    img.save(img_path)

    classification=predict_model(img_path)

    return render_template('result.html',result=classification[0],percentage=classification[1],img_path=img_path)




if __name__=='__main__':
    app.run(debug=True)