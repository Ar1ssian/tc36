from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('technoservice.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    r1 = (request.args.get("r1"))
    if r1 is not None:
        print('Данные введены')
        r1 = (request.args.get("r1"))
        r2 = (request.args.get("r2"))
        r3 = (request.args.get("r3"))
        r4 = (request.args.get("r4"))
        r5 = (request.args.get("phone"))
        r6 = (request.args.get("nameuser"))
        price = int(r1)*1500 + int(r2)*2000 + int(r3)*800 + int(r4)*3000     
        # Подключение к базе данных SQLite и Создание объекта курсора
        conn = sqlite3.connect('TechnoService.db')
        cursor = conn.cursor()
        # SQL-запрос INSERT для добавления записи в таблицу
        sql = """INSERT INTO Orders (idorder,nameuser,nout,plan,pc,tv,price,number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        # Данные для добавления
        r0 = random.randint(1000, 9999)
        data = (r0, r6, r1, r2, r3, r4,  price, r5)
        print(data)
        cursor.execute(sql, data)
        conn.commit()
        conn.close()
        return render_template('succes.html')
    else:
        print('Нет данных')
        return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)

