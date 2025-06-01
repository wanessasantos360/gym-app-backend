from pydantic import BaseModel
from typing import Optional

class ExerciseDefinitionBase(BaseModel):
    name: str
    muscle_group: Optional[str] = None
    description: Optional[str] = None
    image_url: Optional[str] = None

class ExerciseDefinitionCreate(ExerciseDefinitionBase):
    pass

class ExerciseDefinition(ExerciseDefinitionBase):
    id: int

    class Config:
        from_attributes = True