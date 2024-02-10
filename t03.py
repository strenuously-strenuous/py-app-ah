import tkinter as tk
import json

class EntryForm:
    def __init__(self, master):
        self.master = master
        self.master.title("JSON Data Entry for Kashmir Trip")

        # Initial JSON structure with placeholders and example data
        self.json_data = {
            "heading": "Whispers of the Valley: Unveil Kashmir's Hidden Gems",
            "subHeading": "Srinagar in Kashmir",
            "overview": [
                {
                    "heading": "Exploring the Enchantment of Kashmir...",
                    "text": "**Replace with your overview text.**"
                },
                # ... more overview examples
            ],
            "mapSrc": "https://www.google.com/maps/...",  # Placeholder
            "packageOptions": [
                {
                    "package": "Deluxe",
                    "price": "₹14,999",
                    "previousPrice": "₹17,999",
                    "hotelsName": ["K2 Inn", "Hotel Curio's", "Royal Milad"]
                },
                # ... more package examples
            ],
            "carouselImageUrl": ["/productKasauli1.jpg", ...],  # Placeholders
            "exclusions": ["Departure Taxes", ...],  # Example data
            "inclusions": ["Specialized bilingual guide", ...],  # Example data
            "itinerary": [
                {
                    "day": "Day 1",
                    "day1Heading": "Arrival in Srinagar",
                    "day1Overview": "**Describe your Day 1 activities.**"
                },
                # ... more itinerary examples
            ],
        }

        # Create entry fields for each key and populate with initial data
        for key, value in self.json_data.items():
            if isinstance(value, list):
                # Handle lists (overview, packageOptions, carouselImageUrl, exclusions, inclusions, itinerary)
                self.create_list_entry_fields(key, value)
            else:
                # Handle other values (heading, subHeading, mapSrc)
                self.create_single_entry_field(key, value)

        # Submit button and JSON creation
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_data)
        self.submit_button.pack()

        # Error label and success message
        self.error_label = None
        self.success_label = None

    def create_list_entry_fields(self, key, value):
        label = tk.Label(self.master, text=f"{key}:")
        label.pack()

        # Optionally display initial data as examples
        for item in value:
            label = tk.Label(self.master, text=f"- {item}", foreground="gray")
            label.pack()

        num_entries_label = tk.Label(self.master, text=f"Number of entries for {key}:")
        num_entries_label.pack()
        num_entries_entry = tk.Entry(self.master)
        num_entries_entry.pack()

        # Dynamically create entry widgets based on user-entered number
        self.entry_widgets[key] = []
        for _ in range(int(num_entries_entry.get())):
            entry_widget = tk.Entry(self.master)
            entry_widget.pack()
            self.entry_widgets[key].append(entry_widget)

    def create_single_entry_field(self, key, value):
        label = tk.Label(self.master, text=f"{key}:")
        label.pack()
        entry_widget = tk.Entry(self.master)
        entry_widget.insert(0, value)  # Pre-populate with initial value
        entry_widget.pack()
        self.entry_widgets[key] = entry_widget

    def submit_data(self):
        # Clear existing messages
        if self.error_label:
            self.error_label.destroy
