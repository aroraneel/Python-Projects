# Import the tkinter module to create the graphical user interface (GUI)
import tkinter as tk

# Import strftime from the time module to get the current date and time
from time import strftime

# Create the main application window
root = tk.Tk()

# Set the title of the application window
root.title("Digital Clock")

# -------------------- Clock Function --------------------

# Function to update the current time and date every second
def time():

    # Get the current time and date
    # %I = Hour (12-hour format)
    # %M = Minutes
    # %S = Seconds
    # %p = AM/PM
    # %A = Full weekday name
    # %d = Day of the month
    # %B = Full month name
    # %Y = Year
    string = strftime('%I:%M:%S %p\n%A, %d %B %Y')

    # Update the label with the current time and date
    label.config(text=string)

    # Call this function again after 1000 milliseconds (1 second)
    label.after(1000, time)

# -------------------- Create Label --------------------

# Create a label to display the time and date
label = tk.Label(
    root,
    font=("ds-digital", 50),   # Set font style and size
    background="black",        # Set background color
    foreground="cyan"          # Set text color
)

# Place the label in the center of the window
label.pack(anchor="center")

# Start updating the clock
time()

# -------------------- Run Application --------------------

# Keep the window open and running until the user closes it
root.mainloop()