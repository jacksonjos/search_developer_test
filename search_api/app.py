from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    # count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
