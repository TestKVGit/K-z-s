from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            id = request.form["id"]
            nev = request.form["nev"]
            brutto = request.form["brutto"]
            with sqlite3.connect("ber.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into Ber (id, nev, brutto) values (?,?,?)", (id, nev, brutto))
                con.commit()
                msg = "Sikeresen feltöltődött az adat"
        except:
            con.rollback()
            msg = "Nem lehet hozzáadni a listához"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect("ber.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Ber")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("ber.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Ber where id = ?", id)
            msg = "Törlés megtörtént"
        except:
            msg = "Nem lehet törölni"
        finally:
            return render_template("delete_record.html", msg=msg)

@app.route("/update")
def update():
    return render_template("update.html")

@app.route("/updatedetails", methods=["POST"])
def updaterecord():
    msg = "msg"
    if request.method == "POST":
        try:
            id = request.form["id"]
            nev = request.form["nev"]
            brutto = request.form["brutto"]
            with sqlite3.connect("ber.db") as con:
                cur = con.cursor()
                cur.execute("UPDATE Ber SET nev=?, brutto=? WHERE id=?", (nev, brutto, id))
                con.commit()
                msg = "Sikeresen frissültek az adatok"
        except:
            con.rollback()
            msg = "Nemlehet új adatot csinálni"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

if __name__ == "__main__":
    app.run(debug=True)