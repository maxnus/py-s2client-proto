"""Generate _pb2.py files from the s2client-proto .proto definitions."""

import glob
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PROTO_ROOT = ROOT / "external" / "s2client-proto"
PACKAGE = "s2clientprotocol"
OUTPUT_DIR = ROOT / "src" / PACKAGE


def main():
    proto_files = glob.glob(str(PROTO_ROOT / PACKAGE / "*.proto"))
    if not proto_files:
        print(f"No .proto files found in {PROTO_ROOT / PACKAGE}", file=sys.stderr)
        sys.exit(1)

    subprocess.run(
        [
            sys.executable, "-m", "grpc_tools.protoc",
            f"--proto_path={PROTO_ROOT}",
            f"--python_out={ROOT / 'src'}",
            *proto_files,
        ],
        check=True,
    )

    generated = sorted(f.name for f in OUTPUT_DIR.glob("*_pb2.py"))
    print(f"Generated {len(generated)} files in {OUTPUT_DIR}:")
    for name in generated:
        print(f"  {name}")


if __name__ == "__main__":
    main()
