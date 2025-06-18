import pytest
from pathlib import Path
from unittest.mock import patch
from app.models.media import Episode
from app.services.input_processor import InputProcessor

@pytest.fixture
def episode(tmp_path):
    return Episode(
        episode_id="test",
        source_url="https://youtube.com/watch?v=dQw4w9WgXcQ",
        raw_path="raw/test.mp3",
        wav_path="processed/audio_wav/test.wav",
    )

@patch("subprocess.run")
def test_ingest_calls_yt_dlp(mock_run, tmp_path, episode):
    ip = InputProcessor(tmp_path)
    ip.ingest(episode)
    # First call yt-dlp, second call ffmpeg
    yt_cmd, ff_cmd = mock_run.call_args_list
    assert "yt-dlp" in yt_cmd[0][0][0]
    assert "ffmpeg" in ff_cmd[0][0][0]
