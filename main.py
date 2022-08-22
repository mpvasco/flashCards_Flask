from flask import Flask, render_template, url_for ,  request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345"
app.config["MYSQL_DB"] = "flashCards"

counter = -1

@app.route("/") #OK home
def home():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT front, back FROM flashcards.cards;''')
    rv = cur.fetchall()
    try:
      global counter
      counter += 1
    except:
      counter = 0
    return render_template('card.html', x=rv, counter=counter)


@app.route("/formAddCard") #mostrar formulário de add card
def showForm():
  return render_template('addCard.html')


@app.route("/addSql", methods=['GET','POST'])  # ação de inserir no banco
def addCard():
  if request.method == 'POST':
    # Fetch from data
    cardsData = request.form
    front = cardsData['front']
    back = cardsData['back']
    cur = mysql.connection.cursor()
    cur.execute ("INSERT INTO Cards (front, back, Deck_ID) VALUES (%s, %s, %s)", (front, back, 1))
    mysql.connection.commit()
    cur.close()
    return redirect('/allCards')
  return render_template('index.html')

@app.route("/allCards") #OK lista todos os itens
def getAllCards():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT front, back FROM flashcards.cards;''')
    rv = cur.fetchall()
    return render_template('allCards.html', x=rv)


if __name__ == '__main__':
  app.run(debug=True)