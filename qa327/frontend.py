from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
import datetime
import re
import datetime

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""
# REGISTER METHODS

@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')

@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None
    
    if password != password2:
        error_message = "The passwords do not match"

    elif not is_valid_email(email):
        error_message = "Email format error"

    elif not is_valid_password(password):
        error_message = "Password not strong enough"
    elif not is_valid_user(name):
        error_message = "Username not allowed"
    else:
        user = bn.get_user(email)
        if user:
            error_message = "User Already exists"
        
        #*********Getting error message showing up even thou it shouldnt**************************
        elif not bn.register_user(email, name, password, password2):
            error_message = ""
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


# LOGIN METHODS

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


def check_empty_fields(field):
   
    #Raises error message and renders login html page if field is empty
    #:param field: the field in question
    
    if not field:
        return render_template('login.html',
        message='Field is required')


def is_valid_user(name):
    #Returns the boolean for valid 
    #:param user: the user in question
    INVALID_USER = (len(name) < 2 or len(name) >20) or re.match(r".*[*^+&@!#$%]", name) or name.startswith(' ')
    return False if INVALID_USER else True


def is_valid_email(email):
    
    #Returns the boolean for valid email
    #:param email: the email in question
    
    INVALID_EMAIL = (len(email) < 1 or \
        not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email))
    return False if INVALID_EMAIL else True


def is_valid_password(password):
   
    #Validate the password complexity 
    #min length 6, min one upper case, min one lower case, min one special char
    #:param password: the password in question
  
    upper = lower = special = False

    for char in password:
        if not upper and char.isalnum() and char.isupper():
            upper = True
        elif not lower and char.isalnum() and char.islower():
            lower = True
        elif not special and not char.isalnum():
            special = True
        else:
            continue

    if len(password) < 6 or not upper or \
            not lower or not special:
        return False
    return True


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Re render login page with error message 
    # if pwd field is empty or wrong format
    check_empty_fields(field=password)

    user = bn.login_user(email, password)

    if not is_valid_email(email):
        return render_template('login.html', message='Email format error')
    elif not is_valid_password(password):
        return render_template('login.html', message='Invalid password')
    #elif not is_valid_user(name):
       # return render_template('login.html', message='Invalid UserName')
    elif user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.
        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.
        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='login failed')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')



# PROFILE METHODS

def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object
    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.
    To wrap a function, we can put a decoration on that function.
    Example:
    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
                
        return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner

#user profile page
@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)

    
#assesses whether or not the ticket name is valid    
def is_valid_ticket_name(name):
    #check if ticket name has non-alphanumeric characters, starts with a space, ends with a space, is longer than 60 characters
    invalid_ticket_name = re.match(r".*[*^+&@!#$%]", name) or name.startswith(' ') or name.endswith(' ') or (len(name) > 60)
    return False if invalid_ticket_name else True
    
#assesses whether or not the ticket quantity is within the acceptable range
def is_valid_ticket_quanitity(quantity):
    #check if ticket quantity falls in accceptable quantity range
    invalid_ticket_quantity = (int(quantity) < 1) or (int(quantity) > 101)
    return False if invalid_ticket_quantity else True
    
#assesses whether or not the ticket price is valid    
def is_valid_ticket_price(price):
    #check if ticket price falls in accceptable price range
    invalid_ticket_price = (int(price) < 10) or (int(price) > 100)
    return False if invalid_ticket_price else True
    
#assesses whether or not the ticket date matches the proper format
def is_valid_ticket_date(date):
    return True if date > datetime.datetime.now() else False
    
#updating existing ticket using update form on user profile page    
@app.route('/', methods=['POST'])
#@authenticate
def update_post():
    #extract contents of the update form
    name = request.form.get('update_name')
    price = request.form.get('update_price')
    quantity = request.form.get('update_quantity')
    date = request.form.get('update_date')
    
    #initialize error message to be empty
    error_message = None
    
    #check that the given ticket name exists in the database
    ticket = bn.get_ticket(name=name)
    if not ticket:
        error_message = 'no such ticket exists'
        
    #check that the ticket name is alphanumeric only, space allowed only if not first or last character, and contains less than 60 chars
    if is_valid_ticket_name(str(name)) == False:
        error_message = 'invalid ticket name'
        
    #check ticket quantity is greater than 0 and less or equal to 100
    if is_valid_ticket_quantity(quantity) == False:
        error_message = 'invalid ticket quantity'
       
    #check ticket price is in the range 10 to 100 (including 10 and 100)
    if is_valid_ticket_price(price) == False:
        error_message = 'invalid ticket price'
        
    #check that date format is YYYYMMDD
    if is_valid_ticket_date(date) == False:
        error_message = 'invalid ticket date'
        
    #save ticket to database
    ticket = bn.store_ticket(name=name, price=price, quantity=quantity, date=date)
    
    #if theres an error message, output that message. Otherwise, post and redirect to user profile page
    if error_message:
        return render_template('index.html', update_message=error_message, user=user)
    else:
        return redirect('/')
    
    #The added new ticket information will be posted on the user profile page
@app.route('/sell', methods=['POST'])
def sellticket():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    date = request.form['date']
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    user_email = request.form['user']
    user = bn.get_user(user_email)

    #initialize error message to be empty
    message = None


#Tests for R4 SELL

    # check name
    ticket = bn.get_ticket(name=name)
    if not ticket:
        message = 'no such ticket exists'
    #check that the ticket name is alphanumeric only, space allowed only if not first or last character, and contains less than 60 chars
    if is_valid_ticket_name(str(name)) == False:
        message = 'invalid ticket name'
    # check quantity
    if not is_valid_ticket_quanitity(quantity):
        message = "Ticket quantity must be between 0 and 100."
    # check price
    if not is_valid_ticket_price(price):
        message = "Ticket price is invalid."
    # check date
    if not is_valid_ticket_date(date):
        message = "Ticket date is invalid."

    if not message: # if message is empty, indicating no validation errors
        message = "Ticket created successfully."
        bn.sell_ticket(name, quantity, price, date, user.id)

    # redirect user to profile page with result message
    
    return redirect("/?message={}".format(message))
    


#buying a ticket using buy form on user profile page
@app.route('/', methods=['POST'])
def buy_post():
    #extract contents of buy form
    name = request.form.get('buy_name')
    quantity = request.form.get('buy_quantity')
    
    #initialize error message to be empty
    error_message = None


# 404 METHODS

#Added 404 Error Handler
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')



