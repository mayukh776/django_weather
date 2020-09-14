from django.shortcuts import render

# Create your views here.
# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=74AD2A22-A089-4156-B66B-428BF9203477
def home(request):
    import json
    import requests
    if request.method == "POST":
        zipcode = request.POST['ZipCode']
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=74AD2A22-A089-4156-B66B-428BF9203477")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ...."
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is considered satisfactory and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) Air quality is acceptable; however,for some pollutanats there may be a moderate concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general public is not likely to be affected at this AQI range,people with lung disease,senior citizens and children are at a greater risk of exposure to ozone whereas people with heart and lung diseases are at a greater risk of exposure to air particles."
            category_color = "USG"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Health alert: Everyone may experience more serious health issues."
            category_color = "VeryUnhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500) Health warnings of emergency conditions. The entire population is likely to be affected."
            category_color = "Hazardous"
        return render(request,'home.html',{'api':api,'category_description':category_description,'category_color':category_color})
    else:
        api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=74AD2A22-A089-4156-B66B-428BF9203477")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error ...."
        if api[0]['Category']['Name'] == "Good":
            category_description = "(0-50) Air quality is considered satisfactory and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51-100) Air quality is acceptable; however,for some pollutanats there may be a moderate concern for a very small number of people who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101-150) Although general public is not likely to be affected at this AQI range,people with lung disease,senior citizens and children are at a greater risk of exposure to ozone whereas people with heart and lung diseases are at a greater risk of exposure to air particles."
            category_color = "USG"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151-200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "Unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201-300) Health alert: Everyone may experience more serious health issues."
            category_color = "VeryUnhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "(301-500) Health warnings of emergency conditions. The entire population is likely to be affected."
            category_color = "Hazardous"
        return render(request,'home.html',{'api':api,'category_description':category_description,'category_color':category_color})
def about(request):
    return render(request,'about.html')