import tkinter as tk
import tkinter.font as tkfont
from PIL import Image, ImageTk

class TemperatureConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry('500x300')
        self.resizable(False, False)

        self.mode = "Fahrenheit"
        self.mode1 = "Celsius"
        self.mode2 = "Kelvin"
        self.create_widgets()

    def create_widgets(self):
        # Load and set the background image
        self.bg_image = Image.open("D:/background.jpg")  # Replace with your image path
        self.bg_image = self.bg_image.resize((500, 300), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self, width=500, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Define fonts with white color
        custom_font = tkfont.Font(family="Helvetica", size=20, weight="bold")
        custom_font2 = tkfont.Font(family="Times New Roman", size=14)
        custom_font3 = tkfont.Font(family="Times New Roman", size=12, weight="bold")

        # Draw text directly on the canvas
        self.canvas.create_text(250, 20, text="Temperature Calculator", font=custom_font, fill="white")
        self.mode_text_id = self.canvas.create_text(165, 80, text=f"Enter the temperature in {self.mode}", font=custom_font2, fill="white")
        self.mode1_text_id = self.canvas.create_text(60, 120, text=f"{self.mode1}", font=custom_font2, fill="white")
        self.mode2_text_id = self.canvas.create_text(60, 160, text=f"{self.mode2}", font=custom_font2, fill="white")

        # Display Entry and Buttons on the canvas
        self.e1 = tk.Entry(self, font=custom_font3)
        self.canvas.create_window(335, 70, anchor="nw", window=self.e1)

        # Drawing the result text directly on the canvas
        self.result_text_id = self.canvas.create_text(335, 120, anchor="nw", text="", font=custom_font3, fill="white")
        self.result_text_id2 = self.canvas.create_text(335, 160, anchor="nw", text="", font=custom_font3, fill="white")

        self.b1 = tk.Button(self, text="Calculate", font=custom_font3, command=self.convert)
        self.b2 = tk.Button(self, text="Close", font=custom_font3, command=self.destroy)
        self.b3 = tk.Button(self, text="Clear", font=custom_font3, command=self.clear)
        self.b4 = tk.Button(self, text="Switch", font=custom_font3, command=self.switch_mode)

        self.canvas.create_window(20, 220, anchor="nw", window=self.b1)
        self.canvas.create_window(150, 220, anchor="nw", window=self.b3)
        self.canvas.create_window(250, 220, anchor="nw", window=self.b2)
        self.canvas.create_window(350, 220, anchor="nw", window=self.b4)

    def convert(self):
        try:
            temp = float(self.e1.get())
            if self.mode == "Celsius":
                f = (temp * 9/5) + 32
                k = temp + 273.15
                self.canvas.itemconfig(self.result_text_id, text=f"{f:.2f}°F")
                self.canvas.itemconfig(self.result_text_id2, text=f"{k:.2f}K")
            elif self.mode == "Fahrenheit":
                c = (temp - 32) * 5/9
                k = c + 273.15
                self.canvas.itemconfig(self.result_text_id, text=f"{c:.2f}°C")
                self.canvas.itemconfig(self.result_text_id2, text=f"{k:.2f}K")
            elif self.mode == "Kelvin":
                c = temp - 273.15
                f = (c * 9/5) + 32
                self.canvas.itemconfig(self.result_text_id, text=f"{c:.2f}°C")
                self.canvas.itemconfig(self.result_text_id2, text=f"{f:.2f}°F")
        except ValueError:
            self.canvas.itemconfig(self.result_text_id, text="Invalid input")
            self.canvas.itemconfig(self.result_text_id2, text="")

    def switch_mode(self):
        # Switch between modes and update text
        if self.mode == "Celsius":
            self.mode = "Fahrenheit"
            self.mode1 = "Celsius"
            self.mode2 = "Kelvin"
        elif self.mode == "Fahrenheit":
            self.mode = "Kelvin"
            self.mode1 = "Celsius"
            self.mode2 = "Fahrenheit"
        elif self.mode == "Kelvin":
            self.mode = "Celsius"
            self.mode1 = "Fahrenheit"
            self.mode2 = "Kelvin"

        self.canvas.itemconfig(self.mode_text_id, text=f"Enter the temperature in {self.mode}")
        self.canvas.itemconfig(self.mode1_text_id, text=f"{self.mode1}")
        self.canvas.itemconfig(self.mode2_text_id, text=f"{self.mode2}")
        self.clear()

    def clear(self):
        self.e1.delete(0, tk.END)
        self.canvas.itemconfig(self.result_text_id, text="")
        self.canvas.itemconfig(self.result_text_id2, text="")

# Running the application
if __name__ == "__main__":
    app = TemperatureConverter()
    app.mainloop()
