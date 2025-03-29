import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from speech_recognition_handler import SpeechRecognition
from plot_distributions import plot_distribution

class DistributionPlotter(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize main window
        self.title("Distribution Plotter with Speech Recognition")
        self.geometry("800x600")
        self.configure(bg='#f0f8ff')

        # Create a top frame to hold the logo
        self.logo_frame = tk.Frame(self, bg='#f0f8ff')
        self.logo_frame.pack(pady=20)

        # Set the logo path directly
        self.logo_path = "distribution logo.jpg"

        try:
            # Load the logo image
            logo_image = Image.open(self.logo_path)
            logo_image = logo_image.resize((100, 100))
            self.logo_tk = ImageTk.PhotoImage(logo_image)

            # Add the logo to the GUI
            self.logo_label = tk.Label(self.logo_frame, image=self.logo_tk, bg='#f0f8ff')
            self.logo_label.pack()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load the logo image: {e}")

        # Add a label with nice font and color
        self.title_label = tk.Label(self, text="Distribution Plotter", font=("Arial", 24, "bold"), bg='#f0f8ff', fg='#4CAF50')
        self.title_label.pack(pady=10)

        # Create a frame for holding the button at the bottom
        self.button_frame = tk.Frame(self, bg='#f0f8ff')
        self.button_frame.pack(side="bottom", pady=30)

        # Label to show the result of the voice command
        self.result_label = tk.Label(self, text="Voice Command Result will show here", wraplength=500,
                                     font=("Arial", 12), bg="#f0f8ff", fg="#333")
        self.result_label.pack(pady=10)

        # Set up the button to trigger speech recognition
        self.plot_button = tk.Button(self.button_frame, text="Select Distribution with Voice", command=self.on_button_click,
                                     bg="#4CAF50", fg="white", font=("Arial", 14), padx=10, pady=5)
        self.plot_button.pack()

        self.speech_recognition = SpeechRecognition()

        # Add a label with small font at the bottom right corner, with text on two lines
        self.footer_label = tk.Label(self, text="Programmed by:\nSiddhartha (409)\n Monish Reddy (410)",
                                     font=("Arial", 8), bg="#f0f8ff", fg="#333")
        self.footer_label.place(relx=0.99, rely=0.99, anchor="se")  # Adjusted position without padx/pady

    def on_button_click(self):
        # Get the distribution type from voice command
        distribution_type = self.speech_recognition.get_distribution_from_voice()

        if not distribution_type:
            messagebox.showerror("Error", "No valid distribution selected.")
            return

        # Update label with the selected distribution
        self.result_label.config(text=f"Selected Distribution: {distribution_type.capitalize()}")

        # Generate and plot the distribution
        plot_distribution(distribution_type)
