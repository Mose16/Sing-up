from bottle import run, route, view, get, post, request
from itertools import count
#LOGS
#Ver-1.1 --- Added tickets list
#Ver-1.2 --- Adding server functionality

#Ver-1.4 --- Added check in page


class Ticket:
    _ids = count (0)
    
    def __init__(self,name,photo,email,date_of_birth, check_in):
        self.id = next(self._ids)
        self.name = name
        self.photo = photo
        self.email = email
        self.date_of_birth = date_of_birth
        self.check_in = date_of_birth
    

tickets = [
    Ticket("Dom", "https://scontent-syd2-1.xx.fbcdn.net/v/t1.0-9/19429857_1835349050125327_4797561959109957190_n.jpg?_nc_cat=105&_nc_ht=scontent-syd2-1.xx&oh=ce567917dbb32cfe97ae1da90aa1d4f5&oe=5D251B8F", "dom@gmail.com", "16/11/2001", False),
    Ticket("Jerry", "https://scontent-syd2-1.xx.fbcdn.net/v/t1.0-9/26907201_581373668870805_4632463134542420547_n.jpg?_nc_cat=110&_nc_ht=scontent-syd2-1.xx&oh=c2abe234842c2ec35064bf6dfcfca84c&oe=5CE38DE6", "jerry@gmail.com", "16/11/2001", False),
    Ticket("Tom", "https://scontent-syd2-1.xx.fbcdn.net/v/t1.0-9/49730702_1123306764495777_5072699591707590656_n.jpg?_nc_cat=105&_nc_ht=scontent-syd2-1.xx&oh=319d236a78018313d0ab1d6322079bca&oe=5CE5107E", "tom@gmail.com", "16/11/2001", False),
    Ticket("Moses", "https://scontent-syd2-1.xx.fbcdn.net/v/t1.0-9/46429131_2325188731047157_6483553222676971520_n.jpg?_nc_cat=109&_nc_ht=scontent-syd2-1.xx&oh=8ba5ee8e8c15b5610fff200c1be7fc0e&oe=5D20F5A7", "moses@gmail.com", "16/11/2001", False)
]



#Pages

#Index page
@route('/')
@view('index')
def index():
    pass


#Change checked in status
@route('/check-in-success/<ticket_id>')
@view('check-in-success')
def check_in_success(ticket_id):
    ticket_id = int(ticket_id)
    found_ticket = None
    for ticket in tickets:
        if ticket.id == ticket_id:
            found_ticket = ticket
            break
    found_ticket.check_in = True
    data = dict(ticket = found_ticket)
    return data

#Sign-up
@route('/sign-up')
@view('sign-up')
def sign_up():
    pass

#Sign-up-success
@route('/sign-up-success', method="POST")
@view('sign-up-success')
def sign_up_success():
    pass



#Check in page
@route('/check-in')
@view('check-in')
def check_in():
    data = dict(ticket_list = tickets)
    return data

run(host='0.0.0.0', port = 8080, reloader = True, debug = True)
