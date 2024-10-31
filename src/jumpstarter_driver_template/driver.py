from dataclasses import dataclass
from itertools import count
from anyio import sleep

from jumpstarter.driver import Driver, export
from jumpstarter.drivers.power.driver import PowerInterface
from jumpstarter.drivers.power.common import PowerReading
from collections.abc import Generator
import logging

# drivers SHOULD use standrd python logging
logger = logging.getLogger(__name__)


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


@dataclass(kw_only=True)  # drivers taking config values SHOULD be kw_only dataclasses
class ExampleCustom(Driver):
    """
    Example driver implementing custom interface
    """

    # config values would be automatically initialized from the exporter config
    custom_parameter: str

    # required classmethod returning the import path of corresponding client class
    @classmethod
    def client(cls) -> str:
        # roughly equals "from jumpstarter_driver_template.client import ExampleCustomClient"
        # see `client.py` for implementation
        return "jumpstarter_driver_template.client.ExampleCustomClient"

    # driver methods can take positional arguments
    @export
    def configure(self, param1: float, param2: str, param3: list[float]) -> None:
        # e.g. configure the device with parameters
        logger.info(f"configure called with parameters: {param1}, {param2}, {param3}")

    # driver methods can be async
    @export
    async def slow_task(self, seconds: float) -> str:
        await sleep(seconds)
        return f"slept for {seconds} seconds"
