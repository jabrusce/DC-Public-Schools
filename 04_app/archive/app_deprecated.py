from flask import Flask, Response, request, jsonify, render_template
import numpy as np
import pickle
#MPLD3 lets us make an html of a matplotlib plot:
import matplotlib.pyplot as plt, mpld3
import seaborn as sns
import pandas as pd
#Mapping Specific imports:
import json 
import requests
from shapely.geometry import shape, Point
import folium


#This is supposed to help with crashing
import matplotlib
matplotlib.use('Agg')

#initialize the flask app

app = Flask('myApp')

#Read in our Dataframe:
df = pd.read_csv('./data/cluster_student_counts.csv')
df['Count of English Learner Students'] = pd.to_numeric(df['Count of English Learner Students'], errors = 'coerce').fillna(value = 0)
school_df = pd.read_csv('./data/school_df_v1.csv')

#### MAPPING ####

#URL for neighborhood boundaries:
neighbs_url = 'https://opendata.arcgis.com/datasets/f6c703ebe2534fc3800609a07bad8f5b_17.geojson'

#URL for the DC area boundary:
dc_area_url = 'https://opendata.arcgis.com/datasets/7241f6d500b44288ad983f0942b39663_10.geojson'

#URL for Wards:
ward_url = 'https://opendata.arcgis.com/datasets/0ef47379cbae44e88267c01eaec2ff6e_31.geojson'

#Reading in the neighborhood data
resp = requests.get(neighbs_url)
neighbs_data = resp.json()

#Reading in the ward data
resp2 = requests.get(ward_url)
ward_data = resp2.json()

#Loop through all of the neighborhoods and check if the school is inside that neighborhood.
#If it is, assign the neighborhood number to it.
school_df['neighborhood'] = np.nan

for neb in range(len(neighbs_data['features'])): #len(neighbs_data['features'])
  
  outline = shape(neighbs_data['features'][neb]['geometry'])
  #print(neb)
  #neighbs_data['features'][neb]['geometry'] should give us the geometry of the neighborhood. Next we need to check
  #if the school is inside that geometry:
  for school in range(len(school_df)):

    location = Point(school_df['school_longitude'].iloc[school], school_df['school_latitude'].iloc[school])
    name = school_df.iloc[school]['school_name']
    if outline.contains(location):
      #Uncomment below if you want a full printout of the loop finding the neighborhood:
      #print(f'School #{name} is in neighborhood {neb} ')
      #print('----')
      #print(school_data.iloc[school])
      school_df.iloc[school, school_df.columns.get_loc('neighborhood')] = neb
      pass
    else:
      
      pass
  


#### END MAPPING SETUP ####



### ROUTES / WEBPAGES ###

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

    f = plt.figure()
    sns.scatterplot(df[x].values, df[y].values) #hue=plot_hue
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(x + ' vs '+ y)
    #plt.show()

    return render_template('results.html', graph=(mpld3.fig_to_html(f)))

@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/graph")
def graph():
    #https://stackoverflow.com/questions/25728442/how-to-place-a-matplotlib-plot-into-an-html-container-using-mpld3-and-flask
    #load in form data from incoming request
    user_input = request.args

    x = user_input['x_var']
    y = user_input['y_var']
    plot_hue = user_input['hue']
    plot_yr =user_input['year']

    x2 = user_input['x_var2']
    y2 = user_input['y_var2']
    plot_hue2 = user_input['hue2']
    plot_yr2 =user_input['year2']

    choro_n = user_input['chorop_n']
    choro_w = user_input['chorop_w']

    #First Graph:
    f2 = plt.figure()
    sns.scatterplot(df[x].values, df[y].values) #hue=plot_hue
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(x + ' vs '+ y)
    
    #Second Graph:
    f3 = plt.figure()
    sns.scatterplot(df[x2].values, df[y2].values) #hue=plot_hue
    plt.xlabel(x2)
    plt.ylabel(y2)
    plt.title(x2 + ' vs '+ y2)

    #Choropleth:
    m = folium.Map(width = 600, height=600, location = [38.9, -77], zoom_start=10.5)
    #Adding a neighborhood layer:
    neighborhood_layer = folium.FeatureGroup(name='Neighborhoods', show=False, )
    folium.GeoJson(neighbs_data).add_to(neighborhood_layer)
    neighborhood_layer.add_to(m)
    #Adding a ward layer:
    ward_layer = folium.FeatureGroup(name='Wards', show=False)
    folium.GeoJson(ward_data).add_to(ward_layer)
    ward_layer.add_to(m)
    school_layer = folium.FeatureGroup(name='Schools', show=False)
    #Iterate through the schoo
    for row in range(len(school_df)):
        lat = school_df.iloc[row]['school_latitude']
        long = school_df.iloc[row]['school_longitude']
        label = school_df.iloc[row]['school_name']
        folium.Marker(location = [lat, long], popup = label, tooltip=f'''
        School Name: {label}  \n  
        Neighborhood: {school_df.iloc[row]['neighborhood']} 
        ''').add_to(school_layer)
    school_layer.add_to(m)
    folium.LayerControl().add_to(m)
    #Display the map:
    m.save('templates/map.html') 


    return render_template('test.html', graph=(mpld3.fig_to_html(f2)), graph2=(mpld3.fig_to_html(f3)))


if __name__=="__main__":
    app.run(debug=True)
