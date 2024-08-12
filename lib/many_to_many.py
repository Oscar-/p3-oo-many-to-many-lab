class Author:

    all = []

    def __init__(self, name):
        self.name = name

    def contracts(self):
         related_contracts = []
         for contract in Contract.all:
              if(contract.author == self):
                   related_contracts.append(contract)
                   return related_contracts
                   

    def books(self):
        #  related_books = []
        #  for contract in Contract.all:
        #       if(contract.book == self):
        #            related_books.append(self)
        #            return related_books
        return list(set([contract.book for contract in self.contracts()]))
                   

    def sign_contract(self, book, date, royalties):
         return Contract(self,book,date,royalties)
              
        

    def total_royalties(self):
         grand_total = 0
         for contract in Contract.all: 
              if(contract.author == self):
                   grand_total += contract.royalties
         return grand_total
            

    def __repr__(self):
        return f'<Author name={self.name} />'
    


class Book:
    
    all = []

    def __init__(self, title):
        self.title = title

    def contracts(self):
          similar_contracts = []
          for contract in Contract.all:
              if(contract.book == self):
                   similar_contracts.append(contract)
                   return similar_contracts
              
    def authors(self):
         return list(set([contract.author for contract in self.contracts()]))
         

    def __repr__(self):
        return f'<Book name={self.title} />'
        


class Contract:

    all = []
    
    

    def __init__(self, author, book, date, royalties):
        self.author = author 
        self.book = book 
        self.date = date 
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod 
    def contracts_by_date(cls,date):
         matching_contract = []
         for contract in cls.all:
              if contract.date == date: 
                   matching_contract.append(contract)
         return matching_contract
                   

 
    @property 
    def author(self): 
        return self._author
        
    @author.setter
    def author(self, value):
        if(isinstance(value, Author)):
                self._author = value
        else:
            raise Exception("Author must be a type of author")
        
    @property 
    def book(self): 
        return self._book
        
    @book.setter
    def book(self, value):
        if(isinstance(value, Book)):
                self._book = value
        else:
            raise Exception("Book must be a type of book")
        
    @property 
    def date(self): 
        return self._date
        
    @date.setter
    def date(self, value):
        if(isinstance(value, str)):
                self._date = value
        else:
            raise Exception("Date must be a type of date")
        
    @property 
    def royalties(self): 
        return self._royalties
        
    @royalties.setter
    def royalties(self, value):
        if(isinstance(value, int)):
                self._royalties = value
        else:
            raise Exception("Royalties must be a type of royalties")
        
        
    def __repr__(self):
         pass
        # return f'<Contract name={self.title} />'
            
                