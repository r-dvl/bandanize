from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing import Optional, List
from typing_extensions import Annotated

from bson import ObjectId

PyObjectId = Annotated[str, BeforeValidator(str)]   

tabTemplate = """
e|---------------------------------------------------------------|
B|---------------------------------------------------------------|
G|---------------------------------------------------------------|
D|---------------------------------------------------------------|
A|---------------------------------------------------------------|
E|---------------------------------------------------------------|
"""

class TabModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    instrument: str = Field(...)
    description: str = Field(default="")
    tuning: str = Field(default="Standard")
    tab: str = Field(default=tabTemplate)
    song_id: str = Field(default=[])
    model_config = ConfigDict(
        populate_by_name = True,
        arbitrary_types_allowed = True,
        json_schema_extra = {
            "example": {
                "title": "Lead and Rythm",
                "instrument": "Guitar",
                "description": "Solo FX is difficult to reproduce",
                "tuning": "Standard",
                "tab": "...",
                "song_id": "60a4b5c0f0a4c9f1d4e7d6b1"
            }
        },
    )

class UpdateTabModel(BaseModel):
    title: Optional[str] = None
    instrument: Optional[str] = None
    description: Optional[str] = None
    tuning: Optional[str] = None
    tab: Optional[str] = None
    song_id: Optional[str] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders = {ObjectId: str},
        json_schema_extra = {
            "example": {
                "title": "Lead and Rythm",
                "instrument": "Guitar",
                "description": "Solo FX is difficult to reproduce",
                "tuning": "Standard",
                "tab": "...",
                "song_id": "60a4b5c0f0a4c9f1d4e7d6b1"
            }
        },
    )


class TabCollection(BaseModel):
    tabs: List[TabModel]