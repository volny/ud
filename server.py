from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db') # create the SQLA output file 
Base.metadata.bind = engine # bind the engine to the Base class. connect class defs to tables
DBSession = sessionmaker(bind=engine) # link btw code execution and engine (?)
session = DBSession()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                results = session.query(Restaurant).all()

                output = "<h1>Restaurants</h1>"
                output += "<h2>All the restaurants in the DB:</h2>"
                for r in results:
                    if r.zipcode:
                        output += "<b> ZIP " + r.zipcode + "</b>: "
                    else:
                        output += "<b>Unknown location</b>: "
                    output += r.name + " "
                    output += '(<a href="/restaurant/' + str(r.id) + '/edit">edit</a>'
                    output += " / "
                    output += '(<a href="/restaurant/' + str(r.id) + '/delete">delete</a>)'
                    output += "<br>"
                output += '<br><a href="/restaurants/new"><button>Create a new restaurant here</button></a>'

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = "<h1>Create a new restaurant</h1>"
                output +=  """<form method='POST' enctype='multipart/form-data' action='/restaurants/new'>
                            Restaurant Name
                            <input name='restaurant' type='text' >
                            <input type='submit' value='Submit'>
                            </form>"""


            if self.path.endswith("/edit"):

                # what an ugly hack. for the love of god, use re
                # https://docs.python.org/2/library/re.html
                # then: https://docs.djangoproject.com/en/1.7/topics/http/urls/
                r_id = self.path.split("/")[2]
                r = session.query(Restaurant).filter_by(id=r_id).one()

                if r != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()


                    output = '<h1> Edit "%s" </h1>' % r.name
                    output += 'New name for restaurant "%s": ' % r.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/edit'>" % r_id
                    output += '<input name="r_rename" type="text" placeholder="%s">' % r.name
                    output += '<input type="submit" value="Rename">'
                    output += "</form>"

            if self.path.endswith("/delete"):

                # what an ugly hack. for the love of god, use re
                # https://docs.python.org/2/library/re.html
                # then: https://docs.djangoproject.com/en/1.7/topics/http/urls/
                r_id = self.path.split("/")[2]
                r = session.query(Restaurant).filter_by(id=r_id).one()

                if r != []:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()


                    output = '<h1> Are you sure you want to delete "%s" ?</h1>' % r.name
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurant/%s/delete'>" % r_id
                    output += "<input type='submit' value='Confirm deletion'>"
                    output += "</form> " 

                    #session.delete(r)

            self.wfile.write(output) # wfile: send a message back to the client
            print output
            return

        except IOError:
            self.send_error(404, "404 Not found. File: %s" % self.path)

    def do_POST(self):
        try:
            # --- helpers ---

            # cgi looks at the header and stores content-type in a dict
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data': # have we received form data?
                fields = cgi.parse_multipart(self.rfile, pdict) # collect the form input, store in dict

            # --- urls ---
            if self.path.endswith("/restaurants/new"):
                _input = fields.get('restaurant') # get the restaurant field out of the dict

                new_restaurant = Restaurant(name=_input[0])
                session.add(new_restaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            if self.path.endswith("/edit"):
                _input = fields.get('r_rename')

                # what an ugly hack. for the love of god, use re
                r_id = self.path.split("/")[2]
                r = session.query(Restaurant).filter_by(id=r_id).one()

                if r != []:
                    r.name = _input[0]
                    session.add(r)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            if self.path.endswith("/delete"):
                _input = fields.get('r_rename')

                # what an ugly hack. for the love of god, use re
                r_id = self.path.split("/")[2]
                r = session.query(Restaurant).filter_by(id=r_id).one()

                if r != []:
                    session.delete(r)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

            self.wfile.write(output) # wfile: send a message back to the client
            print output
        except:
            pass

def main():
    try:
        port = 8080
        server_address = ('', port)
        server = HTTPServer(server_address, Handler)
        print "Web server running on port %s" % port
        server.serve_forever()

    except KeyboardInterrupt: # user pressing ctrl-c
        print "  --> stopping the web server"
        server.socket.close()


if __name__ == '__main__':
    main()

