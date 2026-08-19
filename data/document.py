from dataclasses import dataclass


@dataclass
class Document:
    id: str
    text: str
    metadata: dict