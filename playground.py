
def main():
    some_record = {'name': 'John'}
    employee = CommissionedEmployee(record=some_record)
    employee.is_payday()


class Pay:
    def __init__(self, record):
        self.record = record

    def is_payday(self):
        NotImplementedError


class CommissionedEmployee(Pay):
    def is_payday(self):
        print(self.record)


main()
