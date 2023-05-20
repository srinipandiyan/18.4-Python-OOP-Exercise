"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize a starting value for serial generator object"""
        self.start = start
        self.counter = start

    def generate(self):
        """Generate the serial number by incrementing serial generator object by one."""
        serial_num = self.counter
        self.counter += 1
        return serial_num

    def reset(self):
        """Reset serial generator object to starting value."""
        self.counter = self.start
    
