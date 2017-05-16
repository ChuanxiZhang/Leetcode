class Logger(object):
    def __init__(self):
        self.cal = dict()

    def shouldPrintMessage(self, timestamp, message):
        if not self.cal.has_key(message):
            self.cal[message] = 0
        if timestamp - self.cal[message] >= 0 or self.cal[message] == 0:
            self.cal[message] = timestamp + 10
            return True
        else:
            return False



            # Your Logger object will be instantiated and called as such:
            # obj = Logger()
            # param_1 = obj.shouldPrintMessage(timestamp,message)