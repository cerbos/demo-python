#! /usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTAINER_IMG=${CONTAINER_IMG:-"pkg.cerbos.dev/containers/cerbos"}
CONTAINER_TAG=${CONTAINER_TAG:-"0.0.2"}

docker run -i -t -p 3592:3592 \
  -v ${SCRIPT_DIR}/policy:/policies \
  "${CONTAINER_IMG}:${CONTAINER_TAG}"


