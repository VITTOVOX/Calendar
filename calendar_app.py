# calendar_app.py
import calendar

def display_month(year, month):
    # Display the calendar for a given month and year
    return calendar.month(year, month)

def display_year(year):
    # Display the calendar for the entire year
    return calendar.calendar(year)

if __name__ == "__main__":
    print("Simple Calendar App")
    choice = input("Do you want to see a (M)onth or a (Y)ear? ").lower()

    if choice == "m":
        year = int(input("Enter year (e.g., 2025): "))
        month = int(input("Enter month (1-12): "))
        print(display_month(year, month))
    elif choice == "y":
        year = int(input("Enter year (e.g., 2025): "))
        print(display_year(year))
    else:
        print("Invalid choice")