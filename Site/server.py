from flask import Flask, request, render_template
from app import ghostWritter
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/', methods=['POST'])
def my_link():
  print ('I got clicked!')
  userPrompt = request.form['text']
  return ghostWritter(userPrompt)

if __name__ == '__main__':
  app.run(debug=True)