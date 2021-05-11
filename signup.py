@app.route('/insert', methods=['POST'])
def insert():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO Users VALUES (?,?)",
        (request.form['un'],request.form['pw']))
    con.commit()
    return request.form['un'] + ' added'
