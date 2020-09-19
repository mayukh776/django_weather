from django.shortcuts import render
import json
import requests
# Create your views here.

def about(request):
    return render(request,"about.html",{})
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 

        source = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=8ca31c14830b39c8e8a78b41c454d200")
  
        # converting JSON data to a dictionary 
        try:
            list_of_data = json.loads(source.content) 
        except:
            list_of_data = "Error...."
        # data for variable list_of_data 
        data = { 
            "icon" : list_of_data['weather'][0]['icon'],
            "description" : str(list_of_data['weather'][0]['description']),
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp" : str(list_of_data['main']['temp']),
            "temp_min" : str(list_of_data['main']['temp_min']) + ' ' + 'K',
            "temp_max" : str(list_of_data['main']['temp_max']) + ' ' + 'K', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
            "visibility": str(list_of_data['visibility']) + ' ' + 'm', 
            } 
        print(data) 
    else: 
        data ={} 
    return render(request, "index.html", data)