from typing import Optional
from pydantic import BaseModel


class PcbSpecsBase(BaseModel):
    pcb_information: str
    value: int
    notes: Optional[str] = None

class PcbSpecsOutput(PcbSpecsBase):
    id: Optional[int] = None
    pcb_information: Optional[str] = None
    value: Optional[int] = None
    notes: Optional[str] = None


class TestPointListBase(BaseModel):
    net: Optional[str] = None
    name: Optional[str] = None
    x_coord: Optional[str] = None
    y_coord: Optional[str] = None
    side: Optional[str] = None
    type: Optional[str] = None
    hole_size: Optional[str] = None


class TestPointListOutput(TestPointListBase):
    id: Optional[int] = None