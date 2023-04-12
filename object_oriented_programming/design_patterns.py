"""

Object-oriented programming is a paradigm based on the concept of
wrapping pieces of data, and behaviour related to that data, into
special bundles called objects, which are constructed from a set 
of blueprints defined by a programmer called classes


Class: Blueprint from which individual objects are created
Object: Instance of a class

Four pillar of OOPS


1. Encapsulation
        Encapsulation is the ability of an object to hide parts of
        its state and behavious from other objects, exposing only a
        limited interface to the rest of the program
        To encapsulate something means to make it private, and thus
        accesible only from within of the methods of its own class
        There's a little bit less restrictive mode called protected
        that makes a member of a class available to subclasses as well
        
        Interfaces and abstract classes/methods of most programming 
        languages are based on the concepts of abstraction and encapsulation
        In modern object-oriented programming languages, the interface 
        mechanism (usually declared with the interface or protocol keyword)
        lets you define contracts of the interaction between objects. That's
        one of the reason why the interface only care about behaviours of
        objects, and why you can't declare a field in an interface
        
        Encapsulation is defined as the wrapping up of data under a single unit.
        It is the mechanism that binds together code and the data it manipulates. 
        Another way to think about encapsulation is, that it is a protective shield 
        that prevents the data from being accessed by the code outside this shield. 
        Technically in encapsulation, the variables or data of a class is hidden from 
        any other class and can be accessed only through any member function of its own 
        class in which they are declared. As in encapsulation, the data in a class is 
        hidden from other classes, so it is also known as data-hiding. Encapsulation 
        can be achieved by Declaring all the variables in the class as private and writing 
        public methods in the class to set and get the values of variables. 
        
    
        Encapsulation: Information hiding
        Example: hiding data using getter and setter method.

2. Abstraction
        Represent the essential features without including implementation details.
        
        Abstraction: Implementation hiding
        Example: hiding implementation using abstract class and interfaces
        
2. Polymorphism
        Polymorphism is the ability of a program to detect the real class of
        an object and call its implementation even when its real type is unknown
        in the current context
        

4. Inheritance
        Inheritance is the ability to build new classes on top of existing ones
        The main benefit of inheritance is code resuse.


Relations Between Objects

In addtion to inheritance and implementation, there are other types of relations between
objects.

Association is a type of relationship in which one object uses or interacts with another.

1. Dependency

Dependency is a weaker variant of association that usually implies that there's no permanent
link between objects. Dependency typically (but not always) implies that an object accepts
another object as a method parameter, instantiates, or uses another object. Here's how you can
spot a dependency between classes: a dependecy exists between two classes if change to defintion
of one class result in modifications in another class

2. Aggregation

3. Composition

4. Association



Design principles

Encapsulate what varies: 
  Encapsulation on method level: seperate method implementation for code that may require change in future. E.g Tax calculation logic in an invoicing system
  Encapsulation on class level: when implentation in a separate method becomes large and complex, its better to put it into a seperate class implementation
  
Program to interface not implementation:
  An abtraction based implementation is better than focus on concrete implentation
  With focus on abstract methods and behaviour more use cases can solved than concrete implementation
  
Favour compostion over inheritance


Solid Principles

[S]ingle Responsibility Principle: A class should have just one reason to change

[O]open Closed Principle: Classes should be open for extension but closed for modification

[L]iskovs Substitution Principle: When extending a class you should be able to pass object of 
                                  the subclass in place of object of the parent class without
                                  breaking the client code
    Parameter types in a method of a subclass should match or be more abstract than parameter
    types in the method of the superclass
    
    Similiarly, the return type in a method of a subclass should match or be a subtype of the 
    return type in the method of the superclass

[I]interface Segregation Principle: Clients shouldn't be forced to depend on methods they do not use

[D]ependency Inversion Principle: High level classes shouldn't depend on low-level classes.
                                  Both should depend on abstraction. Abstraction should not depend on details.
                                  Details should depend on abstraction.
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
                                  
Creational Design Patterns:
1. Factory Method
2. Abstract Factory
3. Builder
4. Prototype
5. Singleton

Structural Design Patterns:
1. Adapter
2. Bridge
3. Composite
4. Decorator
5. Facade
6. Flyweight
7. Proxy

Behavioural Design Patterns
1. Chain of responsibility
2. Command
3. Iterator
4. Mediator
5. Memento
6. Observer
7. State
8. Strategy
9. Template Mehthod
10. Visitor
                                  
Important Design Patterns

Factory/Factory Method [read, coded]
Abstract Factory [read, coded]
Singleton [read, coded]
Observer [read, ]

Builder [read, coded]
Decorator [read, coded]
Adapter [read, coded]
Strategy [read, coded]
State [read, coded]
Fascade [read]













"""










