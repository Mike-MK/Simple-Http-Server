class Handler:
    def start_response(url):
        try:
            if url == '' or url=='/':
                with open('index.html')as f:
                    response = f.read()
                    response = 'HTTP/1.0 200 OK\n\n' + response
                return response.encode()

            with open(url[1:]) as f:
                response = f.read()
                response = 'HTTP/1.0 200 OK\n\n' + response
                return response.encode()
            
        except Exception as e:
            print(e)
            return 'HTTP/1.0 500 Server error'.encode()