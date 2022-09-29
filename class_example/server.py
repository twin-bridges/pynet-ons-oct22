class Server:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password

    def test_method(self):
        print(f"Device is: {self.hostname}")
        print(f"Username is: {self.username}")


svr1 = Server("test.domain.com", "admin", "passwd1")
svr1.test_method()
