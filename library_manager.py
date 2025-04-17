import os
import json

data_file= "library.txt"

def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
        return []
    
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file)

def add_book(library):
    title= input("Enter the title of book")
    author= input("Enter the author of book")
    year= input("Enter the year of book")
    genre= input("Enter the genre of book")
    read= input("Have you read the book yes/no?").lower() == "yes"

    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_library(library)
    print("Book added successfully!")     

def remove_book(library):
    title= input("Enter the book title you want to remove")    
    initial_length= len(library)
    library= [book for book in library if book["title"].lower() != "title"]
    if len(library) < initial_length:
        save_library(library)
        print("Book removed successfully")
    else:
        print(f"Book {title} not found in library")

def search_library(library):
    search_by= input("Search by author or book title: ").lower()
    
    if search_by not in ["author", "title"]:
        print("Invalid search field. Please search by 'author' or 'book title'.")
        return

    
    search_term= input(f"Enter the {search_by}: ").lower()

    results= [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book["read"] else "unread"
            title= book["title"]
            author= book["author"]
            year= book["year"]
            genre= book["genre"]
            print(f"{title} by {author} - {year} - {genre} - {status}")
    else:
        print(f"No book available with {search_term} in the {search_by} field")       

def display_all_books(library):
    if library:
        for book in library:
            status= "Read" if book["read"] else "Unread"
            print(f"{book["title"]} by {book["author"]} - {book["year"]} - {book["genre"]} - {status}")
    else:
        print("The library is empty")

def display_statistics(library):
    total_books= len(library)
    read_books= len([book for book in library if book["read"]])
    percentage_read= (read_books/total_books)*100 if read_books>0 else 0

    print(f"Total books: {total_books}")
    print(f"Read percentage: {percentage_read}")

def main():
    library= load_library()
    while True:
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice= input("Type the number of option you want to select: ")
        if choice== "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Good bye!")
            break

        else:
            print("Invalid choice, please select a number from 1 to 6")

if __name__ == "__main__":
    main()