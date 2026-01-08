# calendar_app.py
import calendar
from datetime import datetime

# Constants
MIN_YEAR = 1
MAX_YEAR = 9999

def is_valid_year(year):
    """Check if year is within valid range."""
    return MIN_YEAR <= year <= MAX_YEAR

def is_valid_month(month):
    """Check if month is valid."""
    return 1 <= month <= 12

def display_month(year, month):
    """Return the calendar for a specific month and year."""
    return calendar.month(year, month)

def display_year(year):
    """Return the calendar for an entire year."""
    return calendar.calendar(year)

def show_today():
    """Display today's date and weekday."""
    today = datetime.now()
    weekday = calendar.day_name[today.weekday()]
    return f"Today is {weekday}, {today.day}-{today.month}-{today.year}"

def find_weekday(year, month, day):
    """Find the weekday for a specific date."""
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]

def get_int_input(prompt):
    """Safely get an integer from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")

def main_menu():
    """Display the main menu."""
    print("\n📅 Simple Calendar App")
    print("1. View a month")
    print("2. View a year")
    print("3. Show today's date")
    print("4. Find weekday of a date")
    print("5. Exit")

def main():
    while True:
        main_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            year = get_int_input("Enter year (e.g., 2025): ")
            month = get_int_input("Enter month (1-12): ")

            if is_valid_year(year) and is_valid_month(month):
                print(display_month(year, month))
            else:
                print("❌ Invalid year or month.")

        elif choice == "2":
            year = get_int_input("Enter year (e.g., 2025): ")

            if is_valid_year(year):
                print(display_year(year))
            else:
                print("❌ Invalid year.")

        elif choice == "3":
            print(show_today())

        elif choice == "4":
            year = get_int_input("Enter year: ")
            month = get_int_input("Enter month: ")
            day = get_int_input("Enter day: ")

            try:
                weekday = find_weekday(year, month, day)
                print(f"📆 That date falls on a {weekday}")
            except ValueError:
                print("❌ Invalid date entered.")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please select 1–5.")

if __name__ == "__main__":
    main()