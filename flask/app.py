from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# MariaDB 연결 설정
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='sesac',
            user='root',
            password='your_password'  # 실제 패스워드로 변경하세요
        )
        return connection
    except Error as e:
        print(f"데이터베이스 연결 오류: {e}")
        return None

visitCount = 0


@app.route("/")
def home():
    global visitCount
    visitCount += 1
    return render_template("index.html", count=visitCount)

@app.route("/user", methods=["GET", "POST"])
def user():
    username = request.form.get('id')
    pw = request.form.get('pw')

    conn = get_db_connection()
    if conn is None:
        return "<h1>데이터베이스 연결 실패 ❌</h1>"

    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT id, user_id, username FROM users_info WHERE user_id=%s AND password=%s",
            (username, pw)
        )
        row = cur.fetchone()

        if row:
            _id, user_id, name = row
            return f"<h1>로그인 성공! {name}님 환영합니다 🎉</h1>"
        else:
            return "<h1>로그인 실패 ❌</h1>"

    except Error as e:
        return f"<h1>데이터베이스 오류: {e} ❌</h1>"
    finally:
        cur.close()
        conn.close()


@app.route('/admin')
def admin():
    return "<h1> Welcome to Admin </h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
