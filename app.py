from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def get_root():
    return render_template('index.html')


@app.route('/api/swagger')
def swagger():
    return render_template('swaggerui.html')


@app.route('/api')
def get_api():
    hello_dict = {'en': 'Hello',
                  'es': 'Hola',
                  'fr': 'Bonjour',
                  'ge': 'Gamarjoba'
                  }
    lang = request.args.get('lang')
    return jsonify(hello_dict[lang])


@app.route('/api/langs')
def get_available_langs():
    return jsonify(['en', 'es', 'fr', 'ge'])


if __name__ == '__main__':
    app.run(use_reloader=True, debug=False, port=8000)