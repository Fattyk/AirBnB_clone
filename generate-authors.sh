#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

echo
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf > AUTHORS

