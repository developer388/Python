"""
Library Management Software


Actors:
1. Member


2. Librarian
        can issue a book
        can receive a book
        can recieve payment by a member
        can add a new book in library
3. Admin



"""

from datetime import datetime, timedelta
from enum import Enum



class BookStatus(Enum):
    available = 'AVAILABLE'
    booked = 'BOOKED'
    unavailable = 'UNAVAILABLE'
    
    
class UserStatus(Enum):
    active = 'ACTIVE'
    inactive = 'INACTIVE'
    

class Book:
    def __init__(self, isbn, title, author, page_count):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.page_count = page_count
        

class BookItem(Book):
    def __init__(self, isbn, title, author, page_count, id, status, rack_address):
        super().__init__(isbn, title, author, page_count)
        self.id = id
        self.status = status
        self.rack_address = rack_address
        
    def updateStatus(self, status):
        self.status = status
            
    def getDetails(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'page_count': self.page_count,
            'id': self.id,
            'status': self.status,
            'rack_address': self.rack_address
        }

class Rack:
    def __init__(self, id, row_count, column_count):
        self.rack = {}
        
        for row in range(row_count):
            for col in range(column_count):
                self.rack[id + '-' + str(row+1) + '-' + str(col+1)] = []
        
        
    def getDetails(self):
        return self.rack
    
    def addBook(self, rack_id, book_id):
        self.rack[rack_id].append(book_id)
    
    def removeBook(self, rack_id, book_id):
        self.rack[rack_id].remove(book_id)
    
    def getBooks(self, rack_id):
        return self.rack[rack_id]
    
    
class User:
    def __init__(self, id, email, phone, password, status):
        self.id = id
        self.email = email
        self.phone = phone
        self.password = password
        self.status = status
        
    def getDetails(self):
        return {
            'id': self.id,
            'email': self.email,
            'phone': self.phone,
            'password': self.password,
            'status': self.status
        }

class Member(User):
    def __init__(self, id, email, phone, password, status):
        super().__init__(id, email, phone, password, status)
        self.issued_books = []
    
    def addIssuedBook(self, book_id):
        self.issued_books.append(book_id)
    
    def removeIssuedBook(self, book_id):
        self.issued_books.remove(book_id)
    
    def getDetails(self):
        details = super().getDetails()
        details['issued_books'] = self.issued_books
        return details

class BookReservation:
    def __init__(self, book_id, days, member_id, librarian_id):
        self.book_id = book_id
        self.booking_date = datetime.now()
        self.return_date = datetime.now() + timedelta(days=+days)
        self.issued_to = member_id
        self.issued_by = librarian_id

    def getDetails(self):
        return {
            'book_id': self.book_id,
            'booking_date': self.booking_date,
            'return_date': self.return_date,
            'issued_to': self.issued_to,
            'issued_by': self.issued_by
        }

class Librarian(User):
    def __init__(self,  id, email, phone, password, status, library):
        super().__init__(id, email, phone, password, status)
        self.library = library
    
    def addBook(self, book_item):
        library.addBook(book_item)
    
    def issueBook(self, book_id, user):
        
        book = self.library.getBook(book_id)
        
        print('b', book.getDetails())
        
        if book and book.status == BookStatus.available.value:
            book.updateStatus(BookStatus.unavailable.value)
            user.addIssuedBook(book_id)
            rack = self.library.rack
            rack.removeBook(book.rack_address, book.id)
        else:
            print('Book not available')     
            
        reservation = BookReservation(book_id, 15, user.id, self.id)
        return reservation

class Library:
    def __init__(self, rack):
        self.book_list = {}
        self.rack = rack
        
    def addBook(self, book_item):
        library.book_list[book_item.id] = book_item
        self.rack.addBook(book_item.rack_address, book_item.id)
    
    def getBook(self, book_id):
        return self.book_list.get(book_id, None)
    
    
    
rack = Rack('RACK1', 5, 10)


b1 = BookItem('EB3S424A3', 'Mathemetics RD Sharma', 'RD Sharma', 503, 1548, BookStatus.available.value, 'RACK1-1-1')
b2 = BookItem('ZD3GN5N23', 'Computer Networks', 'Taneumbom', 359, 4782, BookStatus.available.value, 'RACK1-1-1')
b3 = BookItem('B3H4D78G3', 'Computer Architechture and Organization', 'Moris Mano', 503, 8421, BookStatus.available.value, 'RACK1-1-1')
b4 = BookItem('L8M3ML9A3', 'Object Oriented Programming', 'Ballagruru Swamy', 201, 1011, BookStatus.available.value, 'RACK1-1-1')

library = Library(rack)
library.addBook(b1)
library.addBook(b2)
library.addBook(b3)
library.addBook(b4)

member = Member('USER001', 'kuak@gmail.com', '965862101', '****', UserStatus.active.value)
print(member.getDetails())


librarian = Librarian('LIBRARIAB215', 'kanishk@hellobooks.com', '8921586445', '****', UserStatus.active.value, library)
print(librarian.getDetails())


print(rack.getDetails())

reservation = librarian.issueBook(1548, member)
print(reservation.getDetails())
print(rack.getDetails())
print(b1.getDetails())
print(member.getDetails())





























