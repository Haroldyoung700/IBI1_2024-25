import xml.dom.minidom
import xml.sax
from datetime import datetime
import os
os.chdir('Practical14')

def dom_parser(xml_file):
    start_time = datetime.now()
    dom = xml.dom.minidom.parse(xml_file)

    max_counts = {
        "molecular_function": {"id": "", "count": 0},
        "biological_process": {"id": "", "count": 0},
        "cellular_component": {"id": "", "count": 0}
    }

    for term in dom.getElementsByTagName("term"):
        namespace = term.getElementsByTagName("namespace")[0].firstChild.data.strip()
        term_id = term.getElementsByTagName("id")[0].firstChild.data.strip()

        if namespace in max_counts:
            is_a_list = term.getElementsByTagName("is_a")
            current_count = len(is_a_list)

            if current_count > max_counts[namespace]["count"]:
                max_counts[namespace]["id"] = term_id
                max_counts[namespace]["count"] = current_count

    dom_time = (datetime.now() - start_time).total_seconds()
    return max_counts, dom_time

class GoboSaxHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.max_counts = {
            "molecular_function": {"id": "", "count": 0},
            "biological_process": {"id": "", "count": 0},
            "cellular_component": {"id": "", "count": 0}
        }
        self.current_data = {"namespace": "", "term_id": "", "is_a_count": 0}
        self.current_element = ""
    def startElement(self, tag, s):
        self.current_element = tag
        if tag == "term": 
            self.current_data = {"namespace": "", "term_id": "", "is_a_count": 0}
        elif tag == "is_a":
            self.current_data["is_a_count"] += 1

    def characters(self, content):
        if self.current_element == "namespace":
            self.current_data["namespace"] += content.strip()
        elif self.current_element == "id":
            self.current_data["term_id"] += content.strip()

    def endElement(self, tag):
        if tag == "term":
            namespace = self.current_data["namespace"]
            if namespace in self.max_counts:
                current_count = self.current_data["is_a_count"]
                if current_count > self.max_counts[namespace]["count"]:
                    self.max_counts[namespace]["id"] = self.current_data["term_id"]
                    self.max_counts[namespace]["count"] = current_count

def sax_parser(xml_file):
    start_time = datetime.now()
    handler = GoboSaxHandler()
    xml.sax.parse(xml_file, handler)
    sax_time = (datetime.now() - start_time).total_seconds()
    return handler.max_counts, sax_time

if __name__ == "__main__":
    xml_path = "go_obo.xml"

    dom_results, dom_time = dom_parser(xml_path)
    sax_results, sax_time = sax_parser(xml_path)

    print("DOM Results:")
    for ontology, data in dom_results.items():
        print(f"{ontology}: GO:{data['id']} with {data['count']} is_a relationships")
    
    print("\nSAX Results:")
    for ontology, data in sax_results.items():
        print(f"{ontology}: GO:{data['id']} with {data['count']} is_a relationships")

    print(f"\nDOM Time: {dom_time:.4f} seconds")
    print(f"SAX Time: {sax_time:.4f} seconds")
    print("# SAX was faster" if sax_time < dom_time else "# DOM was faster")