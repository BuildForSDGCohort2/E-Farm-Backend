from efarm import create_app

app = create_app('development.py')

if __name__ == '__main__':
    app.run()