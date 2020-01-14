class Library:
    def __init__(self, name, list):
        self.name = name
        self.bookList = list
        self.lenDict = {}
    def displayBook(self, list):
        print(f"Here the books in library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self, user, book):
        print("Enter the book you want to lend")
        if book not in self.lenDict.keys():
            self.lenDict.update({book:user})
            print("books are updated, you can take the book")
        else:
            print(f"book is already deliverd {self.lenDict[book]}")


    def addBook(self, book):
        self.bookList.append(book)
        print("book is added in the booklist")
    def returnBook(self, book):
        self.bookList.remove(book)
        print("book has been returned")

if __name__ == '__main__':
    tippecano = Library('tiplibrary', ['Python', 'C++', 'Java', 'HTML', 'Machine Learning', 'Deep Learning'])
    while(True):
        print(f"Welcome to the {tippecano.name}. Enter your choice to continue")
        print("1. for display books")
        print("2. for lend books")
        print("3. for add books")
        print("4. for return books")
        user_choice = int(input())
        if user_choice == 1:
            tippecano.displayBook(list)
        elif user_choice ==2:
            book = input("Enter the  name of the book you want to lend")
            user = input("Enter your name")
            tippecano.lendBook(user, book)
        elif user_choice == 3:
            book = input("enter the book you want to add")
            tippecano.addBook(book)
        elif user_choice == 4:
            book = input("Enter the book you want to return:")
            tippecano.returnBook(book)
        else:
            print("invalid entry:")
        print("press c for continue and q for quiet: ")
        user_choice2 =""

        while(user_choice2!= 'c'and user_choice2!= 'q'):
            user_choice2 = input()
            if user_choice2 == 'q':
                exit()
            elif user_choice2 == 'c':
                continue


