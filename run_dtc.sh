#/usr/bin/env bash

dtc -I dts -O dtb --out-version 17 -o manifest.dtb manifest.dts

echo "Expected:"
diff <(hexdump manifest.dtb) expected.hexdump

echo
echo "Actual:"
diff <(hexdump manifest.dtb) actual.hexdump
