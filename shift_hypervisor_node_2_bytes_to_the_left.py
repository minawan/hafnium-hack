from pyfdt.pyfdt import FdtBlobParse
import sys

NODE_HYPERVISOR = b'hypervisor'
DIRECTION_LEFT = -1
DIRECTION_RIGHT = 1

def shift_node_by_n_bytes(dtb, node, nnn):
  node_offset = dtb.find(node) - 2
  node_length = len(node)
  return dtb[:node_offset + nnn] + dtb[node_offset:node_offset + node_length + 76] + (-1 * nnn) * b'\000' + dtb[node_offset + node_length + 76:]

with open(sys.argv[1], 'rb') as input_device_tree_binary_file:
    input_device_tree_binary = FdtBlobParse(input_device_tree_binary_file).to_fdt().to_dtb()
output_device_tree_binary = shift_node_by_n_bytes(input_device_tree_binary, NODE_HYPERVISOR, DIRECTION_LEFT * 2)

with open(sys.argv[2], 'wb') as output_device_tree_binary_file:
    output_device_tree_binary_file.write(output_device_tree_binary)
