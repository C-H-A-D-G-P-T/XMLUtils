import xml.dom.minidom as minidom

class XMLUtils:
    def dump_xml(self, xml_string):
        """
        Cleans up and pretty-prints the provided XML string without the XML declaration.
        Args:
            xml_string (str): The raw XML string.
        Returns:
            str: The cleaned and formatted XML string without the XML declaration.
        """
        # Parse the XML string into a DOM object
        dom = minidom.parseString(xml_string)
        # Pretty-print with indentation
        pretty_xml = dom.toprettyxml(indent="    ")
        # Remove the XML declaration and empty lines
        cleaned_xml = "\n".join([line for line in pretty_xml.splitlines() if line.strip() and not line.startswith("<?xml")])
        return cleaned_xml