from qa327.models import db, User, Ticket
import decimal
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user
    
def store_ticket(name, price, quantity, date):
    new_ticket = Ticket(name=name, price=price, quantity=quantity, date=date)
    
    db.session.add(new_ticket)
    db.session.commit()
    return None
  
def get_ticket(name):
    ticket = Ticket.query.filter_by(name=name).first()
    return ticket
    
def get_all_tickets():
    tickets = Ticket.query.all()
    return tickets

def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw)

    db.session.add(new_user)
    db.session.commit()
    return None

#Test to see updated ticket price
def update_ticekt(name, quantity, price, date, user):
    ticket = Ticket()
    ticket.name = name
    ticket.quantity = quantity
    ticket.price = price
    ticket.date = date
    ticket.user = user
    db.session.add(ticket)
    db.session.sell(ticket)
    db.session.commit()

#Tests for selling a ticket
def sell_ticket(name, quantity, price, date, user):
#Used to test the sell ticket function
    ticket = Ticket()
    ticket.name = name
    ticket.quantity = quantity
    ticket.price = price
    ticket.date = date
    ticket.user = user
    db.session.add(ticket)
    db.session.commit()

#Used to test buying ticket function
def buy_ticket(ticket_id, buyer_id):
    ticket = get_ticket(ticket_id)
    buyer = get_user(buyer_id)
    ticket.user = buyer.id
    buyer.balance -= ticket.price*decimal.Decimal("1.30")*decimal.Decimal("1.00")
    Ticket.query.filter_by(id=int(ticket_id)).delete()
    db.session.commit()