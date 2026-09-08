#!/usr/bin/env python3
"""Ap ban va PPF3 len dia goc, co kiem sha256 truoc va sau.

Chay:  python apply_patch.py <dia_goc.bin> <ban_va.ppf> <dia_ra.bin>
Khong can cai them gi ngoai Python 3.  Khong sua dia goc.
"""
import hashlib
import struct
import sys

# sha256 cua dia goc va cua dia dich - doc tu README de doi chieu
SHA_GOC = '51c38225b7e6e4af01f45aa3dd6209412ffb19c1f8569b667d038aca1141a355'
SHA_DICH = '9fd03ed2a3cd5661de41faa36388a38104411a36ab3754d383f27da212657830'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main(src, ppf, dst):
    data = bytearray(open(src, 'rb').read())
    if SHA_GOC and sha(data) != SHA_GOC:
        sys.exit('Dia goc khong dung (sha256 khong khop). Can dung ban .bin Mode2/2352 cua SLPM-86096.')
    p = open(ppf, 'rb').read()
    if p[:5] != b'PPF30' or p[5] != 2:
        sys.exit('Khong phai file PPF3.')
    undo = p[58]
    pos, n = 59, 0
    while pos < len(p):
        off = struct.unpack_from('<Q', p, pos)[0]
        ln = p[pos + 8]
        pos += 9
        data[off:off + ln] = p[pos:pos + ln]
        pos += ln + (ln if undo else 0)
        n += 1
    open(dst, 'wb').write(data)
    h = sha(data)
    print('da ap %d ban ghi -> %s' % (n, dst))
    print('sha256 dia ra: %s' % h)
    if SHA_DICH:
        print('KHOP ban phat hanh' if h == SHA_DICH else 'KHONG KHOP - dia goc co the khac ban chuan')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
