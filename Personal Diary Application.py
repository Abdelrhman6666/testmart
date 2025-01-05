import os
from datetime import datetime

# Function to create a new diary entry
def create_diary_entry(file_path, entry, add_timestamp=False):
    try:
        # Open the file in append mode. If the file doesn't exist, it will be created.
        with open(file_path, 'a') as file:
            # Optionally add timestamp
            if add_timestamp:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{timestamp}] {entry}\n")
            else:
                file.write(f"{entry}\n")
            print("Diary entry added successfully.")

    except IOError as e:
        print(f"Error writing to file: {e}")

# Function to view previous diary entries
def view_diary_entries(file_path):
    try:
        # Check if the diary file exists before attempting to read it
        if not os.path.exists(file_path):
            print("No previous entries found.")
            return
        
        # Open and read the file
        with open(file_path, 'r') as file:
            entries = file.readlines()
            if entries:
                print("\nPrevious Diary Entries:")
                for entry in entries:
                    print(entry.strip())
            else:
                print("No entries found.")
    except IOError as e:
        print(f"Error reading the file: {e}")

# Main function to handle the user's options
def main():
    diary_file = 'diary.txt'
    
    while True:
        print("\nDiary Application")
        print("1. Create a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            entry = input("Enter your diary entry: ")
            add_timestamp = input("Would you like to add a timestamp? (y/n): ").lower() == 'y'
            create_diary_entry(diary_file, entry, add_timestamp)
        
        elif choice == '2':
            view_diary_entries(diary_file)
        
        elif choice == '3':
            print("Exiting the diary application.")
            break
        
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
