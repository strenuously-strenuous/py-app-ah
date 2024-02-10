# from bard

import tkinter as tk
import json
from tkinter import Scrollbar

class EntryForm:
    def __init__(self, master):
        self.master = master
        
        self.heading = tk.Label(master, text='Package heading')
        self.heading.pack()
        self.headding_entry = tk.Entry(master)
        self.headding_entry.pack()
        
        self.subheading = tk.Label(master, text='Package sub-heading')
        self.subheading.pack()
        self.subheadding_entry = tk.Entry(master)
        self.subheadding_entry.pack()
        
        # Entry field for number of entries
        self.num_entries_label = tk.Label(master, text="Overview:-Number of entries:")
        self.num_entries_label.pack()
        self.num_entries_entry = tk.Entry(master)
        self.num_entries_entry.pack()

        # Create entry fields on button click
        self.create_entries_button = tk.Button(master, text="Create Entries", command=self.create_entries)
        self.create_entries_button.pack()
        
        self.map = tk.Label(master, text="Enter map coordinates")
        self.map.pack()

        self.frame = tk.Frame(master)
        self.frame.pack()
        
        
        self.map_entry = tk.Entry(master)
        self.map_entry.pack()

        # Entry and error handling setup
        self.entries = []  # Store entry widgets for easy access
        self.error_label = None  # Initialize placeholder for error messages
        
        # Submit button and JSON creation
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_data)
        self.submit_button.pack()

    def create_entries(self):
        try:
            num_entries = int(self.num_entries_entry.get())
            if num_entries <= 0:
                raise ValueError("Number of entries must be positive.")

            # Clear existing entries if any
            self.clear_entries()

            # Create entry widgets
            for i in range(num_entries):
                entry_label = tk.Label(self.master, text=f"Overview - Heading {i + 1}:")
                entry_label.pack()
                entry_widget = tk.Entry(self.master)
                entry_widget.pack()
                
                entry_label_text = tk.Label(self.master, text=f"Overview - Text {i + 1}:")
                entry_label_text.pack()
                entry_widget_text = tk.Entry(self.master)
                entry_widget_text.pack()

                self.entries.append(entry_widget)

                # Enable submit button once entries are created
                self.submit_button.config(state=tk.NORMAL)

        except ValueError as e:
            self.show_error("Invalid input: " + str(e))

    def create_packages(self):
        try:
            num_entries = int(self.num_entries_entry.get())
            if num_entries <= 0:
                raise ValueError("Number of entries must be positive.")

            # Clear existing entries if any
            self.clear_entries()

            # Create entry widgets
            for i in range(num_entries):
                entry_label = tk.Label(self.master, text=f"Overview - Heading {i + 1}:")
                entry_label.pack()
                entry_widget = tk.Entry(self.master)
                entry_widget.pack()
                
                entry_label_text = tk.Label(self.master, text=f"Overview - Text {i + 1}:")
                entry_label_text.pack()
                entry_widget_text = tk.Entry(self.master)
                entry_widget_text.pack()

                self.entries.append(entry_widget)

                # Enable submit button once entries are created
                self.submit_button.config(state=tk.NORMAL)

        except ValueError as e:
            self.show_error("Invalid input: " + str(e))

    def clear_entries(self):
        # Destroy existing entry widgets and error label
        for widget in self.entries:
            widget.destroy()
        self.entries = []
        if self.error_label:
            self.error_label.destroy()
            self.error_label = None

    def submit_data(self):
        try:
            data = []
            for entry in self.entries:
                value = entry.get().strip()
                if not value:
                    raise ValueError("All entries must be filled.")
                data.append(value)

            # Create JSON file
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

            self.show_success("Data saved successfully!")

        except ValueError as e:
            self.show_error("Error: " + str(e))

    def show_error(self, message):
        if not self.error_label:
            self.error_label = tk.Label(self.master, text=message, fg="red")
            self.error_label.pack()
        else:
            self.error_label.config(text=message)

    def show_success(self, message):
        self.show_error(message, fg="green")  # Use error label for success message with green color



if __name__ == "__main__":
    root = tk.Tk()
    
    # main
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=1)
    
    # canvas
    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side='left', fill='both', expand=1)

    # scrollbar
    my_scrollbar = tk.Scrollbar(main_frame, orient='vertical', command=my_canvas.yview)
    my_scrollbar.pack(side='right', fill='y')
    
    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    )
    
    second_frame = tk.Frame(my_canvas, width = 1000, height = 100)
    btn1 = tk.Button(second_frame,
                    text="Browse...",
                    compound="left",
                    fg="blue", width=22,
                    font=("bold", 10),
                    height=1,
                    )

    btn1.place(x=600, y=0)

    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")
    
    
    app = EntryForm(second_frame)
    root.geometry('600x600')
    root.title("JSON Data Entry")
    
    root.mainloop()
