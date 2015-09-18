i mport cgi
from wsgiref.simple_server import make_server
from wsgiref import util

import database

# Templates
HTML_WRAP = open('main.html').read()
POST = open('post.html').read()

## Request handler for main page
def View(env, resp):
    '''View is the 'main page' of the forum.

    It displays the submission form and the previously posted messages.
    '''
    # get posts from database
    posts = database.GetAllPosts()
    # send results
    headers = [('Content-type', 'text/html')]
    resp('200 OK', headers)
    return [HTML_WRAP % ''.join(POST % p for p in posts)]

## Request handler for posting - inserts to database
def Post(env, resp):
    '''Post handles a submission of the forum's form.
  
    The message the user posted is saved in the database, then it sends a 302
    Redirect back to the main page so the user can see their new post.
    '''
    # Get post content
    input = env['wsgi.input']
    length = int(env.get('CONTENT_LENGTH', 0))
    # If length is zero, post is empty - don't save it.
    if length > 0:
        postdata = input.read(length)
        fields = cgi.parse_qs(postdata)
        content = fields['content'][0]
        # If the post is just whitespace, don't save it.
        content = content.strip()
        if content:
            # Save it in the database
            database.AddPost(content)
    # 302 redirect back to the main page
    headers = [('Location', '/'),
               ('Content-type', 'text/plain')]
    resp('302 REDIRECT', headers) 
    return ['Redirecting']

## Dispatch table - maps URL prefixes to request handlers
DISPATCH = {'': View,
            'post': Post,
    }

## Dispatcher forwards requests according to the DISPATCH table.
def Dispatcher(env, resp):
    '''Send requests to handlers based on the first path component.'''
    page = util.shift_path_info(env)
    if page in DISPATCH:
        return DISPATCH[page](env, resp)
    else:
        status = '404 Not Found'
        headers = [('Content-type', 'text/plain')]
        resp(status, headers)    
        return ['Not Found: ' + page]

httpd = make_server('', 8000, Dispatcher)
print "Serving HTTP on port 8000..."
httpd.serve_forever()

