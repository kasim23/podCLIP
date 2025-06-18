from pathlib import Path
import subprocess
from app.models.media import Episode

class InputProcessor:
    """Downloads audio & converts to Whisper-ready WAV."""

    def __init__(self, data_root: Path):
        self.data_root = data_root

    def download_audio(self, ep: Episode) -> Path:
        raw_path = self.data_root / ep.raw_path
        if raw_path.exists():
            return raw_path
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        cmd = [
            "yt-dlp",
            "-x", "--audio-format", "mp3",
            "-o", str(raw_path),
            ep.source_url,
        ]
        subprocess.run(cmd, check=True)
        return raw_path

    def convert_to_wav(self, ep: Episode) -> Path:
        wav_path = self.data_root / ep.wav_path
        if wav_path.exists():
            return wav_path
        wav_path.parent.mkdir(parents=True, exist_ok=True)
        cmd = [
            "ffmpeg", "-i", str(self.data_root / ep.raw_path),
            "-ac", "1", "-ar", "16000",
            str(wav_path),
        ]
        subprocess.run(cmd, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return wav_path

    def ingest(self, ep: Episode) -> Episode:
        self.download_audio(ep)
        self.convert_to_wav(ep)
        return ep
