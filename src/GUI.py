import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from main import download_video
from main import preview


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="white")
        self.grid(sticky="nsew")
        self.create_widgets()

    def create_widgets(self):
        # Add empty rows and columns for padding and centering
        for i in range(6):  # Adjust based on the number of rows
            self.grid_rowconfigure(i, weight=1)
        for i in range(5):  # Adjust based on the number of columns (5 including padding)
            self.grid_columnconfigure(i, weight=1)

        # Welcome label
        self.label = tk.Label(self, text="YouTube Downloader", font=("Arial", 15), bg="white")
        self.label.grid(row=0, column=1, columnspan=3, pady=10, sticky="nsew")  # Span across columns 1 to 3

        # URL label
        url_label = tk.Label(self, text="Enter YouTube URL:", bg="white", fg="black")
        url_label.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="nsew")  # Span across columns 1 to 3

        # Entry for video URL
        self.url_entry = tk.Entry(self, width=50, bg="white", fg="black", justify="center")
        self.url_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="nsew")  # Span across columns 1 to 3

        # Format label
        format_label = tk.Label(self, text="Choose a format:", bg="white", fg="black")
        format_label.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="nsew")  # Span across columns 1 to 3

        # Value of selected radio button
        self.var = tk.StringVar()
        self.var.set(".mp4")  # Default value

        # Radio buttons
        radio_frame = tk.Frame(self, bg="white")  # Frame for radio buttons
        radio_frame.grid(row=4, column=1, columnspan=3, padx=10, pady=5)  # Span across columns 1 to 3

        radio1 = ttk.Radiobutton(radio_frame, text="MP4", variable=self.var, value=".mp4", style="TRadiobutton")
        radio1.pack(side=tk.LEFT, padx=10)  # Pack radio buttons side by side

        radio2 = ttk.Radiobutton(radio_frame, text="MP3", variable=self.var, value=".mp3", style="TRadiobutton")
        radio2.pack(side=tk.LEFT, padx=10)  # Pack radio buttons side by side

        radio_frame.grid_columnconfigure(0, weight=1)
        radio_frame.grid_columnconfigure(1, weight=1)
        radio_frame.grid_columnconfigure(2, weight=1)

        # Preview button
        preview_button = ttk.Button(self, text="Preview",style="TButton", command=self.preview_submit)
        preview_button.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")  # Place in column 1

        # Download button
        download_button = ttk.Button(self, text="Submit", style="TButton", command=self.download_submit)
        download_button.grid(row=5, column=3, padx=10, pady=10, sticky="nsew")  # Place in column 3

    def preview_submit(self):
        video_url = self.url_entry.get()
        if video_url:
            try:
                author, title, views = preview(video_url)
                messagebox.showinfo("File", f"Title: {author} {title}\nViews: {views}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
        else:
            messagebox.showwarning("Input Error", "Please enter a YouTube URL")

    def download_submit(self):
        video_url = self.url_entry.get()
        if video_url:
            try:
                author, title, views = download_video(video_url, self.var.get())
                messagebox.showinfo("Success", f"Downloaded: {author} - {title}\nViews: {views}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")
        else:
            messagebox.showwarning("Input Error", "Please enter a YouTube URL")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    # Create a style object
    style = ttk.Style()

    # Style for buttons
    style.configure("TButton", foreground="black", background="white", font=("Arial", 12), padding=5, )
    # Style for radio buttons
    style.configure("TRadiobutton", background="white", font=("Arial", 12), padding=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube-Downloader")
    root.minsize(width=750, height=500)
    center_window(root, 750, 500)
    root.iconbitmap(r"C:\Users\seba-\PycharmProjects\YouTube-downloader\src\Images\icon.ico")
    root.config(bg="white")

    # Allow main window to stretch with the frame
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # Create Application frame and allow it to stretch
    myapp = Application(root)
    myapp.grid(sticky="nsew")

    root.mainloop()


