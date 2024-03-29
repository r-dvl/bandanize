from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing import Optional, List
from typing_extensions import Annotated

from bson import ObjectId


PyObjectId = Annotated[str, BeforeValidator(str)]

class SongModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    band: str = Field(...)
    bpm: str = Field(...)
    key: str = Field(...)
    media: List[str] = Field(default=[])
    playlist_id: str = Field(default="")
    tab_ids: List[str] = Field(default=[])
    model_config = ConfigDict(
        populate_by_name = True,
        arbitrary_types_allowed = True,
        json_schema_extra = {
            "example": {
                "title": "D is for Dangerous",
                "band": "Arctic Monkeys",
                "bpm": "120",
                "key": "standard",
                "media": [
                    ""
                ],
                "playlist_id": "60a4b5c8f0a4c9f1d4e7d6b2",
                "tab_ids": [
                    "60a4b5c8f0a4c9f1d4e7d6b2",
                    "60a4b5d0f0a4c9f1d4e7d6b3"
                ]
            }
        },
    )

class UpdateSongModel(BaseModel):
    title: Optional[str] = None
    band: Optional[str] = None
    bpm: Optional[str] = None
    key: Optional[str] = None
    media: Optional[List[str]] = None
    playlist_id: Optional[List[str]] = None
    tab_ids: Optional[List[str]] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders = {ObjectId: str},
        json_schema_extra = {
            "example": {
                "title": "D is for Dangerous",
                "band": "Arctic Monkeys",
                "bpm": "120",
                "key": "standard",
                "media": [
                    ""
                ],
                "playlist_id": "60a4b5c8f0a4c9f1d4e7d6b2",
                "tab_ids": [
                    "60a4b5c8f0a4c9f1d4e7d6b2",
                    "60a4b5d0f0a4c9f1d4e7d6b3"
                ]
            }
        },
    )


class SongCollection(BaseModel):
    songs: List[SongModel]