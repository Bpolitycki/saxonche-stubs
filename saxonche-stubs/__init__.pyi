from typing import Any, Iterator, Self, overload

def __getattr__(name: str) -> Any: ...

class PySaxonProcessor:
    def __init__(self, license: bool = False) -> None:
        """An SaxonProcessor acts as a factory for generating XQuery, XPath, Schema
        and XSLT compilers. This class is itself the context that needs to be managed
        (i.e. allocation & release)"""
        ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: Any,
        exc_val: Any,
        exc_tb: Any,
    ) -> None: ...
    def clear_configuration_properties(self) -> None:
        """Clear all configuration properties that have been set"""
        ...
    def exception_clear(self) -> None:
        """Clear any exception that has been raised"""
        ...
    def exception_occurred(self) -> bool:
        """Check whether an exception has been raised internally within Saxon/C.

        Returns:
            bool: True if an exception has been raised, False otherwise
        """
        ...
    def make_boolean_value(self, value: bool) -> PyXdmAtomicValue:
        """Create an XdmValue from a boolean.

        Args:
            value (bool): The boolean value

        Returns:
            PyXdmAtomicValue: The XdmAtomicValue representing the boolean value.
        """
        ...
    def make_integer_value(self, value: int) -> PyXdmAtomicValue:
        """Create Int64Value or a BigIntegerValue from an integer.

        Args:
            value (int): The integer value

        Returns:
            PyXdmAtomicValue: The XdmAtomicValue representing the integer value.
        """
        ...
    def make_string_value(self, str_: str) -> PyXdmAtomicValue:
        """Create an XdmValue from a string.

        Args:
            str_ (str): The string value. NULL is taken as equivalent to "".

        Returns:
            PyXdmAtomicValue: The XdmAtomicValue representing the string value.
        """
        ...
    def new_xpath_processor(self) -> PyXPathProcessor:
        """Creates a new XPath processor, which used to evaluate XPath expressions."""
        ...
    def new_xquery_processor(self) -> PyXQueryProcessor:
        """Creates a new XQuery processor, which used to evaluate XQuery expressions."""
        ...
    def new_xslt30_processor(self) -> PyXslt30Processor: ...
    @overload
    def parse_xml(self, xml_file_name: str) -> PyXdmNode:
        """Parse a lexical representation, source file or uri of the source document
        and return it as an Xdm Node

        Args:
            xml_file_name (str): The file name of the source document

        Returns:
            PyXdmNode: The Xdm Node representing the source document
        """
        ...
    @overload
    def parse_xml(self, xml_text: str) -> PyXdmNode:
        """Parse a lexical representation, source file or uri of the source document
        and return it as an Xdm Node

        Args:
             xml_text (str): The lexical representation of the source document

        Returns:
            PyXdmNode: The Xdm Node representing the source document
        """
        ...
    @overload
    def parse_xml(self, xml_uri: str) -> PyXdmNode:
        """Parse a lexical representation, source file or uri of the source document
         and return it as an Xdm Node

         Args:
             xml_uri (str): The uri of the source document

        Returns:
             PyXdmNode: The Xdm Node representing the source document
        """
        ...

class PyXPathProcessor:
    def __init__(self) -> None:
        """An XPathProcessor represents factory to compile, load and execute the XPath query."""
        ...
    def clear_parameters(self) -> None:
        """Clear all parameters that have been set"""
        ...
    def clear_properties(self) -> None:
        """Clear all properties that have been set"""
        ...
    def declare_namespace(self, prefix: str, uri: str) -> None:
        """Declare a namespace prefix for use in XPath expressions.

        Args:
            prefix (str): The namespace prefix
            uri (str): The namespace uri
        """
        ...
    def effective_boolean_value(self, xpath_str: str) -> bool:
        """Evaluate an XPath expression and return the effective boolean value of the result.

        Args:
            xpath (str): The XPath expression

        Returns:
            bool: The effective boolean value of the result
        """
        ...
    def evaluate(self, xpath_str: str) -> PyXdmValue | None:
        """Evaluate an XPath expression and return the result as a sequence.

        Args:
            xpath (str): The XPath expression

        Returns:
            PyXdmValue: A sequence of Xdm Values is returned. Return None if the expression returns an empty sequence.
        """
        ...
    def evaluate_single(self, xpath_str: str) -> PyXdmItem | None:
        """Evaluate an XPath expression and return the result as a single item.

        Args:
            xpath (str): The XPath expression

        Returns:
            PyXdmValue: A single Xdm Item is returned. Return None if the expression returns an empty sequence.
            If the expression returns a sequence of more than one item, any items after the first are ignored.
        """
        ...
    def exception_clear(self) -> None:
        """Clear any exception that has been raised"""
        ...
    def exception_count(self) -> int:
        """Get the number of errors and warnings that have been reported.

        Returns:
            int: The number of errors and warnings that have been reported
        """
        ...
    def exception_occured(self) -> bool:
        """Check whether an exception has been raised internally within Saxon/C.

        Returns:
            bool: True if an exception has been raised, False otherwise
        """
        ...
    @overload
    def set_context(self, file_name: str) -> None:
        """Set the context item from a file.

        Args:
            file_name (str): The file name of the context item
        """
        ...
    @overload
    def set_context(self, xdm_item: PyXdmItem) -> None:
        """Set the context item from an XdmItem.

        Args:
            xdm_item (PyXdmItem): The XdmItem of the context item
        """
        ...

class PyXQueryProcessor:
    def __init__(self) -> None:
        """An PyXQueryProcessor object represents factory to compile, load and execute queries."""
    ...

