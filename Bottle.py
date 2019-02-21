from bottle import run, route, view, get, post, request
from itertools import count
#LOGS
#Ver-1.1 --- Added tickets list
#Ver-1.2 --- Adding server functionality

#Ver-1.4 --- Added check in page


class Ticket:
    _ids = count (0)
    
    def __init__(self,name,email,date_of_birth, check_in):
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.check_in = date_of_birth
    

tickets = [
    Ticket("Moses", "moses@gmail.com", "16/11/2001", False),
    Ticket("Jerry", "moses@gmail.com", "16/11/2001", False),
    Ticket("Tom", "moses@gmail.com", "16/11/2001", False)
]


#Pages

#Index page
@route('/')
@view('index')
def index():
    pass

#Check in page
@route('/check-in')
@view('check-in')
def check_in():
    data = dict(ticket_list = tickets)
    return data

run(host='0.0.0.0', port = 8080, reloader = True, debug = True)
