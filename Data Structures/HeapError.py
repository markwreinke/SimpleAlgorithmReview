class HeapError(Exception):
    """Raised when an operator doesn't work well with a heap.

        Attributes:
            message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
