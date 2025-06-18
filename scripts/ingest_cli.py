import json, sys
from pathlib import Path
from app.models.media import Episode
from app.services.input_processor import InputProcessor

def main(manifest="app/data/manifest.json"):
    manifest = Path(manifest)
    data_root = manifest.parent
    ip = InputProcessor(data_root)
    entries = json.load(manifest.open())
    for e in entries:
        ep = Episode(**e)
        print(f"Ingesting {ep.episode_id} …")
        ip.ingest(ep)
        print("✅  done")

if __name__ == "__main__":
    main(*sys.argv[1:])
