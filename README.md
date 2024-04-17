# EX01 Developing a Simple Webserver
## Date: 14/02/2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title> simple webserver </title>
    </head>
    <body>
       <table border="2" cellspacing="12" cellpadding="12" height="25" width="50">
       <h1> TOP FIVE SOFTWARE COMPANIES </h1>
            <tr>
                <th>Rank</th>
                <th>Company</th>
                <th>Revenue(in billion USD)</th>
            </tr>
            <tr>
                <th>1</th>
                <th>Microsoft</th>
                <th>$143.0</th>
            </tr>
            <tr>
                <th>2</th>
                <th>Oracle</th>
                <th>$39.1</th>
            </tr>
            <tr>
                <th>3</th>
                <th>SAP</th>
                <th>$27.4</th>
            </tr>
            <tr>
                <th>4</th>
                <th>Salesforce</th>
                <th>$17.1</th>
            </tr>
            <tr>
                <th>5</th>
                <th>Adobe</th>
                <th>$12.9</th>
            </tr>
        </table>
    </body>
</html>           



"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()


```

## OUTPUT:
![op1](https://github.com/charu-dharshinii/simplewebserver/assets/130828943/a909c630-ecb3-4a8d-9f64-2860c45e0c79)

![op2](https://github.com/charu-dharshinii/simplewebserver/assets/130828943/c863c446-27cf-419d-bbb9-74ba1fd9819c)

## RESULT:
The program for implementing simple webserver is executed successfully.
