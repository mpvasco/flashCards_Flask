from flask import Flask, render_template, url_for ,  request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345"
app.config["MYSQL_DB"] = "example"

@app.route("/") 
def home():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM example.clientes;''')
    rv = cur.fetchall()
    return render_template('cliente.html', x=rv)


@app.route("/formAddCliente") 
def showForm():
  return render_template('addCliente.html')


@app.route("/addSql", methods=['POST'])  # ação de inserir no banco
def addCliente():
  conn = None
  cursor = None
  try:		
    _fname = request.form['fname']
    _lname = request.form['lname']
    _fav_numb = request.form['fav_numb']
    sql = "INSERT INTO clientes (fname, lname, favorite_number ) VALUE (%s, %s, %s);"
    data = (_fname, _lname, _fav_numb )
    cursor = mysql.connection.cursor()
    cursor.execute(sql, data)
    conn.commit()
    return redirect('/')
  except Exception as e:
    print(e)
  finally:
    return redirect('/')  #sempre retorna 302 no console, no mySql não adiciona nada.
    # cursor.close()      # se eu descomentar essa linha o flask nem roda.
    # conn.close()        # se eu descomentar essa linha o flask nem roda.


@app.route("/allClientes") 
def getAllClientes():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM example.clientes;''')
    rv = cur.fetchall()
    return render_template('allClientes.html', x=rv)


if __name__ == '__main__':
  app.run(debug=True)



# https://github.com/febin-george/flaskapp/blob/master/app.py