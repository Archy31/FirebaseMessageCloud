
from app import app
import gunicorn


if __name__ == '__main__':
    from gunicorn.app.wsgiapp import run
    run()
