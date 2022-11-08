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
    def __init__(self,start):
        """Initialize class"""
        self.start = start
        self.new = start
    
    def __repr__(self):
         """Show representation."""
         return f"<SerialGenerator start={self.start} next={self.new}>"


    def generate(self):
        """Incriment number by 1"""
        self.new += 1
        return self.new 

    def reset(self):
        """Reset the generator"""
        self.new = self.start
        

