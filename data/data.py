from dataclasses import dataclass
from datetime import date


@dataclass
class Person:
    full_name: str = None
    first_name: str = None
    last_name: str = None
    age: int = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    salary: int = None
    department: str = None
    mobile: str = None
    birth: date = date