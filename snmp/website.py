from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rainbow Login Page</title>
    <style>
        /* Style the body */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
            font-family: Arial, sans-serif;
        }

        /* Style the form container */
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Style the input fields */
        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        /* Style the login button */
        .login-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #6a1b9a;
            border: none;
            color: white;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }

        /* Add hover effect for the login button */
        .login-container input[type="submit"]:hover {
            background-color: #4a148c;
        }

        /* Style the heading */
        .login-container h1 {
            text-align: center;
            color: #6a1b9a;
            font-size: 24px;
            margin-bottom: 20px;
        }
    </style>
</head>

<body>
    <div class="login-container">
        <h1>Login</h1>
        <form action="#">
            <input type="text" placeholder="Username" required><br>
            <input type="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
    </div>
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
