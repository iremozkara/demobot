import requests



def Weather(city): 
    api_address="http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=a450b2a6adc5683224c14f5a73a2e485"
    #city = input("City Name :")
    url = api_address  
    json_data = requests.get(url).json() 
    format_add = json_data['main'] 
    print(format_add) 
    return format_add