class PyXslt30Processor:
    def __init__(self) -> None:
        """An PyXslt30Processor represents factory to compile, load and execute a stylesheet."""
        ...
    def clear_parameters(self) -> None:
        """Clear all parameters that have been set"""
        ...
    def set_parameter(self, name: str, value: PyXdmValue) -> None:
        """Set the value of a stylesheet parameter.

        Args:
            name (str): The name of the stylesheet parameter, as a string.
                        For namespaced parameter use the JClark notation, that is "{uri}local".
            value (PyXdmValue): The value of the stylesheet parameter, or None to clear a previously set value.

        Returns:
            None
        """
        ...

class PyXdmValue:
    def __init__(self) -> None:
        """Value in the XDM data model. A value is a sequence of one or more items."""
        ...
    def __iter__(self) -> Iterator[PyXdmItem]:
        """Iterate over the items in the sequence.

        Returns:
            Iterator[PyXdmItem]: Iterator object of PyXdmValue
        """
        ...

class PyXdmItem(PyXdmValue):
    def __init__(self) -> None: ...
    def get_atomic_value(self) -> PyXdmAtomicValue:
        """Get the atomic value of this item.

        Returns:
            PyXdmAtomicValue: The atomic value of this item

        Raises:
            Exception: If the item is not an atomic value
        """
        ...
    def get_map_value(self) -> PyXdmMap:
        """Get the map value of this item.

        Returns:
            PyXdmMap: The map value of this item

        Raises:
            Exception: If the item is not a map
        """
        ...
    def get_node_value(self) -> PyXdmNode:
        """Get the node value of this item.

        Returns:
            PyXdmNode: The node value of this item

        Raises:
            Exception: If the item is not a node
        """
        ...
    @property
    def head(self) -> PyXdmItem | None:
        """Property which returns the first item in the sequence.

        Returns:
            PyXdmItem | None: The first item in the sequence or None if the sequence is empty
        """
        ...
    @property
    def is_array(self) -> bool:
        """Property which returns whether the item is an array.

        Returns:
            bool: True if the item is an array, False otherwise
        """
        ...
    @property
    def is_atomic(self) -> bool:
        """Property which returns whether the item is an atomic value.

        Returns:
            bool: True if the item is an atomic value, False otherwise
        """
        ...
    @property
    def is_function(self) -> bool:
        """Property which returns whether the item is a function.

        Returns:
            bool: True if the item is a function, False otherwise
        """
        ...
    @property
    def is_map(self) -> bool:
        """Property which returns whether the item is a map.

        Returns:
            bool: True if the item is a map, False otherwise
        """
        ...
    @property
    def is_node(self) -> bool:
        """Property which returns whether the item is a node.

        Returns:
            bool: True if the item is a node, False otherwise
        """
        ...
    @property
    def string_value(self) -> str:
        """Property which returns the string value.

        Returns:
            str: The string value of the atomic value
        """
        ...

class PyXdmFunctionItem(PyXdmItem):
    def __init__(self) -> None:
        """Represents a function item in the XDM data model."""
        ...

class PyXdmAtomicValue(PyXdmItem):
    def __init__(self) -> None:
        """Reprensts an atomic value in the XDM data model. Atomic values are either
        built-in atomic values (such as xs:integer or xs:date) or user-defined atomic
        values."""
        ...
    @property
    def boolean_value(self) -> bool:
        """Property which returns the boolean value.

        Returns:
            bool: The boolean value of the atomic value
        """
        ...
    @property
    def integer_value(self) -> int:
        """Property which returns the integer value.

        Returns:
            int: The integer value of the atomic value
        """
        ...

class PyXdmMap(PyXdmFunctionItem):
    def __init__(self) -> None:
        """The class PyXdmMap represents a map in the XDM data model. A map is a list of zero or more entries,
        each consisting of a key-value pair. The map itself is an XDM item and is immutable.
        """
        ...
    @property
    def map_size(self) -> int:
        """Property which returns the number of entries in the map.

        Returns:
            int: The number of entries in the map
        """
        ...
    @property
    def string_value(self) -> str:
        """Property which returns the string value of the map.

        Returns:
            str: The string value of the map
        """
        ...
    def contains_key(self, key: PyXdmAtomicValue) -> bool:
        """Check whether the map contains a given key.

        Args:
            key (PyXdmAtomicValue): The key

        Returns:
            bool: True if the map contains the key, False otherwise
        """
        ...
    def get(self, key: str | PyXdmAtomicValue | int | float) -> PyXdmValue | None:
        """Get the value associated with a given key.

        Args:
            key (str | PyXdmAtomicValue | int | float): The key

        Returns:
            PyXdmValue | None: The value associated with the key or None if the key is not present in the map
        """
        ...
    def keys(self) -> list[PyXdmAtomicValue]:
        """Get the keys of the map.

        Returns:
            list[PyXdmAtomicValue]: The keys of the map
        """
        ...
    def put(self, key: PyXdmAtomicValue, value: PyXdmValue) -> PyXdmMap:
        """Put an entry into the map. And return a new map with the entry added.

        Args:
            key (PyXdmAtomicValue): The key
            value (PyXdmValue): The value

        Returns:
            PyXdmMap: The map with the entry added
        """
        ...
    def remove(self, key: PyXdmValue) -> PyXdmMap:
        """Remove an entry from the map.

        Args:
            key (PyXdmValue): The key

        Returns:
            PyXdmMap: The map with the entry removed
        """
        ...
    def values(self) -> list[PyXdmValue]:
        """Get the values of the map.

        Returns:
            list[PyXdmValue]: The values of the map
        """
        ...

class PyXdmNode(PyXdmItem):
    def __init__(self) -> None: ...
