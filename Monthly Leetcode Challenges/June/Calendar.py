class MyCalendar(object):

    def __init__(self):
        self.slots = []
        

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i = 0
        while i < len(self.slots):
            if start not in range(self.slots[i][0], self.slots[i][1]):
                for booking in self.slots:
                    if end in range(booking[0] + 1, booking[1]) or (start < booking[0] and end > booking[1]):
                        return False
                i += 1
            else:
                return False
                
        self.slots.append((start, end))
        return True


x = MyCalendar()
x.book(10,20)
x.book(15, 25)
x.book(20, 30)
x.book(40, 45)
