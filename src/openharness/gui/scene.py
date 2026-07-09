from PySide6.QtWidgets import QGraphicsScene

from openharness.gui.connector_item import ConnectorItem
from openharness.model.connector import ConnectorHousing
from openharness.model.contact import Contact


class HarnessScene(QGraphicsScene):
    def __init__(self) -> None:
        super().__init__()
        self.setSceneRect(-10000, -10000, 20000, 20000)
        self._create_demo_connector()

    def _create_demo_connector(self) -> None:
        connector = ConnectorHousing(
            ref="J1",
            manufacturer="Molex",
            part_number="5557-10R",
            description="10 Pin Connector Housing",
            library_link="https://www.molex.com",
            x=100,
            y=100,
            contacts=[
                Contact("1", "+24V", "Molex", "5556TL", "socket", "W001", "RD"),
                Contact("2", "GND", "Molex", "5556TL", "socket", "W002", "BK"),
                Contact("3", "DOOR_OPEN", "Molex", "5556TL", "socket", "W003", "BU"),
                Contact("4", "SENSOR", "Molex", "5556TL", "socket", "W004", "YE"),
                Contact("5", "N.C", "Molex", "5556TL", "socket", "", ""),
            ],
        )

        self.addItem(ConnectorItem(connector))