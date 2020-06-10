import datetime
from peewee import *


#"http://docs.peewee-orm.com/en/latest/peewee/models.html#"

db = MySQLDatabase('library', user='root', password='toor', host='localhost', port=3306)


class Books(Model):
    title = CharField(unique=True)
    description= TextField(null=True)
    category = ForeignKeyField(Category, backref='category', null=True)
    code = CharField(null=True)
    barcode = CharField()
    #parts*
    part_order = IntegerField(null=True )
    price = DecimalField(null=True)
    publisher = ForeignKeyField(Publisher, backref='publisher', null=True)
    author = ForeignKeyField(Author, backref='author', null=True)
    image = CharField(null=True)
    status = CharField() #choices
    date = DateTimeField()
    

class Clients(Model):
    name = CharField()
    mail = CharField(null=True, unique=True)
    phone = CharField(null=True)
    date= DateTimeField()
    national_id = IntegerField(null=True, unique=True)
    
    

class Employee(Model):
    name = CharField()
    mail = CharField(null=True, unique=True)
    phone = CharField(null=True)
    date= DateTimeField()
    national_id = IntegerField(null=True, unique=True)
    #permisssions = IntegerField()
    Priority = IntegerField(null=True)
    
    

class Category(Model):
    category_name = CharField(unique=True)
    #parent_category =  Recursive  relationship
    

class Branch(Model):
    name = CharField()
    code = CharField(null=True,unique=True)
    location = CharField(null=True)
    
    

class Daily_Movements(Model):
    book = ForeignKeyField(Books, backref='daily_book')
    client = ForeignKeyField(Clients, backref='')
    type = CharField()   #[rent - retrieve]
    date = DateTimeField()
    branch = ForeignKeyField(Branch, backref='Daily_branch',null=True)
    Book_from = DateField(null=True)
    Book_to  = DateField(null=True)
    employee = ForeignKeyField(Employee, backref='Daily_employee',null=True)
    
    
    

class History(Model):
    employee = ForeignKeyField(Employee, backref='History_employee')
    action = CharField() #Choices
    table = CharField() #choices
    date = DateTimerField()
    branch = ForeignKeyField(Branch, backref='history_branch')
    
    
class Publisher(Model):
    name = CharField(unique=True)
    Location = CharField(null=True)
    

class Author(Model):
    name = CharField(unique=True)
    Location = CharField(null=True)
    


db.connect()
db.create_tables([Books, Clients, Employee, Category, Branch, Daily_Movements, History, Publisher, Author )
