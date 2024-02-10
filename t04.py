import tkinter as tk
import json

class EntryForm:
    def __init__(self, master):
        self.master = master
        self.master.title("JSON Data Entry for Kashmir Trip")

        # Initial JSON structure with placeholders
        self.json_data = {
            "heading": tk.Entry(master).insert(0, "Whispers of the Valley: Unveil Kashmir's Hidden Gems"),
            "subHeading": tk.Entry(master).insert(0, "Srinagar in Kashmir"),
            "overview": [
                {"heading": tk.Entry(master).insert(0, "Exploring the Enchantment..."), "text": tk.Entry(master)},
                # ... more overview entries
            ],
            "mapSrc": tk.Entry(master).insert(0, "https://www.google.com/maps/..."),
            "packageOptions": [
                {"package": "Deluxe", "price": "₹14,999", "previousPrice": "₹17,999", "hotelsName": ["K2 Inn", "Hotel Curio's", "Royal Milad"]},
                # ... more package entries
            ],
            "carouselImageUrl": ["/productKasauli1.jpg", ...],
            "exclusions": ["Departure Taxes", ...],
            "inclusions": ["Specialized bilingual guide", ...],
            "itinerary": [
                {"day": "Day 1", "day1Heading": "Arrival in Srinagar", "day1Overview": tk.Entry(master)},
                # ... more itinerary entries
            ],
        }

        for key, value in self.json_data.items():
            if isinstance(value, list):
                self.create_list_entry_fields(key, value)
            else:
                value.pack()

        submit_button = tk.Button(master, text="Submit", command=self.submit_data)
        submit_button.pack()

    def create_list_entry_fields(self, key, value):
        num_entries = tk.Entry(self.master)
        num_entries.pack()
        for _ in range(int(num_entries.get())):
            for subkey in value[0]:
                tk.Entry(master, text=f"{subkey}:").pack()
                value[0][subkey] = tk.Entry(master)
                value[0][subkey].pack()

    def submit_data(self):
        # Extract user-entered data and build the final JSON
        data = {}
        for key, value in self.json_data.items():
            if isinstance(value, list):
                data[key] = []
                for item in value:
                    inner_data = {}
                    for subkey, subvalue in item.items():
                        inner_data[subkey] = subvalue.get().strip()
                    data[key].append(inner_data)
            else:
                data[key] = value.get().strip()

        # Submit the JSON data (replace with your actual submission logic)
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    root = tk.Tk()
    app = EntryForm(root)
    root.mainloop()
