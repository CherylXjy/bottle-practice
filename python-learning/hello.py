from bottle import route, run

@route("/hello/:name")
def hello_name(name='World'):
    return '<h1>Hello %s!</h1>' % name

run(host='localhost',port=8080)
