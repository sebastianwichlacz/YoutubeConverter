import tkinter as tk
from tkinter import messagebox
from main import download_video
from main import preview

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # URL label
        self.label = tk.Label(self, text="Enter YouTube URL:")
        self.label.pack()

        # Entry for video URL
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack()

        # Format label
        self.label = tk.Label(self, text="Chose a format:")
        self.label.pack()

        # Value of selected radio button
        self.var = tk.StringVar()
        self.var.set(".mp4") # Default value

        # Radio buttons
        self.radio1 = tk.Radiobutton(self, text="MP4", variable=self.var, value=".mp4")
        self.radio1.pack()

        self.radio2 = tk.Radiobutton(self, text="MP3", variable=self.var, value=".mp3")
        self.radio2.pack()

        # Preview button display
        self.button2 = tk.Button(self, text="Preview", command=self.preview_submit)
        self.button2.pack()

        # Download button display
        self.button = tk.Button(self, text="Submit", command=self.download_submit)
        self.button.pack()



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
    window.geometry(f'{width}x{height}+{x}+{y}')

root = tk.Tk()
root.title("YouTube-Downloader")
root.minsize(width=750, height=500)
center_window(root, 750, 500)

#button
def on_button_click():
    label.config(text="Hello, World!")

#welcome label
label = tk.Label(root, text="Welcome to my app!")
label.pack()


myapp = Application()

root.mainloop()
