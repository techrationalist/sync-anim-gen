from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class AnimationMarkerType(Enum):
    write = "write"
    wait = "wait"


class AnimationMarkerStart(BaseModel):
    id: str = Field(..., description="Unique identifier for the animation marker")
    text: Optional[str] = None
    type: AnimationMarkerType = Field(
        ...,
        description="Type of the animation marker",
        examples=[item for item in AnimationMarkerType],
    )


class AnimationMarkerEnd(BaseModel):
    id: str = Field(
        ...,
        description="Unique identifier for the animation marker. This should match the id of the start marker",
    )


class TimeStampsData(BaseModel):
    word: str
    start: float
    end: float
    animationStart: Optional[AnimationMarkerStart] = None
    animationEnd: Optional[AnimationMarkerEnd] = None


class StepsConfig(BaseModel):
    """
    `manim` cli tool expects to be able to instantiate the scenes without any arguments.
    We should pass arguments to `Scene` constructor.
    That is why we need to store the config data in a file and read it in Scene constructor.
    """

    timestampsFile: str
    outputFile: str


class AnimationDataOutput(BaseModel):
    id: str
    text: Optional[str] = None
    startTime: float
    endTime: Optional[float] = None
    type: str
