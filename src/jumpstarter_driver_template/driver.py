from dataclasses import dataclass
from itertools import count

from jumpstarter.driver import Driver, export
from jumpstarter.drivers.power.driver import PowerInterface
from jumpstarter.drivers.power.common import PowerReading
from collections.abc import Generator


@dataclass(kw_only=True)
class ExamplePower(PowerInterface, Driver):
    """
    Example driver implementing predefined interface
    """

    @export  # driver methods MUST be marked with the `export` decorator
    def on(self) -> str:
        return "power turned on"

    @export
    def off(self) -> str:
        return "power turned off"

    @export  # driver methods CAN be regular functions or generator functions
    def read(self) -> Generator[PowerReading]:
        for i in count():
            yield PowerReading(
                voltage=5.0,
                current=i,
            )
