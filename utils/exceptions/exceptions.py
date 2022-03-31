
class InvalidFormatError(Exception):
    def __init__(self, message="Invalid format"):
        self.message = message
        super().__init__(self.message)