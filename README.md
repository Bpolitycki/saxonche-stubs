# saxonche-stubs

Type stubs for the [saxonche](https://pypi.org/project/saxonche/) python package. This package has no functionality itself, but is merely an addition to the completion within IDEs. The basis for type annotations and comments is the documentation of [the Saxon Python API](https://www.saxonica.com/saxon-c/doc11/html/saxonc.html).

At the moment not all APIs are fully typed. To install the stubs just install the git repo via poetry or any other package manager.

You can use `stubtest` to get an impression of untyped components:

```sh
poetry run stubtest saxonche
```

## Author / Contact

- [Bastian Politycki](https://github.com/Bpolitycki) – Swiss Law Sources
