from flask import Flask, render_template, url_for ,  request, redirect
from flask_mysqldb import MySQL
app = Flask(__name__)
mysql = MySQL(app)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "12345"
app.config["MYSQL_DB"] = "flashCards"

counter = 0

@app.route("/") #OK home
def home():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT front, back FROM flashcards.cards;''')
    rv = cur.fetchall()
    print(rv)
    cur.execute('''SELECT * FROM flashcards.decks;''')
    rv2 = cur.fetchall()
    print(rv2)
    return render_template('card.html', x=rv, y=rv2, counter=0)
# def home():
#     cur = mysql.connection.cursor()
#     cur.execute('''SELECT front, back FROM flashcards.cards;''')
#     rv = cur.fetchall()
#     global counter
#     if len(rv) >= counter:
#       counter += 1
#     else:
#       counter = 0
#     return render_template('card.html', x=rv, counter=counter)


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
    # return redirect('/allCards')
    return render_template('addCard.html')  
  return render_template('index.html')

@app.route("/allCards") #OK lista todos os itens
def getAllCards():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT Cards.Card_ID as 'cardID', front, back,  Decks.name as 'deckName', Cards.Deck_ID as 'deckID'
    FROM Cards
    INNER JOIN Decks
    ON Cards.Deck_ID = Decks.Deck_ID;''')
    rv = cur.fetchall()
    return render_template('allCards.html', x=rv)


@app.route('/allCards/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cards where Card_ID = "+ str(id) +";")
    resultValue= cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if request.method=='GET':
      return render_template('editCard.html', x=resultValue )
    if request.method=='POST':
      front = request.form['front']
      back = request.form['back']
      cur = mysql.connection.cursor()
      query = "UPDATE cards SET front = %s, back = %s  WHERE Card_ID = %s;"
      cur.execute(query, (front, back, id))
      resultValue= cur.fetchall()
      mysql.connection.commit()
      cur.close()
    return redirect('/allCards')


@app.route('/allCards/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cards where Card_ID = "+ str(id) +";")
    resultValue= cur.fetchall()
    mysql.connection.commit()
    cur.close()
    if request.method=='GET':
      return render_template('deleteCard.html', x=resultValue )

    if request.method=='POST':
      cur = mysql.connection.cursor()
      query = "DELETE FROM cards WHERE Card_ID = %s;"
      # cur.execute(query, str(id))
      cur.execute(query, (id,))
      resultValue= cur.fetchall()
      mysql.connection.commit()
      cur.close()
    return redirect('/allCards')
if __name__ == '__main__':
  app.run(debug=True)