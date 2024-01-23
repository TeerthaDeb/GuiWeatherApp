from geopy.geocoders import Nominatim
from geopy import exc as geopy_exc
import tkinter as tk
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def getWeather():
    try:
        City = text_field.get()

        geolocator = Nominatim(user_agent="your_unique_user_agent")
        location = geolocator.geocode(City)

        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            print(result)
            home = pytz.timezone(result)
            local_time = datetime.now(home)
            current_time  = local_time.strftime("%I:%M %P")
            clock.config(text = current_time)
            name.config(text="CURRENT WEATHER")
        else:
            print("Location not found")

    except geopy_exc.GeocoderInsufficientPrivileges as e:
        print(f"Geocoder error: {e}")
        # Handle 403 error, maybe display a message to the user

    except Exception as e:
        print(f"An error occurred: {e}")


# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Search Box
search_image = tk.PhotoImage(file="search.png")
myimage = tk.Label(image=search_image)
myimage.place(x=20, y=20)

# Text Field
text_field = tk.Entry(root, justify="center", width=17, font=("popints", 25, "bold"), bg="#404040", border=0, fg="white")
text_field.place(x=50, y=40)
text_field.focus()

# Search Icon Button
search_icon = tk.PhotoImage(file="search_icon.png")
myimage_icon = tk.Button(image=search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
logo_image = tk.PhotoImage(file="logo.png")
logo = tk.Label(image=logo_image)
logo.place(x=150, y=100)

# time
name = tk.Label(root , font = ("arial" , 15 , "bold"))
name.place(x = 30 , y = 100)
clock = tk.Label(root , font = ("Gelvetica" , 20))
clock.place(x = 30 , y = 130)

# Bottom Box
frame_image = tk.PhotoImage(file="box.png")
bottom_image = tk.Label(image=frame_image)
bottom_image.pack(padx=5, pady=5, side="bottom")

# Labels
label1 = tk.Label(root, text="Wind", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="Humidity", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = tk.Label(root, text="Description", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = tk.Label(root, text="Pressure", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

# Labels Details
wind_label = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
wind_label.place(x=120, y=430)

humidity_label = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
humidity_label.place(x=280, y=430)

description_label = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
description_label.place(x=450, y=430)

pressure_label = tk.Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
pressure_label.place(x=670, y=430)

root.mainloop()  # Creates a window for the app