import os
import mmap

def ves_to_srm(inputf):
    base = os.path.basename(inputf)
    f = open(inputf, 'a+')
    m = mmap.mmap(f.fileno(), 0)
    f.close()
    outputf = os.path.splitext(base)[0] + '.srm'
    f = open(outputf, 'wb')
    f.write(m[48:])
    f.close()
    return outputf

def srm_to_ves(inputf, gpid):
    f = open(inputf, 'r+')
    m = mmap.mmap(f.fileno(), 0)
    m = bytearray(bytes(47) + bytearray(m))
    m[0] = 1
    m[5] = int(gpid[0:2], 16)
    m[4] = int(gpid[2:], 16)
    m[16:23] = 193, 53, 134, 165, 101, 203, 148, 44
    checksum = str(hex(sum(m)))
    print(checksum)
    m[2] = int(checksum[-2:], 16) - 1
    m[3] = int(checksum[-4:-2], 16)
    f.close()
    outputf = gpid + '.ves'
    f = open(outputf, 'wb')
    f.write(m)
    f.close()
    return outputf