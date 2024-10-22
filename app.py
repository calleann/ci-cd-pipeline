# elements from my dataanalysis
from dataanalysis import df, fig_hist, fig_scatter

# flask server
from flask import Flask, render_template

# Instantiate a new Flask app
app = Flask(__name__)


@app.route("/")
def get_df():
    return render_template("index.html",df_html = df.to_html())


@app.route("/scatter")
def get_scatter_plot():
    return fig_scatter.to_html()


@app.route("/hist")
def get_hist_plot():
    return fig_hist.to_html()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8020)
