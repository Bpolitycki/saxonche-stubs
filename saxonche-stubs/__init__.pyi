from typing import Any, Self, overload

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
    def new_xpath_processor(self) -> PyXPathProcessor:
        """Creates a new XPath processor, which used to evaluate XPath expressions."""
        ...
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
    def __init__(self) -> None: ...

class PyXdmItem:
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

class PyXdmMap(PyXdmItem):
    def __init__(self) -> None: ...

class PyXdmNode(PyXdmItem):
    def __init__(self) -> None: ...
