class Book:
    # Constructor method
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor method
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation method
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation method
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
