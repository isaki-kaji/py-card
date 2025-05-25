from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    value: str

    def __post_init__(self):
        if "@" not in self.value:
            raise ValueError("Invalid email format")


email = Email("sdfsf@com")
print(email.value)
email.value = "ss@ff"
print(email.value)
