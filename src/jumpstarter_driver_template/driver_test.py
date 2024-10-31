from jumpstarter.common.utils import serve
from jumpstarter.drivers.power.common import PowerReading
from itertools import islice
from jumpstarter_driver_template.driver import ExamplePower, ExampleCustom


def test_example_power():
    with serve(ExamplePower()) as power:
        assert power.on() == "power turned on"
        assert power.off() == "power turned off"
        assert list(islice(power.read(), 3)) == [
            PowerReading(voltage=5.0, current=0.0),
            PowerReading(voltage=5.0, current=1.0),
            PowerReading(voltage=5.0, current=2.0),
        ]


def test_example_custom():
    with serve(ExampleCustom(custom_parameter="something")) as custom:
        custom.configure(1.0, "two", [3.0, 4.0])
        assert custom.slow_task(2.0) == "slept for 2.0 seconds"
