from jumpstarter.client import DriverClient
from contextlib import contextmanager
from collections.abc import AsyncGenerator


# client classes are based on the DriverClient base class
class ExampleCustomClient(DriverClient):
    def configure(self, param1: float, param2: str, param3: list[float]) -> None:
        # the `call` method is provided by the DriverClient base class
        # for calling into the driver by method name
        self.call("configure", param1, param2, param3)

    def slow_task(self, seconds: float) -> str:
        # both blocking and async driver methods can be called from the client in the same way
        return self.call("slow_task", seconds)

    def slow_generator(self) -> AsyncGenerator[float]:
        # generator methods (blocking or async) MUST be called with the `streamingcall` method
        yield from self.streamingcall("slow_generator")

    # additional methods can be provided as appropriate
    def combined_action(self) -> None:
        result = self.slow_task(0.1)
        self.configure(1.0, result, [3.0, 4.0])

    # "stream" methods SHOULD be context managers to manage the lifecycle of the streams
    @contextmanager
    def random_stream(self):
        # new streams can be created with the provided `stream` method
        with self.stream(method="random_stream") as stream:
            yield stream
