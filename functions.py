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

def srm_to_ves(inputves, inputsrm):
    f = open(inputves, 'r+')
    header = mmap.mmap(f.fileno(), 0)
    header = bytearray(bytearray(header))
    header = header[0:48]
    f.close()

    f = open(inputsrm, 'r+')
    m = mmap.mmap(f.fileno(), 0)
    f.close()

    base = os.path.basename(inputves)
    outputf = os.path.splitext(base)[0] + '.ves'
    f = open(outputf, 'wb')
    f.write(header + m)
    f.close()
    return outputf
    pass