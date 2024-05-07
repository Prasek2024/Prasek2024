




class SeasonFinder:
    def __init__(self, month_number):
        self.month_number = month_number

    def find_season(self):
        if 1 <= self.month_number <= 12:
            if self.month_number in (12, 1, 2):
                return "Winter"
            elif self.month_number in (3, 4, 5):
                return "Spring"
            elif self.month_number in (6, 7, 8):
                return "Summer"
            elif self.month_number in (9, 10, 11):
                return "Autumn"
        else:
            return "Error: The month number is out of range. Please enter a number from 1 to 12."

if __name__ == "__main__":
    try:
      user_input = int(input("Please enter the number of the month (from 1 to 12): "))
      finder = SeasonFinder(user_input)
      result = finder.find_season()
      print(result)
    except ValueError:
        print("Error: Please enter a valid integer number.")