# Jumpstarter Driver Template
Template repo for custom jumpstarter drivers

## Getting Started
> [!TIP]
> `<description>` represents placeholders in this documents, e.g. `foo-<put bar here>-baz` means `foo-bar-baz`, without the less/bigger than signs.

To get started, first create a new repository using this template. It's recommended to name the repo as `jumpstarter-driver-<driver name (e.g. raspberrypi)>`.

Then replace references to `jumpstarter-driver-template` with your own driver's name.
```shell
find * -type f -exec sed -i "s|\(jumpstarter[_-]driver[_-]\)template|\1<driver name>|" {} \;
```

Now you can decide if you want to implement an existing driver interface or create a fully custom driver. Existing driver interfaces cover common usecases such as power control, serial console and storage mux. They are easier to implement since the client part of the driver is provided, but less flexible.

### Existing Driver Interface
An example implementation of `PowerInterface` can be found as the `ExamplePower` class in `src/jumpstarter_driver_template/driver.py`. In general, you are required to base your driver class on both the interface you want to implement and the `Driver` base class. After which you can implement the `abstractmethod` defined on the interface, in the case of `PowerInterface`, there are three: `on`, `off`, and `read`.

### Custom Driver

## Content
### `pyproject.toml`
Python package metadata

### `Dockerfile`
Dockerfile for integrating custom driver with upstream jumpstarter image

### `src/jumpstarter_driver_template/driver.py`
Example driver implementation of the power interface definition and a custom driver using advanced features

### `src/jumpstarter_driver_template/client.py`
Client part of the custom driver

### `src/jumpstarter_driver_template/driver_test.py`
Tests for the drivers and clients
