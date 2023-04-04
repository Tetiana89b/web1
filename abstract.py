from abc import ABC, abstractmethod


class UserView(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_commands(self):
        pass


class ConsoleUserView(UserView):
    def display_contacts(self, contacts):
        print("Contacts:")
        for contact in contacts:
            print(contact)

    def display_notes(self, notes):
        print("Notes:")
        for note in notes:
            print(note)

    def display_commands(self):
        print("Commands:")
        print("1. Display contacts")
        print("2. Display notes")
        print("3. Display commands")
