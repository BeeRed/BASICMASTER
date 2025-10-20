#!/usr/bin/env python3
#
# require a filename(s) which is open for read and a
# hexdump and checksum per (line, block, total) is generated
#
# author: Heinz Blaettner 2025-10-20
#
#######################################
import sys
import binascii

# CONST
HEX_LINE_LEN    = 8
HEX_BLOCK_SIZE  = 0x80

### ###
def process_block(data, blk_offs, bsize, lsize=HEX_LINE_LEN):
    sum = 0
    todo_size = bsize
    for b_offs in range(0, bsize, lsize):
        blk_addr     = blk_offs + b_offs
        blk_addr_end = blk_addr + lsize
        lend = blk_addr_end if todo_size >= lsize else blk_addr + todo_size
        #print(f"${blk_addr:04X} {lend:04X} ", end="")
        print(f"${blk_addr:04X}  ", end="")
        for i in range(b_offs, b_offs + lsize):       # process one line
            try:        # if line is not long enough
                c = data[i]
            except Exception as e:
                print("Exception read data[{i}]");
                break   # we are done with the data
            sum       += c
            todo_size -= 1
            print(f"  {c:02X}", end="")
            if 0==todo_size:
                #print("todo_size==0");
                break   # we are done with the block
        print(f"      sum :${sum:04X}")
    print(f" SUM :${sum:04X}")
    return sum

### ###
def process_file(fname):
    print(f"# process_file({fname})");
    with open(fname, 'rb') as f:
        binary_data = f.read()

    blk_cnt = 0
    total_sum = 0
    binary_data_len = len(binary_data)
    todo_len = binary_data_len
    for blk_offs in range(0, binary_data_len, HEX_BLOCK_SIZE):
        slice_start = blk_offs
        slice_end   = slice_start + HEX_BLOCK_SIZE
        slice_data  = binary_data[slice_start:slice_end]
        blk_cnt    += 1
        blk_len     = HEX_BLOCK_SIZE if todo_len >= HEX_BLOCK_SIZE else todo_len
        print(f"XXXX NO.{blk_cnt: 2} XXXX size:${blk_len:02X}");
        todo_len -= blk_len
        total_sum += process_block(slice_data, blk_offs, blk_len, HEX_LINE_LEN)
        total_sum &= 0xffff
        #print(f"{blk_offs:04x}: ")

    print(f"\nTOTAL CHECK SUM :${total_sum:04X}")
#       for chunk in iter(lambda: f.read(16), b''):
#           print(f"{blk_offs}")
#           # print(codecs.encode(chunk, 'hex'))
#           print(binascii.hexlify(chunk, ' '))

### ###
def main(argv):
    prg_name = argv[0]
    args = argv[1:]
    argc = len(args)
    print(f"# {prg_name}(#{argc})");

    for arg in args:
        process_file( arg )

### ###
if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print('Caught main exception:',e)
    sys.exit(0)

