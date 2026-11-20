#!/bin/bash
# GP & GP draft build (cloud container). Usage: bash _src/make.sh [domain]
set -e; cd "$(dirname "$0")/.."; T=${ADVON:-/mnt/user-data/uploads/ADVON-CLIENTS/.advon}; D=$(pwd)
python3 _src/build.py
python3 $T/favicon.py make "$D" assets/img/gp-and-gp-icon.svg --tile none >/dev/null
(cd $T && python3 seo_live.py fix "$D" $1 && python3 seo_rank.py en "$D" $1 && python3 ai_seo.py fix "$D" $1)
