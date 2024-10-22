# elements from my dataanalysis
from dataanalysis import df, fig_hist, fig_scatter

# flask server
from flask import Flask

# Instantiate a new Flask app
app = Flask(__name__)


@app.route("/")
def get_df():
    return f"<h1> Ma dataset </h1><div>{df.to_html(border=1)}</div>"


@app.route("/scatter")
def get_scatter_plot():
    return fig_scatter.to_html()


@app.route("/hist")
def get_hist_plot():
    return fig_hist.to_html()


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8020)
