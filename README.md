# Jumpstarter Driver Template
Template repo for out-of-tree jumpstarter drivers

## Getting Started
> [!TIP]
> `<description>` represents placeholders in this documents, e.g. `foo-<put bar here>-baz` means `foo-bar-baz`, without the less/bigger than signs.

To get started, first create a new repository using this template. It's recommended to name the repo as `jumpstarter-driver-<driver name (e.g. raspberrypi)>`.

Then replace references to `jumpstarter-driver-template` with your own driver's name.
```shell
find * -type f -exec sed -i "s|\(jumpstarter[_-]driver[_-]\)template|\1<driver name>|" {} \;
```

Now you can decide if you want to implement an existing driver interface (standard driver) or create a fully custom driver. Existing driver interfaces cover common usecases such as power control, serial console and storage mux. They are easier to implement since the client part of the driver is provided, but less flexible.

### Standard Driver
An example implementation of `PowerInterface` can be found as the `ExamplePower` class in `src/jumpstarter_driver_template/driver.py`. In general, you are required to base your driver class on both the interface you want to implement and the `Driver` base class. After which you can implement the `abstractmethod` defined on the interface, in the case of `PowerInterface`, there are three: `on`, `off`, and `read`. Make sure to conform to the predefined function signature, and mark the methods with the `exporter` decorator, other than that the internal implementation can be however you prefer. An easy way to start is to use the `subprocess` module to call existing tools or scripts, and gradually rewrite them in python.

### Custom Driver
An example custom driver can be found as the `ExampleCustom` class in `src/jumpstarter_driver_template/driver.py`. Unlike standard drivers, custom drivers only have to inherit from the `Driver` base class. One of the features of custom drivers is they can take arbitrary (yaml serializable) configuration parameters, thus it's recommended to define custom drivers as `kw_only` dataclasses, the fields would be automatically initialized from the exporter config. Another peculiarity of custom drivers is you have to provide a `classmethod` named `client`, returning the full import path of the corresponding client class (which would be further explained later in this document).

Other than that, the implementation of custom drivers are very similar to standard drivers. It's recommended to keep the function signatures simple, taking only positional arguments and use simple data types, such as list or dict, so that they can be serialized into protobufs.

#### Custom Driver Clients
Clients for standard drivers are provided by jumpstarter, but for custom drivers, you need to write your own. A client for the `ExampleCustom` driver can be found as the `ExampleCustomClient` class in `src/jumpstarter_driver_template/client.py`. Having the driver and the client in different modules allows them to be distributed separately, avoiding installint extraneous dependencies on the client side. Client classes are based on the `DriverClient` base class, which would be automatically populated with data and methods for accessing the driver. Namely `call` and `streamingcall` are provided for calling regular functions and generator functions.

## Using Out-of-tree Driver
Out-of-tree drivers can be shipped as regular python packages to be installed into existing jumpstarter installations. Beware for custom drivers, it has to be installed on both the exporter and the client side, for standard drivers, installing them on the exporters is enough.

To build the package, run
```shell
uv build
```
And the wheel would be generated in `dist`

For container based installations, you can integrate the wheel into prebuilt jumpstarter container images, an example `Dockerfile` is provided in this repo.

## Content
### `pyproject.toml`
Python package metadata

### `Dockerfile`
Dockerfile for integrating out-of-tree driver with upstream jumpstarter image

### `src/jumpstarter_driver_template/driver.py`
Example driver implementation of the power interface definition and a custom driver using advanced features

### `src/jumpstarter_driver_template/client.py`
Client part of the custom driver

### `src/jumpstarter_driver_template/driver_test.py`
Tests for the drivers and clients
