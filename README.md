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
