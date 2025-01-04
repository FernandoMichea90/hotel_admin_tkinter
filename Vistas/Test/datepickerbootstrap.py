import ttkbootstrap as ttk
from ttkbootstrap.widgets import DateEntry

class DatePickerView(ttk.Window):
    def __init__(self):
        super().__init__(themename="cosmo")
        self.title("Date Picker Example")
        self.geometry("300x200")
        
        # Create a frame
        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)
        
        # Add a label
        label = ttk.Label(frame, text="Select a date:")
        label.pack(pady=10)
        
        # Add a date picker
        date_entry = DateEntry(frame, bootstyle="primary")
        date_entry.pack(pady=10)
        
        # Add a button to print the selected date
        button = ttk.Button(frame, text="Print Date", command=lambda: self.print_date(date_entry))
        button.pack(pady=10)
    
    def print_date(self, date_entry):
        selected_date = date_entry.entry.get()
        print(f"Selected Date: {selected_date}")

if __name__ == "__main__":
    app = DatePickerView()
    app.mainloop()
