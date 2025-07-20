from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

# Query 2: All books in a specific library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

# Query 3: Retrieve the librarian of a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")
