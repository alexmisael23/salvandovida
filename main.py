import email

import lista as lista
from flask import Flask, render_template, request, url_for,redirect
import pyrebase

import json
from Modelo.usuario import usuario

#Variable de configuración
config={
    "apiKey": "AIzaSyBXPZq0iXyIcrb18x5WjVE2r7XA9fgpP18",
    "authDomain": "salvandovida-10b02.firebaseapp.com",
    "databaseURL": "https://salvandovida-10b02-default-rtdb.firebaseio.com",
    "projectId": "salvandovida-10b02",
    "storageBucket": "salvandovida-10b02.appspot.com",
    "messagingSenderId": "935386215564",
    "appId": "1:935386215564:web:f92e396909ea2df84877a9"
}

firebase=pyrebase.initialize_app(config)
db=firebase.database()

app = Flask(__name__)

@app.route('/prueba')
def prueba():
    lista_Comida=db.child("Comida").get().val()

    return render_template("inicio.html", elementos_Comida=lista_Comida.values())

@app.route('/')
def hello_word():
    lista=db.child("Registro").get()
    try:
        lista_Registro=lista.val()
        lista_indices=lista_Registro.keys()
        lista_indice_final=list(lista_indices)
        return render_template("inicio.html", elementos_Registro=lista_Registro.values(),lista_indice_final=lista_indice_final)
    except:
         return render_template("inicio.html")


#ruta para mostrar formulario de registro
@app.route('/add')
def add():
    return render_template('alta_personas.html')

#---------------------------------------------------------------------------------------------
#Capturar los datos del formulario y guardarlos en FB
@app.route('/save_data', methods=['POST'])
def save_data():
    email=request.form.get('email')
    contraseña=request.form.get('contraseña')
    nueva_persona=usuario(email, contraseña)
    objeto_enviar = json.dumps(nueva_persona.__dict__)

    formato = json.loads(objeto_enviar)
    db.child("Registro").push(formato)

    #db.child("Registro").push({"email":email, "contraseña":contraseña})

    #return render_template("inicio.html")
    return redirect(url_for('hello_word'))

    #eliminar un registro de la tabla
@app.route('/eliminar_persona', methods=["GET"])
def eliminar_persona():
    id=request.args.get("id")
    db.child("Registro").child(str(id)).remove()
    return redirect(url_for('hello_word'))
    #return "usuario eliminado correctamente"



@app.route('/alta/<nombre>')
def registrar(nombre):
    db.child("personas").push({"nombre":nombre})
    return "dato guardado exitosamente"

@app.route('/eliminar')
def eliminar():
    db.child("personas").child("-MxCQaEgMBu5xDfAzOWP").remove()
    return "usuario eliminado correctamente"

@app.route('/modificar')
def modificar():
    db.child("personas").child("-MxCRMB6ex31I-Qsnbjy").update({"nombre": "Maria Dosantos Aveiro"})
    return "Datos modificados correctamente"

if __name__ == '__main__':
    app.run(debug=True)