"""
  Factory Method Pattern
  
  
                 Car
            Hatchback SUV Sedan
  
  
"""


class Car:
    def __init__(self, **kwarg):
        self.manufacturer = kwarg.get('manufacturer')
        self.cylinder_count = kwarg.get('cylinder_count')
        self.chasis_no = kwarg.get('chasis_no')
        self.year = kwarg.get('year')
        self.model_name = kwarg.get('model_name')
        self.color = kwarg.get('color')
        
class Hatchback(Car):
    def __init__(self, **kwarg):
        print('concrete hatchback car created')
        super().__init__(**kwarg)
        
class SUV(Car):
    def __init__(self, **kwarg):
        print('concrete suv car created')
        super().__init__(**kwarg)
        
class Sedan(Car):
    def __init__(self, **kwarg):
        print('concrete sedan car created')
        super().__init__(**kwarg)
   
"""
Without Factory Pattern
"""

car_details = {
    "manufacturer": "0Hyundai",
    "cylinder_count": 3,
    "chasis_no": "M1948SFCCAQ",
    "year": 2015,
    "model_name": "Eon",
    "color": "Red"
}


# Client Code {

car_type = 'hatchback'

car = None

if car_type == 'hatchback':
    car = Hatchback(**car_details)
elif car_type == 'suv':
    car = SUV(**car_details)
elif car_type == 'sedan':
    car = Sedan(**car_details)
     
print(car.manufacturer)

"""
In this approach we are heavily dependent on concrete implementation.
We will have to make changes in client code whenever there is a change
library code. It violates 'open for extension closed for modification'
principle, as we have to make change in the client code whenever there
is a change in library code


Better approch: encapsulate what varies

We can seperate the logic of object creation in a seperate class and method
This approach is also called Factory Pattern.

Factory class is using Single responsiblity principle because it is now only 
responsible for object creation

Flaw: This class is open for modification, if old products are removed or new product needs to added

"""
# }


class CarFactory:
    def getVehicle(self, car_type, **kwarg):
        if car_type == 'hatchback':
            return Hatchback(**kwarg)
        elif car_type == 'suv':
            return SUV(**kwarg)
        elif car_type == 'sedan':
            return Sedan(**kwarg)


factory = CarFactory()
car = factory.getVehicle('suv', **car_details)
print(car.manufacturer)

# https://www.youtube.com/playlist?list=PLlsmxlJgn1HJpa28yHzkBmUY-Ty71ZUGc
"""

Factory Method Pattern: The Factory Method Pattern defines an interface for creating an object, but lets subclasses
decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses

Factory method pattern loosens the coupling of a given code by seperating the
product's construction code from the code that uses this product

"""

class CarFactory:
    def orderCar(self):
        pass

class MarutiCarFactory(CarFactory):
    def orderCar(self, car_type, **kwarg):
        print("Ordered from Maruti Factory")
        if car_type == 'hatchback':
            return Hatchback(**kwarg)
        elif car_type == 'suv':
            return SUV(**kwarg)
        elif car_type == 'sedan':
            return Sedan(**kwarg)
        

class TataCarFactory(CarFactory):
    def orderCar(self, car_type, **kwarg):
        print("Ordered from Tata Factory")
        
        if car_type == 'hatchback':
            return Hatchback(**kwarg)
        elif car_type == 'suv':
            return SUV(**kwarg)
        elif car_type == 'sedan':
            return Sedan(**kwarg)

factory = MarutiCarFactory()
vehicle = factory.orderCar("sedan", **car_details)


