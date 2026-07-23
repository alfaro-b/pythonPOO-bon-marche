class Customer:
    first_name = ''
    last_name = ''
    # --------------------------Methods---------------------

    def get_full_name(self, first_name, last_name):
        return first_name + ' ' + last_name

    # ------------------------Constructor-------------------

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name



