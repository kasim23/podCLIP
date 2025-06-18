from pydantic import BaseModel, HttpUrl, Field

class Episode(BaseModel):
    episode_id: str
    source_url: HttpUrl
    raw_path: str  # path to downloaded .mp3
    wav_path: str  # path to 16 kHz mono .wav
    length_sec: int | None = Field(
        None, description="Optional rough length for progress bar."
    )