"""
  Abstract Factory Pattern
  
"""


class CarFactory:
    def orderHatchbackCar(self):
        pass
    
    def orderSUVcar(self):
        pass
    
    def orderSedancar(self):
        pass
    

class Maruti(CarFactory):
    def orderHatchbackCar(self, **kwarg):
        print("Hatchback requested from maruti factory")
        return Hatchback(**kwarg)
    
    def orderSUVcar(self, **kwarg):
        print("SUV requested from maruti factory")
        return SUV(**kwarg)
    
    def orderSedancar(self, **kwarg):
        print("Sedan requested from maruti factory")
        return Sedan(**kwarg)


class Tata(CarFactory):
    def orderHatchbackCar(self, **kwarg):
        print("Hatchback requested from tata factory")
        return Hatchback(**kwarg)
    
    def orderSUVcar(self, **kwarg):
        print("SUV requested from tata factory")
        return SUV(**kwarg)
    
    def orderSedancar(self, **kwarg):
        print("Sedan requested from tata factory")
        return Sedan(**kwarg)


factory = Tata()
vehicle = factory.orderSedancar(**car_details)



"""
Builder Pattern
"""

class Car:
    def __init__(self, **kwarg):
        self.manufacturer = kwarg.get('manufacturer')
        self.cylinder_count = kwarg.get('cylinder_count')
        self.chasis_no = kwarg.get('chasis_no')
        self.year = kwarg.get('year')
        self.model_name = kwarg.get('model_name')
        self.color = kwarg.get('color')

    class Builder:
        
        def manufacturer(self,manufacturer):
            self.manufacturer = manufacturer
            return self
            
        def cylinder_count(self,cylinder_count):
            self.cylinder_count = cylinder_count
            return self
        
        def chasis_no(self,chasis_no):
            self.chasis_no = chasis_no
            return self
        
        def year(self,year):
            self.year = year
            return self
        
        def model_name(self,model_name):
            self.model_name = model_name
            return self
        
        def color(self,color):
            self.color = color
            return self
            
        def build(self):
            car_details = {
                "manufacturer": self.manufacturer,
                "cylinder_count": self.cylinder_count,
                "chasis_no": self.chasis_no,
                "year": self.year,
                "model_name": self.model_name,
                "color": self.color
            }
            
            return Car(**car_details)
            



car = Car.Builder().manufacturer('Tata').cylinder_count(4).chasis_no('ME34AS1').year(2015).model_name('Tiago').color('Grey').build()
print('car created using builder ', car.model_name)


class Directive:
    def buildTiago(self, builder):
        return builder.manufacturer('Tata').cylinder_count(4).chasis_no('ME34AS1').year(2015).model_name('Tiago').color('Grey').build()
        
    def buildNexon(self, builder):
        return builder.manufacturer('Tata').cylinder_count(5).chasis_no('E7PQ2B').year(2022).model_name('Nexon').color('Red').build()

builder = Car.Builder()
directive = Directive()

nexon = directive.buildNexon(builder)
print('car created using directive ', nexon.model_name)



"""
Prototype Pattern
"""

class Prototype:
    def clone(self):
        pass

class Car(Prototype):
    def __init__(self, **kwarg):
        self.manufacturer = kwarg.get('manufacturer')
        self.cylinder_count = kwarg.get('cylinder_count')
        self.chasis_no = kwarg.get('chasis_no')
        self.year = kwarg.get('year')
        self.model_name = kwarg.get('model_name')
        self.color = kwarg.get('color')
        
    def clone(self):
        car_details = {
                "manufacturer": self.manufacturer,
                "cylinder_count": self.cylinder_count,
                "chasis_no": self.chasis_no,
                "year": self.year,
                "model_name": self.model_name,
                "color": self.color
        }
        return Car(**car_details)

class Hatchback(Car):
    def __init__(self,**kwarg):
        super().__init__(**kwarg)
        
    
    def clone(self):
        car_details = {
                "manufacturer": self.manufacturer,
                "cylinder_count": self.cylinder_count,
                "chasis_no": self.chasis_no,
                "year": self.year,
                "model_name": self.model_name,
                "color": self.color
        }
        return Car(**car_details)
        

