from detector.server import Server

if __name__ == '__main__':
    server = Server(key='secret key')
    server.start_server()
