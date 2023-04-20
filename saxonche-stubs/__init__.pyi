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

class PyXdmNode(PyXdmItem):
    def __init__(self) -> None: ...
