#! /usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONTAINER_IMG=${CONTAINER_IMG:-"pkg.cerbos.dev/containers/cerbos"}
CONTAINER_TAG=${CONTAINER_TAG:-"0.0.1-rc2"}

docker run -i -t -p 9998:9998 \
  -v ${SCRIPT_DIR}/policy:/policy \
  -v ${SCRIPT_DIR}/config:/config \
  "${CONTAINER_IMG}:${CONTAINER_TAG}" \
  server --config=/config/conf.yaml


