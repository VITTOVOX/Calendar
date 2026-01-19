


# calendar_app.py
import calendar
from datetime import datetime

# =====================
# Constants
# =====================
MIN_YEAR = 1
MAX_YEAR = 9999


# =====================
# Validation Helpers
# =====================
def is_valid_year(year: int) -> bool:
    """Return True if year is within allowed range."""
    return MIN_YEAR <= year <= MAX_YEAR


def is_valid_month(month: int) -> bool:
    """Return True if month is between 1 and 12."""
    return 1 <= month <= 12


# =====================
# Calendar Logic
# =====================
def get_month_calendar(year: int, month: int) -> str:
    """Return a formatted calendar for a specific month."""
    return calendar.month(year, month)


def get_year_calendar(year: int) -> str:
    """Return a formatted calendar for a full year."""
    return calendar.calendar(year)


def get_today_info() -> str:
    """Return today's date with weekday."""
    today = datetime.now()
    weekday = calendar.day_name[today.weekday()]
    return f"Today is {weekday}, {today.day}-{today.month}-{today.year}"


def get_weekday(year: int, month: int, day: int) -> str:
    """Return weekday name for a given date."""
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]


# =====================
# Input Utilities
# =====================
def get_int_input(prompt: str) -> int:
    """Safely get an integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number.")


# =====================
# Menu Handlers
# =====================
def show_menu() -> None:
    """Display the main menu."""
    print("\n📅 Simple Calendar App")
    print("1. View a month")
    print("2. View a year")
    print("3. Show today's date")
    print("4. Find weekday of a date")
    print("5. Exit")


def view_month() -> None:
    year = get_int_input("Enter year (e.g., 2025): ")
    month = get_int_input("Enter month (1-12): ")

    if not (is_valid_year(year) and is_valid_month(month)):
        print("❌ Invalid year or month.")
        return

    print(get_month_calendar(year, month))


def view_year() -> None:
    year = get_int_input("Enter year (e.g., 2025): ")

    if not is_valid_year(year):
        print("❌ Invalid year.")
        return

    print(get_year_calendar(year))


def find_weekday_handler() -> None:
    year = get_int_input("Enter year: ")
    month = get_int_input("Enter month: ")
    day = get_int_input("Enter day: ")

    try:
        weekday = get_weekday(year, month, day)
        print(f"📆 That date falls on a {weekday}")
    except ValueError:
        print("❌ Invalid date entered.")


# =====================
# Main Application Loop
# =====================
def main() -> None:
    """Run the calendar application."""
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_month()
        elif choice == "2":
            view_year()
        elif choice == "3":
            print(get_today_info())
        elif choice == "4":
            find_weekday_handler()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()





