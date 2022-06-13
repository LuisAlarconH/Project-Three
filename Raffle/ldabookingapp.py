from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key="d36d5433361f6337fd3d73bfeed6ec15"

DB_HOST = "localhost"
DB_NAME = "raffle"
DB_USER = "postgres"
DB_PASS = "Luisdavid171002@@"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

@app.route('/')
def Index():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM students"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('index.html', list_users = list_users)

@app.route('/add_user', methods=['POST'])
def add_user():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        cur.execute("INSERT INTO students (fname, lname, age) VALUES (%s,%s,%s)", (fname, lname, age))
        conn.commit()
        flash('User Has Been Added Successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_update(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    cur.execute('SELECT * FROM students WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit.html', username = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_username(id):
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE students
            SET fname = %s,
                lname = %s,
                age = %s
            WHERE id = %s
        """, (fname, lname, age, id))
        flash('User Has Been Successfully Been Updated')
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_username(id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute('DELETE FROM students WHERE id = {0}'.format(id))
    conn.commit()
    flash('User Has Successfully Been Removed')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
