
from flask import Flask, request, jsonify

app = Flask(__name__)

# Создаем простой эндпоинт для POST запросов
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()  # Получаем данные из POST запроса

    # Здесь вы можете обработать данные или сохранить их в базу данных

    response = {'message': ['\n\nДанные успешно получены!\n\n', ''], 'data': data}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)


