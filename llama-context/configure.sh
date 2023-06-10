#!/bin/bash
set -eu pipefail

ROOTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
VENV="${ROOTDIR}/venv"
VPYTHON="${VENV}/bin/python3"

[ -d "${VENV}" ] || mkdir -p "${VENV}"

echo "Creating venv in '${VENV}' and installing packages..."
python3 -m venv "${VENV}"

base_packs="pip python-dotenv llama-index python-bidi"
for pack in ${base_packs}; do
    ${VPYTHON} -m pip install --upgrade "${pack}"
done

echo "Done!"
