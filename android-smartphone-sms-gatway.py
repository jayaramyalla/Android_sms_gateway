from bottle import get, post, request, template, run, route #pip install bottle
import sl4a #pip install sl4a
@get('/login')
def login():
    return '''
    <form action="/login" method="post">
    <h1>Custom SMS portal using your android smartphone </h1></br></br></br>
    Mobile : <input name="mobile_number" type="text" /></br></br></br></br>
    Message: <textarea rows="4" cols="50" name="message" /></textarea></br></br>
    <input value="Send" type="submit" />
    </form>
    '''
@post('/login')
def do_login():
    mobile = request.forms.get('mobile_number')
    message = request.forms.get('message')
    droid = sl4a.Android()
    droid.smsSend(mobile,message)
    return template("<p>{{mobile}}</br>{{message}}</br>sent...!</p>",mobile=mobile,message=message)

@route('/api/<mobile>/<message>')
def api(mobile, message):
    #API http://IPADDRESS/mobilenumer/message
    droid = sl4a.Android()
    droid.smsSend(mobile,message)
    return template("<p>{{mobile}}</br>{{message}}</br>sent...!</p>",mobile=mobile,message=message)

run(host='0.0.0.0', port=8080, debug=True)

#coded by jayaram yalla
#https://www.linkedin.com/in/jayaramyalla
#https://twitter.com/jayaramyalla
