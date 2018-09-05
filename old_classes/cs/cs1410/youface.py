from bottle import get, post, run, request, response
from bottle import redirect, debug, static_file
import xmlrpclib
import template

DB_ADDRESS = 'http://youface.cs.dixie.edu/'
DB_SERVER = None

title = 'YouFace'
subtitle = "A billion dollars and it's yours!"
links = [
    { 'href': 'http://cit.cs.dixie.edu/cs/cs1410/',     'text': 'CS 1410' },
    { 'href': 'http://codrilla.cs.dixie.edu/',          'text': 'Codrilla' },
    { 'href': 'http://new.dixie.edu/reg/syllabus/',     'text': 'College calendar' },
]



@get('/youface.css')
def stylesheet():
    return static_file('youface.css', root='./')

@get('/loginscreen')
def loginscreen():
    f = open('login-page.template')
    s=''
    for line in f:
        s+=line

    t=template.Template(s)
    data = {'title':title,
            'subtitle':subtitle,
            'links':links,
            }
    return t.render(data)

@post('/login')
def login():
    name = request.forms.get('name')
    password = request.forms.get('password')
    button = request.forms.get('type')


    response.set_cookie('name', name, path='/')
    response.set_cookie('password', password, path='/')


    if button == "Create":
        (status, message) = DB_SERVER.newUser(name, password)
    elif button =="Delete":
        (status, message) = DB_SERVER.deleteUser(name, password)

    redirect('/')


@get('/')
def home():
    name = request.COOKIES.get('name', '')
    password = request.COOKIES.get('password', '')
    (status, lstofFriends) = DB_SERVER.listFriends(name, password)
    (status2, lstofUpdates) = DB_SERVER.listStatusFriends(name, password,25)
    if status == 'failure' or status2 =='failure':
        redirect('/loginscreen')

    f = open('feed-page.template','r')
    s=f.read()
    f.close()

    t=template.Template(s)
    data = {
        'title':title,
        'subtitle':subtitle,
        'links':links,
        'name':name,
        'updates':[{'status':s} for s in lstofUpdates],
        'friends':[{'name':name} for name in lstofFriends]
    }
    return t.render(data)

@get('/friend/:fname')
def friend(fname):
    name = request.COOKIES.get('name', '')
    password = request.COOKIES.get('password', '')
    (status, lstofFriends) = DB_SERVER.listFriends(name, password)
    (status2, lstofUpdates) = DB_SERVER.listStatusUser(name, password,fname,25)
    if status == 'failure' or status2 =='failure':
        redirect('/')
    else:
           f = open('friend-page.template','r')
    s=f.read()
    f.close()

    t=template.Template(s)
    data = {
        'title':title,
        'subtitle':subtitle,
        'links':links,
        'friend':fname,
        'updates':[{'status':s} for s in lstofUpdates],
        'friends':[{'name':name} for name in lstofFriends]
    }
    return t.render(data)
        
    

@post('/logout')
def logout():
    response.set_cookie('name', '', path='/')
    response.set_cookie('password', '', path='/')
    
    redirect('/')
    
@post('/status')
def status():
    name =request.COOKIES.get('name','')
    password = request.COOKIES.get('password', '')
    message = request.forms.get('status')
    DB_SERVER.setStatus(name,password,message)
    redirect('/')

@post('/addfriend')
def addFriend():
    name =request.COOKIES.get('name','')
    password = request.COOKIES.get('password', '')
    friend = request.forms.get('name')
    DB_SERVER.addFriend(name,password,friend)
    redirect('/')

@post('/unfriend')
def unFriend():
    name =request.COOKIES.get('name','')
    password = request.COOKIES.get('password', '')
    unfriend = request.forms.get('name')
    DB_SERVER.unFriend(name,password,unfriend)
    redirect('/')



def main():
    global DB_SERVER, DB_ADDRESS

    print 'Using YouFace server at', DB_ADDRESS
    DB_SERVER = xmlrpclib.ServerProxy(DB_ADDRESS, allow_none=True)
    debug(True)
    run(host='localhost', port=8080, reloader=True)

if __name__ == '__main__':
    main()
    #print loginscreen()
    

    
