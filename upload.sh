#!/bin/sh

if [ "$#" -ne 1 ]; then
    echo "Please pass a new version number as first argument..."
    exit 1
fi

version=$1

sed -i "/  version/ s/='[^'][^']*'/='${version}'/" setup.py
package_name="scienv"

python setup.py sdist
twine upload dist/${package_name}-${version}.tar.gz --verbose
python setup.py clean
