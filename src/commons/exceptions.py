"""
Register all exception classes
"""


class NotFoundItemQuery(Exception):
    """
    A class represent a class to throw when the product is not found
    Args:
    -   message:(str) message to display
    """

    message: str = "Not found Items"
