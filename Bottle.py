#LOGS
#Ver-1.1 --- Added tickets list
#Ver-1.2 --- Adding server functionality


class Ticket:
    _int = count = (0)
    
    def __inti__(self,name,email,date_of_birth, check_in):
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.check_in = date_of_birth
    

TICKETS = [
    Ticket("Moses", "moses@gmail.com", "16/11/2001", False),
    Ticket("Jerry", "moses@gmail.com", "16/11/2001", False),
    Ticket("Tom", "moses@gmail.com", "16/11/2001", False)
]


#Pages

#Index page
@route("/")
@view("index")
def index():
    pass

run(host='0.0.0.0', port = 8080, reloader = True, debug = True)
