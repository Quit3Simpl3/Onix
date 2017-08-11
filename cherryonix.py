import cherrypy
from onix import Onix

class Cherrix(object):
    @cherrypy.expose
    def index(self, length, plaintext, options, banned):
        if length == '':
            length = 8

        onix = Onix(length=length, plaintext=plaintext, options=options, banned=banned)
        return onix.onix()


if __name__ == "__main__":
    cherrypy.quickstart(Cherrix())