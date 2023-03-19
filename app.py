import requests
from tkinter import *
from PIL import ImageTk,Image

apiKey = 'YOURAPIKEY'
urlRequest = 'https://api.openweathermap.org/data/2.5/weather'
iconUrl = 'https://openweathermap.org/img/wn/{}@2x.png'
#-273.15


def getWeather(city):
    param = {'q': city, 'appid': apiKey, 'lang':'tr'}
    
    data = requests.get(urlRequest, params = param).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int((data['main']['temp']) - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description'].capitalize()
        return(city,country,temp,icon,condition)

    
def getMain():
    city = searchEntry.get()
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
        tempLabel['text'] = '{} °C'.format(weather[2])
        conditionLabel['text'] = weather[4]
        icon = ImageTk.PhotoImage(Image.open(requests.get(iconUrl.format(weather[3]), stream = True).raw))
        iconLabel.configure(image=icon)
        iconLabel.image = icon



mainApp = Tk()
mainApp.geometry('450x600')
mainApp.title('Weather App')
mainApp['background'] = '#e9eaf2'

searchEntry = Entry(mainApp, justify='center')
searchEntry.pack(fill = BOTH, ipady = 10, padx = 18, pady = 5)
searchEntry.focus()

searchButton = Button(mainApp, text="Arama", font=('Arial', 15), command = getMain)
searchButton.pack(fill = BOTH, ipady = 10, padx = 20)

iconLabel = Label(mainApp)
iconLabel.pack()
iconLabel['background'] = '#c2c5d1'

locationLabel = Label(mainApp, font=('Arial', 40))
locationLabel.pack()
locationLabel['background'] = '#e9eaf2'

tempLabel = Label(mainApp, font=('Arial', 50, 'bold'))
tempLabel.pack()
tempLabel['background'] = '#e9eaf2'

conditionLabel = Label(mainApp, font=('Arial', 20))
conditionLabel.pack()
tempLabel['background'] = '#e9eaf2'


mainApp.mainloop()
