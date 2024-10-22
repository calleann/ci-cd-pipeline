# elements from my dataanalysis
from dataanalysis import df, fig_hist, fig_scatter

# flask server
from flask import Flask, render_template

# Instantiate a new Flask app
app = Flask(__name__)
LAYOUT = "layout.html"


@app.route("/")
def get_df():
    return render_template(LAYOUT, title="Ma dataset", html_content=df.to_html())


@app.route("/scatter")
def get_scatter_plot():
    return render_template(LAYOUT, title="Le scatter plot", html_content=fig_scatter.to_html())


@app.route("/hist")
def get_hist_plot():
    return render_template(LAYOUT, title="Histogramme", html_content=fig_hist.to_html())


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8020)
