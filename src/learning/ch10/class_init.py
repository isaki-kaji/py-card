class Person:
    __slots__ = ["firstname", "lastname", "age"]

    @classmethod
    def show(person, a: str) -> str:
        return f"やぁ、{a}"

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

    def show_name(self) -> None:
        print(f"私の名前は{self.firstname}{self.lastname}です！")


if __name__ == '__main__':
    person = Person("isaki", "kaji")
    print(person.firstname)
    print(person.lastname)
    person.age = 25
    print(person.age)
    person.show_name()
    print(Person.show("taki"))
