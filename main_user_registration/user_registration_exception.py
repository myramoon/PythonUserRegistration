class InvalidInput(Exception):
    def __init__(self, message):
        """
        :param message:
        """
        super().__init__(message)
