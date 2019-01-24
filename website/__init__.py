from flask import (
  Flask, render_template
)


app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/news')
def news():
  return render_template('news.html')

@app.route('/products')
def products():
  return render_template('products.html')

@app.route('/productcase')
def productcase():
  return render_template('productcase.html')

@app.route('/careers')
def careers():
  return render_template('careers.html')

@app.route('/support')
def support():
  return render_template('support.html')

@app.route('/videos')
def videos():
  return render_template('videos.html')

@app.route('/contactus')
def contactus():
  return render_template('contactus.html')

@app.route('/p1')
def p1():
  return render_template('p1.html')

@app.route('/p2')
def p2():
  return render_template('p2.html')

@app.route('/p3')
def p3():
  return render_template('p3.html')

@app.route('/p4')
def p4():
  return render_template('p4.html')

@app.route('/p5')
def p5():
  return render_template('p5.html')

@app.route('/p6')
def p6():
  return render_template('p6.html')

@app.route('/p7')
def p7():
  return render_template('p7.html')

@app.route('/p8')
def p8():
  return render_template('p8.html')

@app.route('/p9')
def p9():
  return render_template('p9.html')

@app.route('/p10')
def p10():
  return render_template('p10.html')

@app.route('/p11')
def p11():
  return render_template('p11.html')

@app.route('/p12')
def p12():
  return render_template('p12.html')

@app.route('/p13')
def p13():
  return render_template('p13.html')

@app.route('/p14')
def p14():
  return render_template('p14.html')

