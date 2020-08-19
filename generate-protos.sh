#!/usr/bin/env bash

# set -ex
# PROTOC_VERSION="$(protoc --version)"
# if [[ "$PROTOC_VERSION" != 'libprotoc 3.6.0' && "$PROTOC_VERSION" != 'libprotoc 3.6.1' ]]; then
#     echo "Required libprotoc versions to be 3.6.0 or 3.6.1 (preferred)."
#     echo "We found: $PROTOC_VERSION"
#     exit 1
# fi

PROTOS="./protos"

protoc -I="$PROTOS" \
    --python_out="$PROTOS" \
    "$PROTOS/"*.proto


OLD_="import dataset_pb2 as dataset__pb2"
NEW_="from . import dataset_pb2 as dataset__pb2"
sed -i'.old' -e "s/$OLD_/$NEW_/g" "$PROTOS/dataset_version_pb2.py" "$PROTOS/pipeline_pb2.py"

rm "$PROTOS/dataset_version_pb2.py.old"
rm "$PROTOS/pipeline_pb2.py.old"

OLD_="import algos_pb2 as algos__pb2"
NEW_="from . import algos_pb2 as algos__pb2"
sed -i'.old' -e "s/$OLD_/$NEW_/g" "$PROTOS/pipeline_pb2.py"

rm "$PROTOS/pipeline_pb2.py.old"
