class ServerConnectionException(Exception):
    pass


class PythonTest:
    def __init__(self, num):
        self.num = num

        print("1")
        if num == 2:
            raise ServerConnectionException
        print("2")

    def __del__(slef):
        print("del is called")


if __name__ == '__main__':
    try:
        test = PythonTest(3)
    except ServerConnectionException:
        print("This will be called")
