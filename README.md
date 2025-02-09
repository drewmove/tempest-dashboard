Python/Django app to display weather statistics from multiple Tempest weather stations.

Why does this project exist?

I bought a weather station for my home and share the station with my sailing club.    After that, several other sailing club members got Tempest weather stations and share their station info on to the public as well.    Unfortunately, the Tempest App and Web Site 
doesn't let you display a curated list of reporting stations in one place.  This web application attempts to solve the deficiency of the Tempest web site and mobile app with a simple Weather Dashboard application.

The app is implemented in Django, and currently uses a local embedded sqlite datastore for station locations, credentials, and the last set of weather statistics.

To install this, you would need to clone the repo to your system running Python3.9 or higher ( the code uses several datetime functions only available after 3.8).  You'll need to create your virtual environment, etc and use the command line python3 manage.py to 
run your server

python3 manage.py runserver

to configure the stations, visit the "admin" url - localhost:8000/admin and set up each individual station you want displayed

Note, in your tempest account, you will need to set up a Personal Access Token for your data, and enter that plus your stationID into the configuration.   

For any additional stations, have the owner provide you with a personal access token and their station id.


Current State

The app is pretty basic right now - gets the named statistics and displays them in text form on a web page.

ToDo:

- Implement units of measure logic to display the dashboard with the preferred units.  Right now, it's hardcoded to F/Knots/Millibars.  Tempest data does return the configured units of measurement for the display, the code just isn't handling it today.
- Implement a scheduled retrieval of station data separately from the page render.  Right now, when the view is rendered, the code retrieves the data from the station via the API.  For small groups, this won't matter but for larger ones this may create an API rate limit.
- Improve the display with some basic graphics - overlaying temp/wind chill/feels like on a thermometer, wind as a compass rose, and some thresholds to color code things
- Improve the display with a re-arrangable order of display (perhaps in admin mode for all users) or per-user.
- Implement data storage in an external database, most likely postgres
- Package the app in a docker container for more straghtforward deployments in various environments cloud/raspberry pi, whatever.
- implement some historical data capabilities/display - or not.  I'd like to see where people want to go with this.

  
