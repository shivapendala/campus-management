"""
EduCore Enterprise Framework - DSpace Open-Access Institutional Repository Metadata Archivist

Manages open-access repository for university scholarly assets:
- Faculty pre-prints and post-prints
- Master's theses and Ph.D. dissertations (Shodhganga compliance)
- Dublin Core XML metadata serialization (dc.title, dc.contributor.author, dc.date.issued)
"""

from typing import Dict, List, Any, Optional
import xml.etree.ElementTree as ET


class InstitutionalRepositoryArchivist:
    """
    Serializes academic research items to Dublin Core metadata format.
    """

    @classmethod
    def serialize_dublin_core(
        cls,
        title: str,
        authors: List[str],
        subject_keywords: List[str],
        abstract_text: str,
        publication_date_iso: str,
        doi_identifier: str
    ) -> str:
        """Construct Dublin Core XML metadata record."""
        root = ET.Element("dublin_core", {"schema": "dc"})

        elem_title = ET.SubElement(root, "dcvalue", {"element": "title", "qualifier": "none"})
        elem_title.text = title

        for a in authors:
            elem_a = ET.SubElement(root, "dcvalue", {"element": "contributor", "qualifier": "author"})
            elem_a.text = a

        elem_date = ET.SubElement(root, "dcvalue", {"element": "date", "qualifier": "issued"})
        elem_date.text = publication_date_iso

        elem_desc = ET.SubElement(root, "dcvalue", {"element": "description", "qualifier": "abstract"})
        elem_desc.text = abstract_text

        elem_ident = ET.SubElement(root, "dcvalue", {"element": "identifier", "qualifier": "doi"})
        elem_ident.text = doi_identifier

        return ET.tostring(root, encoding="unicode")
