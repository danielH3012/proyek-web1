import datetime
import os
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/categories')
def categories():
    return render_template("categories.html")

@app.route('/news')
def news():
    return render_template("news.html")

@app.route('/news12')
def news12():
    try:
        with open("nama.txt","r") as file:
           datafile1 = file.read()
           pesan2 = datafile1.split('\n')
    except:
        return 'error'
    #file reader komen user
    try:
        with open("komen.txt","r") as file:
           datafile = file.read()
           pesan = datafile.split('\n')
    except:
        return 'error'
    return render_template("news1.html",data = pesan,panjang = len(pesan)-1,nama = pesan2)

@app.route('/news1', methods=["POST"])
def news1():
    print(request.form)
    #filereader nama user
    nama = request.form['nama'] +"\n"
    komen = request.form['komen'] + "\n"
    with open("nama.txt","a") as file:
        file.write(nama)
    with open("komen.txt","a") as file:
        file.write(komen)
    #passing ke html
    return redirect('/news12')
    #return render_template("index.html",data = pesan,panjang = len(pesan)-1,nama = pesan2)

@app.route('/news22')
def news22():
    try:
        with open("nama2.txt","r") as file:
           datafile1 = file.read()
           pesan2 = datafile1.split('\n')
    except:
        return 'error'
    #file reader komen user
    try:
        with open("komen2.txt","r") as file:
           datafile = file.read()
           pesan = datafile.split('\n')
    except:
        return 'error'
    return render_template("news2.html",data = pesan,panjang = len(pesan)-1,nama = pesan2)

@app.route('/news2', methods=["POST"])
def news2():
    print(request.form)
    #filereader nama user
    nama = request.form['nama'] +"\n"
    komen = request.form['komen'] + "\n"
    with open("nama2.txt","a") as file:
        file.write(nama)
    with open("komen2.txt","a") as file:
        file.write(komen)
    #passing ke html
    return redirect('/news22')

@app.route('/news32')
def news32():
    try:
        with open("nama3.txt","r") as file:
           datafile1 = file.read()
           pesan2 = datafile1.split('\n')
    except:
        return 'error'
    #file reader komen user
    try:
        with open("komen3.txt","r") as file:
           datafile = file.read()
           pesan = datafile.split('\n')
    except:
        return 'error'
    return render_template("news3.html",data = pesan,panjang = len(pesan)-1,nama = pesan2)

@app.route('/news3', methods=["POST"])
def news3():
    print(request.form)
    #filereader nama user
    nama = request.form['nama'] +"\n"
    komen = request.form['komen'] + "\n"
    with open("nama3.txt","a") as file:
        file.write(nama)
    with open("komen3.txt","a") as file:
        file.write(komen)
    #passing ke html
    return redirect('/news32')

@app.route('/news42')
def news42():
    try:
        with open("nama4.txt","r") as file:
           datafile1 = file.read()
           pesan2 = datafile1.split('\n')
    except:
        return 'error'
    #file reader komen user
    try:
        with open("komen4.txt","r") as file:
           datafile = file.read()
           pesan = datafile.split('\n')
    except:
        return 'error'
    return render_template("news4.html",data = pesan,panjang = len(pesan)-1,nama = pesan2)

@app.route('/news4', methods=["POST"])
def news4():
    print(request.form)
    #filereader nama user
    nama = request.form['nama'] +"\n"
    komen = request.form['komen'] + "\n"
    with open("nama4.txt","a") as file:
        file.write(nama)
    with open("komen4.txt","a") as file:
        file.write(komen)
    #passing ke html
    return redirect('/news42')

@app.route('/news52')
def news52():
    try:
        with open("nama5.txt","r") as file:
           datafile1 = file.read()
           pesan2 = datafile1.split('\n')
    except:
        return 'error'
    #file reader komen user
    try:
        with open("komen5.txt","r") as file:
           datafile = file.read()
           pesan = datafile.split('\n')
    except:
        return 'error'
    return render_template("news5.html",data = pesan,panjang = len(pesan)-1,nama = pesan2)

@app.route('/news5', methods=["POST"])
def news5():
    print(request.form)
    #filereader nama user
    nama = request.form['nama'] +"\n"
    komen = request.form['komen'] + "\n"
    with open("nama5.txt","a") as file:
        file.write(nama)
    with open("komen5.txt","a") as file:
        file.write(komen)
    #passing ke html
    return redirect('/news52')

@app.route('/produk1')
def produk1():
    return render_template("produk1.html")

@app.route('/produk2')
def produk2():
    return render_template("produk2.html")

@app.route('/produk3')
def produk3():
    return render_template("produk3.html")

@app.route('/produk4')
def produk4():
    return render_template("produk4.html")

@app.route('/produk5')
def produk5():
    return render_template("produk5.html")

@app.route('/produk6')
def produk6():
    return render_template("produk6.html")

@app.route('/produk7')
def produk7():
    return render_template("produk7.html")

@app.route('/produk8')
def produk8():
    return render_template("produk8.html")

@app.route('/produk9')
def produk9():
    return render_template("produk9.html")

@app.route('/produk10')
def produk10():
    return render_template("produk10.html")

@app.route('/produk11')
def produk11():
    return render_template("produk11.html")

@app.route('/produk12')
def produk12():
    return render_template("produk12.html")

@app.route('/produk13')
def produk13():
    return render_template("produk13.html")

@app.route('/produk14')
def produk14():
    return render_template("produk14.html")

@app.route('/produk15')
def produk15():
    return render_template("produk15.html")

@app.route('/produk16')
def produk16():
    return render_template("produk16.html")

@app.route('/produk17')
def produk17():
    return render_template("produk17.html")

@app.route('/produk18')
def produk18():
    return render_template("produk18.html")

@app.route('/fisik')
def fisik():
    return render_template("produk_fisik.html")

@app.route('/hewan')
def hewan():
    return render_template("produk_hewan.html")

@app.route('/lingkungan')
def lingkungan():
    return render_template("produk_lingkungan.html")

@app.route('/makanan')
def makanan():
    return render_template("produk_makanan.html")

@app.route('/mental')
def mental():
    return render_template("produk_mental.html")

@app.route('/tumbuhan')
def tumbuhan():
    return render_template("produk_tumbuhan.html")

if __name__ == '_main_':
    app.run(debug=True)