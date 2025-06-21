from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_app():
    app = Flask(__name__)

    # ✅ Tambahkan ini untuk mengaktifkan session dan flash
    app.secret_key = 'rul123'  # Ganti dengan string acak yang aman

    # Konfigurasi database
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'perpustakaan'

    mysql.init_app(app)

    # Import blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
