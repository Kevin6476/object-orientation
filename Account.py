class Account:

    def __init__(self, number, holder, sale, limit):
        print("Inicializando classe... {}".format(self))
        self.number = number
        self.holder = holder
        self.sale = sale
        self.limit = limit