tiago1 = Hatchback(**car_details)
print("tiago1: ", tiago1.color)

tiago1.color = 'grey'

tiago2 = tiago1.clone()
print("tiago2: ", tiago1.color)

class VehicleRegistry:
    def getVehicle(self, name):
        registry = {}
        
        car_details['model_name'] = 'alto'
        registry['alto'] = Car(**car_details)
        
        car_details['model_name'] = 'swift'
        registry['swift'] = Car(**car_details)
        
        car_details['model_name'] = 'wagnor'
        registry['wagnor'] = Car(**car_details)
        
        car_details['model_name'] = 'breeza'
        registry['breeza'] = Car(**car_details)
        
        return registry.get(name).clone()
        
        

vehicle1 = VehicleRegistry().getVehicle('breeza')

print(vehicle1.model_name)




"""
Singleton Pattern

https://www.educative.io/answers/how-to-create-a-singleton-class-in-python
https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
"""
class SingletonClass:
  _instance = None
 
  def __init__(self):
      self.host = "google.com"
 
  def __new__(cls):
    if cls._instance is None:
      print('Creating the object')
      cls._instance = super(SingletonClass, cls).__new__(cls)
    return cls._instance

obj1 = SingletonClass()
print(obj1.host, obj1)

obj2 = SingletonClass()
print(obj2.host, obj2)





"""
Adapter Pattern
"""


class XML:
    def __init__(self, data):
        self.data = data
        
    def getData(self):
        return self.data
        

class JSON:
    def __init__(self, data):
        self.data = data
        
    def getData(self):
        return self.data




class DataAnalyticsTool:
    """ Adaptee """
    
    def analyze(self, data):
        print("Data found (JSON): ", data)
    

class Adapter(DataAnalyticsTool):
    """ Adapter """
    def __init__(self, XML):
        self.XML = XML
    
    
    def analyze(self):
        print("Adapter input (XML): ", self.XML.getData())
        json = self.convertXMLtoJSON(self.XML.getData())
        print("Adapter output (JSON): ", json.getData())
        super().analyze(json.getData())
    
    def convertXMLtoJSON(self, xml):
        json = JSON('{"type":"json"}')
        return json
    


    
""" Client """
xml = XML("<xml></xml>")
# tool = DataAnalyticsTool(xml)
# tool.analyze()

adapter = Adapter(xml)
adapter.analyze()



"""
Decorator Pattern
"""

class CommonInterface:
    def sendMsg(self, msg):
        pass

class Notifier(CommonInterface):
    def sendMsg(self, msg):
        print("Send msg using notifier: ", msg)
        
class BaseDecorator(CommonInterface):
    def __init__(self, decorator):
        self.decorator = decorator
        
    def sendMsg(self, msg):
        self.decorator.sendMsg(msg)

class WhatsappNotifierDecorator(BaseDecorator):
    def __init__(self, decorator):
        super().__init__(decorator)
        
    def sendMsg(self, msg):
        super().sendMsg(msg)
        print("Send msg using whatsapp notifier: ", msg)

class FacebookNotifierDecorator(BaseDecorator):
    def __init__(self, decorator):
        super().__init__(decorator)
    
    def sendMsg(self, msg):
        super().sendMsg(msg)
        print("Send msg using notifier: ", msg)

notifier = WhatsappNotifierDecorator(BaseDecorator(Notifier()))
notifier.sendMsg("hello")



class ComponentInterface:
    def sendMsg(self):
        pass

class ConcreteComponent(ComponentInterface):
    def charges(self):
        return 500
        
class BaseDecorator(ComponentInterface):
    def __init__(self, wrappee):
        self.wrappee = wrappee
        
    def charges(self):
        return self.wrappee.charges()

class ConcreteDecorator1(BaseDecorator):
    def __init__(self, wrappee):
        super().__init__(wrappee)
        
    def charges(self):
        return super().charges() + 100
        
class ConcreteDecorator2(BaseDecorator):
    def __init__(self, wrappee):
        super().__init__(wrappee)
    
    def charges(self):
        return super().charges() + 200

# notifier = WhatsappNotifierDecorator(BaseDecorator(Service()))

