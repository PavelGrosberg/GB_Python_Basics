import view
from db_manager import PhoneBook

pb_class = PhoneBook('phone_db.txt')


def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                pass
            case 2:
                pb_class.save_file()
            case 3:
                pb = pb_class.get()
                view.show_contacts(pb)
            case 4:
                new = view.new_contact_input()
                name = new['name']
                if view.confirm('добавить', name):
                    pb_class.add(new)
                if pb_class.check_changes():
                    if view.confirm_changes():
                        pb_class.save_file()
            case 5:
                pb = pb_class.get()
                view.show_contacts(pb)
                ind = view.input_id()
                contact = view.new_contact_input()
                name = contact['name']
                if view.confirm('изменить', name):
                    pb_class.change_contact(ind, contact)
                if pb_class.check_changes():
                    if view.confirm_changes():
                        pb_class.save_file()
            case 6:
                find = view.find_contact()
                result = pb_class.find(find)
                view.show_contacts(result)
            case 7:
                pb = pb_class.get()
                view.show_contacts(pb)
                ind = view.input_id()
                name = pb_class.get_name(ind)
                if view.confirm('удалить', name):
                    pb_class.delete_contact(ind)
            case 8:
                if pb_class.check_changes():
                    if view.confirm_changes():
                        pb_class.save_file()

                print('До свидания!')
                break
