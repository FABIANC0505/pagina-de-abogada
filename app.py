from flask import Flask, render_template
 
app = Flask(__name__)

@app.route('/') # Página de inicio
def home():
    return render_template('index.html')

@app.route('/articulos')  # Página para artículos y pasatiempos
def articulos():
    return ('articulos.html')

if __name__ == '__main__':
    app.run(debug=True)