s = ConcreteDecorator2(ConcreteDecorator1(ConcreteDecorator1(ConcreteComponent())))
print(s.charges())






""" 
Strategy Pattern

"""


# Interface
class PaymentStrategy:
    def pay(self):
        pass
    
    def getTransactionStatus(self):
        pass
    

class PayPal(PaymentStrategy):
    def pay(self, amt):
        print("Paid "+amt+ " using PayPal")
    
    def getTransactionStatus(self):
        pass



class DebitCard(PaymentStrategy):
    def pay(self, amt):
        print("Paid "+amt+ " using DebitCard")
        
    
    def getTransactionStatus(self):
        pass


class PaymentService:
    def setPaymentMode(self, strategy):
        self.strategy = strategy
    
    
    def processPayment(self, amt):
        self.strategy.pay(amt)
    


service = PaymentService()
service.setPaymentMode(PayPal())
service.processPayment('200')




"""
State Pattern

"""

class AudioPlayer:
    
    def __init__(self):
        self.state = StopState(self)
        
    def setState(self, state):
        self.state = state
        
    def playSong(self):
        self.state.play()
    
    def pauseSong(self):
        self.state.pause()
    
    def stopSong(self):
        self.state.stop()
    

# Abstract Class    
class State:
    def play(self):
        pass
    
    def pause(self):
        pass
    
    def stop(self):
        pass

    
class PlayingState(State):
    
    def __init__(self, player):
        self.player = player
        
    def play(self):
        print("Already playing song")

    def pause(self):
        self.player.setState(PausedState(self.player))
        
    def stop(self):
        self.player.setState(StopState(self.player))

class PausedState(State):
    
    def __init__(self, player):
        self.player = player
    
    def play(self):
        print("Set song to PlayingState")
        self.player.setState(PlayingState(self.player))

    def pause(self):
        print("Already paused song")

    def stop(self):
        print("Set song to StopState")
        self.player.setState(StopState(self.player))

class StopState(State):
    
    def __init__(self, player):
        self.player = player
    
    def play(self):
        print("Set song to PlayingState")
        self.player.setState(PlayingState(self.player))

    def pause(self):
        print("Set song to PausedState")
        self.player.setState(PausedState(self.player))

    def stop(self):
        print("Already stopeed song")
        



player = AudioPlayer()
player.pauseSong()
player.stopSong()
player.stopSong()




"""
Observer Design Pattern
"""

# Suscriber
class Notification:
    def send(self):
        pass

# Concrete Suscriber Service 1
class EmailNotificationSender(Notification):
    def __init__(self, email_id):
        self.email_id = email_id
    def send(self, msg):
        print(f"email.send({self.email_id},{msg})")

# Concrete Suscriber Service 2
class SMSNotificationSender(Notification):
    def __init__(self, phone_no):
        self.phone_no = phone_no
    def send(self, msg):
        print(f"sms.send({self.phone_no},{msg})")


# Publisher
class NotificationService:
    def __init__(self):
        self.subscribers = {}
    
    def subscribe(self, event_name, notification_listener):
        print('Subscribers: ', self.subscribers)
        print(event_name in self.subscribers, notification_listener)
        
        if (event_name in self.subscribers) == False:
            self.subscribers[event_name] = [notification_listener]
            print(self.subscribers)
        else:
            self.subscribers[event_name].append(notification_listener)
            
    def notify(self, event_name, msg):
        for listner in self.subscribers[event_name]:
            listner.send(msg)
    
    

notification_service = NotificationService()

notification_service.subscribe('Promotions', EmailNotificationSender("nikhil@gmail.com"))
notification_service.subscribe('Promotions', EmailNotificationSender("naveen@gmail.com"))
notification_service.subscribe('Promotions', EmailNotificationSender("umang@gmail.com"))


notification_service.subscribe('Message', SMSNotificationSender("8594339292"))
notification_service.subscribe('Message', SMSNotificationSender("9374727378"))
notification_service.subscribe('Message', SMSNotificationSender("9086589042"))


notification_service.notify('Promotions', 'Samsung S14 Released')
notification_service.notify('Message', 'Your laptop is repaired')








