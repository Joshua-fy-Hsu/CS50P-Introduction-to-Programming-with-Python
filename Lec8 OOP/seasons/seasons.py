from datetime import date
import sys
import inflect


def main():
    birth_str = input("Date of Birth: ")
    calc = SeasonCalculator(birth_str)
    print(calc.in_words() + " minutes")


class SeasonCalculator:
    def __init__(self, birth_date_str):
        try:
            self.birth_date = date.fromisoformat(birth_date_str)
        except ValueError:
            sys.exit("Invalid date")

        self.today = date.today()
        self.inflect_engine = inflect.engine()

    def minutes_lived(self):
        delta = self.today - self.birth_date
        return round(delta.days * 24 * 60)
    
    def in_words(self):
        minutes = self.minutes_lived()
        return self.inflect_engine.number_to_words(minutes, andword = "").capitalize()


if __name__ == "__main__":
    main()