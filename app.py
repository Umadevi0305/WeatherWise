import tkinter as tk
from tkinter import messagebox
import random

class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather App")

        self.city_label = tk.Label(master, text="Enter city:")
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(master, width=30)
        self.city_entry.pack(pady=10)

        self.get_weather_button = tk.Button(master, text="Get Weather", command=self.display_weather)
        self.get_weather_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def generate_fake_weather(self):
        # Generate random temperature and description for demonstration purposes
        temperature = round(random.uniform(10, 30), 2)
        descriptions = ["Clear sky", "Partly cloudy", "Cloudy", "Light rain", "Thunderstorm"]
        description = random.choice(descriptions)

        return {
            'main': {'temp': temperature},
            'weather': [{'description': description}]
        }

    def display_weather(self):
        city = self.city_entry.get()

        if not city:
            messagebox.showwarning("Warning", "Please enter a city name.")
            return

        weather_data = self.generate_fake_weather()

        if weather_data:
            try:
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                result_text = f"Temperature: {temperature}°C\nDescription: {description}"
                self.result_label.config(text=result_text)
            except KeyError as e:
                print(f"Error parsing weather data: {e}")
                self.result_label.config(text="Error parsing weather data.")
        else:
            self.result_label.config(text="Error fetching weather data.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()