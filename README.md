# py-s2client-proto

Prebuild Python protocol files to communicate with StarCraft II

This is based on the protobuf files from Blizzard's [s2client-proto](https://github.com/Blizzard/s2client-proto),
but with the generated Python files included, so you don't have to install the protobuf compiler
to generate them yourself.

## Installation

```bash
pip install pys2clientprotocol
```

Requires `protobuf>=6,<8` and Python 3.9+.

## Usage

```python
from s2clientprotocol import sc2api_pb2
```
