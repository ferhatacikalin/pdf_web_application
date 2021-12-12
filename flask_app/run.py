from project import app, db

if __name__ == '__main__':
    app.app_context().push()
    app.run(host='0.0.0.0', port=8080)
