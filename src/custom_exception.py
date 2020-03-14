"""
Programs may name their own exception by creating a new exception class.

Exception should typically be derived from the Exception class.
When creating a module that can raise several distinct exception a common
practice is to create a base class for exception defined by that module
and subclass that to create specific exception classes for different error
condition.

Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions."""


class Error(Exception):
    """Base class for exception"""
    pass


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allwoed.
    
    Attributes:
        previous: state at begining of transition.
        next: attempted new state
        message: explanation of why the specific transition is not allowed.
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

