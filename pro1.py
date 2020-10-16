class Library:
    def __init__(self, list, name):
        self.BookList = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"We have following books in our library : {self.name}")
        for book in self.BookList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now!")
        else:
            print(f"Book is already bring used by {self.lendDict[book]}")

    def addBook(self, book):
        self.BookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    Library_Shell = Library(['Python', 'Java Core', 'Cosmos', 'Life of Pie', 'Web Technology', 'Java Advanced'],
                        "Home made Librabry")

    print(f"Welcome to the {Library_Shell.name} Library. ")

    while(True):

        print("1. Display a Books")
        print("2. Lend a Books")
        print("3. Add a Books")
        print("4. Return a Books")
        print("Enter your choice to continue : ")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please! Enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            Library_Shell.displayBook()
        elif user_choice == 2:
            book = input("Enter name of the book you want to lend : ")
            name = input("Enter your name : ")
            Library_Shell.lendBook(name, book)

        elif user_choice == 3:
            book = input("Enter name of the book you want to add : ")
            Library_Shell.addBook(book)
        try:
            if user_choice == 4:
                book = input("Enter name of the book you want to return : ")
                Library_Shell.returnBook(book)
            else:
                print("Please! Enter valid number")
        except KeyError:
            print("You don't have book lend, \nPlease! choose first book and lend")



        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 !="q"):

            print("Press q to quit and c to continue")
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            if user_choice2 == "c":
                continue