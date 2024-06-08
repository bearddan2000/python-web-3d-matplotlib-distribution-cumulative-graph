from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def create_graph():
    filename = 'demo'

    # random but consistant data
    lst = [2,9,4,6,4]

    title = ['mole', 'dog', 'squirel', 'bird', 'cat']
    plt.clf()
    ax = plt.figure().add_subplot(projection='3d')

    # Prepare arrays x, y, z
    _x = np.array(title)
    _y = np.array(lst)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax.bar3d(x, y, bottom, width, depth, top, shade=True)
    ax.set_title('Shaded')
    ax.legend()
    plt.savefig(f'static/img/{filename}.png')

@app.route('/', methods=['GET'])
def getIndex():
    create_graph()
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)