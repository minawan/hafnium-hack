#/usr/bin/env bash

dtc -I dts -O dtb --out-version 17 -o manifest.dtb manifest.dts
python3 shift_hypervisor_node_2_bytes_to_the_left.py manifest.dtb output.dtb

echo "Expected:"
diff <(hexdump output.dtb) expected.hexdump

echo
echo "Actual:"
diff <(hexdump manifest.dtb) actual.hexdump
