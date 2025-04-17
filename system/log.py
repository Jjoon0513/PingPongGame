class Console:
    def __init__(self, class_:type):
        self.class_ = class_

    def log(self, msg:str):
        print(f"from {self.class_.__module__} at {self.class_.__name__}: {msg}")


def debug(msg:str):
    print(f"DEBUG: {msg}")