#!/bin/bash
set -eu pipefail

ROOTDIR="$(pwd)"
VENV="${ROOTDIR}/venv"
DEPSFILE="${ROOTDIR}/pydeps.txt"
VPYTHON="${VENV}/bin/python3"

[ -d "${VENV}" ] || mkdir -p "${VENV}"

echo "Creating venv in '${VENV}' and installing packages..."
python3 -m venv "${VENV}"

${VPYTHON} -m pip install --upgrade pip
${VPYTHON} -m pip install -r "${DEPSFILE}"

echo "Done!"
