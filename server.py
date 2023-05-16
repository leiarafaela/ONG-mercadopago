from app import app

@app.route('/')
def home():
    return '<h1> Olá!!</h1>'

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)