#!/bin/bash

SCRIPT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
OUTPUT_DIR="${SCRIPT_DIR}/out"

function parse_args() {
  local OPTIND
  while getopts 'hxS:D:C:M:G:T:E:' opt; do
    case "${opt}" in
      h)
        show_usage
        ;;
      x)
        set -x
        ;;
      S)
        SOLVER="${OPTARG}"
        ;;
      D)
        DATABASE="${OPTARG}"
        ;;
      C)
        COLLECTION="${OPTARG}"
        ;;
      M)
        MESH="${OPTARG}"
        ;;
      G)
        MESH_TYPE="${OPTARG}"
        ;;
      T)
        EXECUTION_TIME="${OPTARG}"
        ;;
      E)
        EXP_NAME="${OPTARG}"
        ;;
      \?)
        echo "[ERROR]: Invalid option: -${opt}"
        show_usage
        exit 1;
        ;;
    esac
  done
  shift "$((OPTIND-1))"
}

function show_usage() {
  echo "${0} [-h] [-x] -S <SOLVER>"
}

function main() {
    parse_args "${@}"
    # put blockmesh logs to log file
    BlockMesh > "${OUTPUT_DIR}/blockmesh.log"

    # execute solver and put logs to file
    "${SOLVER}" > "${OUTPUT_DIR}/solver.log"

    python ../python/main.py -d "${DATABASE}" -c "${COLLECTION}" -f "${OUTPUT_DIR}/blockmesh.log" -m "${MESH}" --type "${MESH_TYPE}" -t "${EXECUTION_TIME}" -e "${EXP_NAME}"
    python ../python/main.py -d "${DATABASE}" -c "${COLLECTION}" -f "${OUTPUT_DIR}/solver.log" -m "${MESH}" --type "${MESH_TYPE}" -t "${EXECUTION_TIME}" -e "${EXP_NAME}"
}

main "${@}"
