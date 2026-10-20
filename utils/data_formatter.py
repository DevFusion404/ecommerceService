"""
Data Formatter - Transforms raw numeric data for reporting.
"""

class DataFormatter:
    def calc_dat(self, value):
        return value * 2

    def process(self, num):
        return self.calc_dat(num)

if __name__ == "__main__":
    df = DataFormatter()
    print("Formatted:", df.process(20))
