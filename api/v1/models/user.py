from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing import Optional, List
from typing_extensions import Annotated

from bson import ObjectId


PyObjectId = Annotated[str, BeforeValidator(str)]    

class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str = Field(...)
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    hashed_password: str = Field(...)
    disabled: bool = Field(default=False)
    photo: str = Field(default="empty")
    band_ids: List[str] = Field(default=[])
    model_config = ConfigDict(
        populate_by_name = True,
        arbitrary_types_allowed = True,
        json_schema_extra = {
            "example": {
                "username": "lizard_king",
                "full_name": "Jim Morrison",
                "email": "li.king@thedoors.com",
                "hashed_password": "latuyaporsiacaso",
                "disabled": False,
                "photo": "empty",
                "band_ids": [
                    "..."
                ]
            }
        },
    )

class UpdateUserModel(BaseModel):
    name: Optional[str] = None
    photo: Optional[str] = None
    description: Optional[str] = None
    song_ids: Optional[List[str]] = None
    user_ids: Optional[List[str]] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders = {ObjectId: str},
        json_schema_extra = {
            "example": {
                "name": "The Sodawaves",
                "photo": "...",
                "description": "Indie Rock user from Algeciras",
                "song_ids": [
                    "65e6d5cb2258227facc570c1",
                    "..."
                ],
                "user_ids": [
                    "65e6d5cb2258227facc570c1",
                    "65e6d5cb2258227facc570c0",
                    "..."
                ]
            }
        },
    )


class UserCollection(BaseModel):
    users: List[UserModel]