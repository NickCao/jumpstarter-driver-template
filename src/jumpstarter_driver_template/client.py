from jumpstarter.client import DriverClient


class ExampleCustomClient(DriverClient):
    def configure(self, param1: float, param2: str, param3: list[float]) -> None:
        self.call("configure", param1, param2, param3)

    def slow_task(self, seconds: float) -> str:
        return self.call("slow_task", seconds)
