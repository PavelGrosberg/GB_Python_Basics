class PhoneBook:
    phone_book = []
    new_phone_book = []
    path = 'phone_db.txt'

    def __init__(self, path):
        self.path = path

        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {'name': new[0],
                               'phone': new[1],
                               'comment': new[2]}
                self.phone_book.append(new_contact)

    def save_file(self):
        data = []
        for contact in self.phone_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def get(self):
        return self.phone_book

    def add(self, new_contact: dict):
        self.phone_book.append(new_contact)

    def find(self, find_option: str):
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_option.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def change_contact(self, ind: int, contact: dict):
        self.phone_book.pop(ind - 1)
        self.phone_book.insert(ind - 1, contact)

    def delete_contact(self, ind: int):
        self.phone_book.pop(ind - 1)

    def get_name(self, ind: int):
        return self.phone_book[ind - 1].get('name')

    def check_changes(self):
        if self.phone_book != self.new_phone_book:
            return True
        return False
