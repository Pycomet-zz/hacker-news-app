from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase

from datetime import date


@dataclass_json
@dataclass
class Base:
    uid: int
    by: str
    type: str
    time: int
    deleted: bool = False
    dead: bool = False


@dataclass_json
@dataclass
class Comment(Base):
    text: str = ""


@dataclass_json
@dataclass
class Job(Base):
    "New Job Model"
    text: str = ""
    url: str = ""
    title: str = ""


@dataclass_json
@dataclass
class Story(Base):
    descendants: int = 0
    score: int = 0
    title: str = ""
    url: str = ""


@dataclass_json
@dataclass
class Poll(Base):
    # parts: list
    descendants: int = 0
    score: int = 0
    title: str = ""
    text: str = ""
