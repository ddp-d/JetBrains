class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.deposit_dollars = None
        self.deposit_cents = None
        self.total_amount = None

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        self.total_amount = self.dollars * 100 + self.cents
        if self.cents > 99:
            self.dollars = self.total_amount // 100
            self.cents = self.total_amount % 100
