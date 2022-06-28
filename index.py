#importamos la libreria Flask
from flask import Flask, render_template

app = Flask(__name__) 

#---------------------------------------
#Ruta de pagina principal
#---------------------------------------

@app.route('/')
def index():
    return render_template('game.html')

#---------------------------------------
#iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)