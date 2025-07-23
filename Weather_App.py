import tkinter as tk
from PIL import Image, ImageTk
import requests

def format_response(weather_response):
    try:
        city = weather_response['name']
        condition = weather_response['weather'][0]['description']
        temp = weather_response['main']['temp']
        final_str = f'City: {city}\nCondition: {condition.title()}\nTemperature: {temp} °F'
    except:
        final_str = 'There was a problem retrieving the weather...'
    return final_str

def get_weather(city):
    weather_key = 'b0532ad7c22ee5be6ebbac2f695ca8f9'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}  # 'imperial' = °F
    response = requests.get(url, params)
    weather_response = response.json()

    print(f"{weather_response['name']} -----> = {weather_response['main']['temp']}")
    result['text'] = format_response(weather_response)

root = tk.Tk()
root.title("Weather_App")
root.geometry("600x500")

# Background image
img = Image.open('./bg.png')
img = img.resize((600, 500), Image.Resampling.LANCZOS)
img_photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=img_photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Heading
heading_title = tk.Label(label, text='Earth Including Over 2,00,000 Cities..!',
                         fg='red', bg='sky blue', font=('times new roman', 18, 'bold'))
heading_title.place(x=80, y=18)

# Entry + Button
frame_one = tk.Frame(label, bg='green', bd=10)
frame_one.place(x=80, y=60, width=450, height=50)

txt_box = tk.Entry(frame_one, font=('times new roman', 20, 'bold'))
txt_box.grid(row=0, column=0, sticky='w')

btn = tk.Button(frame_one, text='Get_Weather', fg='Black',
                font=('times new roman', 16, 'bold'),
                command=lambda: get_weather(txt_box.get()))
btn.grid(row=0, column=1, padx=10)

# Output frame
fram_two = tk.Frame(label, bg="#42c2f4", bd=5)
fram_two.place(x=80, y=130, width=450, height=300)

result = tk.Label(fram_two, bg='white', font=('times new roman', 14), anchor='nw', justify='left')
result.place(relwidth=1, relheight=1)

root.mainloop()
