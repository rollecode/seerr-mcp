#!/usr/bin/env python3
"""Turn Overseerr's YAML spec into the JSON the generator reads.

Two things need fixing on the way. The spec's paths are relative to a server
URL of `{server}/api/v1`, and the generator emits absolute request paths, so
the prefix is folded in. YAML also parses bare dates into date objects, which
JSON cannot hold; they only appear in examples, so stringifying is enough.

    python scripts/convert_spec.py overseerr-api.yml openapi.json
"""

import json
import sys

import yaml

API_PREFIX = "/api/v1"


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    with open(sys.argv[1]) as handle:
        spec = yaml.safe_load(handle)

    spec["paths"] = {API_PREFIX + path: value for path, value in spec["paths"].items()}

    with open(sys.argv[2], "w") as handle:
        json.dump(spec, handle, default=str)

    operations = sum(
        1
        for methods in spec["paths"].values()
        for method in methods
        if method in ("get", "post", "put", "delete", "patch")
    )
    print(f"{len(spec['paths'])} paths, {operations} operations -> {sys.argv[2]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
