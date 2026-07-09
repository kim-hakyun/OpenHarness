from dataclasses import dataclass


@dataclass
class Contact:
    number: str
    signal: str = ""
    manufacturer: str = ""
    part_number: str = ""
    contact_type: str = "crimp_contact"
    wire_no: str = ""
    wire_color: str = ""