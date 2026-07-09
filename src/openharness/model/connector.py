from dataclasses import dataclass, field

from openharness.model.contact import Contact


@dataclass
class ConnectorHousing:
    ref: str
    manufacturer: str = ""
    part_number: str = ""
    description: str = ""
    library_link: str = ""
    x: float = 0
    y: float = 0
    contacts: list[Contact] = field(default_factory=list)

    @property
    def display_name(self) -> str:
        if self.manufacturer and self.part_number:
            return f"{self.ref}\n{self.manufacturer} {self.part_number}"
        if self.part_number:
            return f"{self.ref}\n{self.part_number}"
        return self.ref