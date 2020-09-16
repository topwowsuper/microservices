import mysql.connector
from flask import Flask, render_template_string, request,Response,jsonify
import prometheus_client
from prometheus_flask_exporter import PrometheusMetrics
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'animals'
app.config['MYSQL_AUTH_PLUGIN'] = 'mysql_native_password'

metrics = PrometheusMetrics(app)
mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])

def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute('select * from animals')
        rv = cur.fetchall()
        if request.method == "POST":
            details = request.form.to_dict()
            details=str(list(details.keys())[0])
            cur = mysql.connection.cursor()
            cur.execute(f"INSERT INTO animals (id,name) VALUES(NULL,'{details}')")
            mysql.connection.commit()
            cur.close()
            return 'success'
        mysql.connection.commit()
        cur.close()
        return jsonify(rv)

    except Error as e:
        print("Error reading data from MySQL table", e)


    finally:
        mysql.connection.commit()
        cur.close()

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=5555,debug=False)
    # app.run(host='0.0.0.0', port=5555,debug=True)

