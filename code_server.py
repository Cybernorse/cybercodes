from werkzeug.wrappers import Request, Response
from php_py_test import cla

@Request.application
def application(request):
    obj=cla()
    return Response(obj.func())

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("192.168.0.107", 8000, application)