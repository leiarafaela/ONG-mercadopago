from app import app
from app.controllers import home_controller


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
