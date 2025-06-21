from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import mysql
from datetime import datetime

main = Blueprint("main", __name__)

@main.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM buku")
    buku = cur.fetchall()
    cur.close()
    return render_template("index.html", buku=buku)

@main.route("/tambah", methods=["GET", "POST"])
def tambah():
    if request.method == "POST":
        judul = request.form["judul"]
        penulis = request.form["penulis"]
        tahun = request.form["tahun"]
        penerbit = request.form["penerbit"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO buku (judul, penulis, tahun, penerbit) "
            "VALUES (%s, %s, %s, %s)",
            (judul, penulis, tahun, penerbit)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("main.index"))

    return render_template("tambah.html")

@main.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cur = mysql.connection.cursor()

    if request.method == "POST":
        judul = request.form["judul"]
        penulis = request.form["penulis"]
        tahun = request.form["tahun"]
        penerbit = request.form["penerbit"]

        cur.execute(
            "UPDATE buku SET judul=%s, penulis=%s, tahun=%s, penerbit=%s "
            "WHERE id=%s",
            (judul, penulis, tahun, penerbit, id)
        )
        mysql.connection.commit()
        cur.close()
        return redirect(url_for("main.index"))

    cur.execute("SELECT * FROM buku WHERE id=%s", (id,))
    buku = cur.fetchone()
    cur.close()
    if not buku:
        return "Buku tidak ditemukan", 404

    return render_template("edit.html", buku=buku)

@main.route("/hapus/<int:id>")
def hapus(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM buku WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for("main.index"))

@main.route("/buku/<int:id>")
def show(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM buku WHERE id=%s", (id,))
    buku = cur.fetchone()
    cur.close()
    if not buku:
        return "Buku tidak ditemukan", 404

    return render_template("show.html", buku=buku)

@main.route("/pinjam/<int:id>", methods=["GET", "POST"])
def pinjam(id):
    if request.method == "POST":
        nama = request.form["nama"]
        tanggal_pinjam = datetime.now().date()

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO peminjaman (id_buku, nama_peminjam, tanggal_pinjam) "
            "VALUES (%s, %s, %s)",
            (id, nama, tanggal_pinjam)
        )
        mysql.connection.commit()
        cur.close()

        flash("Buku berhasil dipinjam.")
        return redirect(url_for("main.index"))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM buku WHERE id=%s", (id,))
    buku = cur.fetchone()
    cur.close()
    if not buku:
        flash("Buku tidak ditemukan.")
        return redirect(url_for("main.index"))

    return render_template("pinjam.html", buku=buku)
