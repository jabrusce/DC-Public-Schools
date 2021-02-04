from flask import Flask, Response, request, jsonify, render_template
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt, mpld3
import seaborn as sns
import pandas as pd

#This is supposed to help with crashing
import matplotlib
matplotlib.use('Agg')

#initialize the flask app

app = Flask('myApp')

#Read in our Dataframe:
df = pd.read_csv('./data/cluster_student_counts.csv')
df['Count of English Learner Students'] = pd.to_numeric(df['Count of English Learner Students'], errors = 'coerce').fillna(value = 0)
#print(df.info())
#print(df['Count of English Learner Students'].describe())
#print(df['Count of At Risk Students'].describe())

#First route: Hello world
#Returns a simple string
@app.route("/")
def home():
    return "Project 5: Washington DC School Districts Analysis"


#Route #2
#Return a webpage
#return hard-coded html
name='Keith'

@app.route("/hc_page")
def hc_page():
    return f"""
        <html>
            <body>
                <h1>This is a hard coded page</h1>
                <p>Here's the text! {name}, isn't this cool?</p>
            </body>
        </html>
    """

#3rd Route: Return some data in json format
#using jsonify function
@app.route("/hc_page.json")
def json_data():
    favs = {
        'movie': 'Inception',
        'band': 'Glass Animals',
        'song': 'Tokyo Drifting'
    }
    return jsonify(favs), 200

#Route 4: show user a form
@app.route("/form")
def form():
    return render_template("form.html")

#route 5: accept form submission and handle it
@app.route("/submit")
def make_graph():
    #load in form data from incoming request
    user_input = request.args

    x = user_input['x_var']
    y = user_input['y_var']
    plot_hue = user_input['hue']
    plot_yr =user_input['year']

    #print(x)
    #print(y)
    #print(df['Count of At Risk Students'].values)

    f = plt.figure()
    sns.scatterplot(df[x].values, df[y].values) #hue=plot_hue
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(x + ' vs '+ y)
    #plt.show()

    return render_template('results.html', graph=(mpld3.fig_to_html(f)))

if __name__=="__main__":
    app.run(debug=True)
