class MyClass:
    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password

    def print_ip(self):
        print(f"My IP is {self.ip_addr}")

    @staticmethod
    def say_hello():
        print("Say hello")
