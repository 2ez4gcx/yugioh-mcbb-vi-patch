#!/usr/bin/env python3
"""Ap ban va PPF3 len dia goc, co kiem sha256 truoc va sau.

Chay:  python apply_patch.py <dia_goc.bin> <ban_va.ppf> <dia_ra.bin>
Khong can cai them gi ngoai Python 3.  Khong sua dia goc.
"""
import hashlib
import os
import struct
import sys

# sha256 cua dia goc va cua dia dich - doc tu README de doi chieu
SHA_GOC = '51c38225b7e6e4af01f45aa3dd6209412ffb19c1f8569b667d038aca1141a355'
SHA_DICH = {
    '68d403c2cc34d339d93cc5a9851733792ae5462405b3cbfe9797eefbc127ff5d': 'ban tieng Viet',
    '40450f2d479c4e6197b470128181d80f532b0a8542e21ed614b5407660b99176': 'tieng Viet + mod CPU +25%',
    'b858d3a0418d1ee85ea8d08f9e1d47d919b2d0da80c5c30fae5c5c7ca1597b5d': 'tieng Viet + mod CPU +50%',
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def viet_cue(dst):
    """Tao file .cue canh file .bin vua ra (dia 1 track, Mode2/2352)."""
    cue = os.path.splitext(dst)[0] + '.cue'
    dong = ['FILE "%s" BINARY' % os.path.basename(dst),
            '  TRACK 01 MODE2/2352',
            '    INDEX 01 00:00:00']
    with open(cue, 'wb') as f:
        f.write(('\r\n'.join(dong) + '\r\n').encode('utf-8'))
    return cue


def main(src, ppf, dst):
    data = bytearray(open(src, 'rb').read())
    if SHA_GOC and sha(data) != SHA_GOC:
        sys.exit('Dia goc khong dung (sha256 khong khop). Can dung ban .bin Mode2/2352 cua SLPM-86096.')
    p = open(ppf, 'rb').read()
    if p[:5] != b'PPF30' or p[5] != 2:
        sys.exit('Khong phai file PPF3.')
    # dau PPF3: 56 imagetype, 57 blockcheck, 58 undo, 59 dummy; ban ghi tu 60
    # (co them 1024 byte khoi kiem neu bat blockcheck) - dung chuan PPF-O-Matic
    undo = p[58]
    pos, n = 60 + (1024 if p[57] else 0), 0
    while pos < len(p):
        off = struct.unpack_from('<Q', p, pos)[0]
        ln = p[pos + 8]
        pos += 9
        data[off:off + ln] = p[pos:pos + ln]
        pos += ln + (ln if undo else 0)
        n += 1
    open(dst, 'wb').write(data)
    print('da tao %s' % viet_cue(dst))
    h = sha(data)
    print('da ap %d ban ghi -> %s' % (n, dst))
    print('sha256 dia ra: %s' % h)
    if SHA_DICH:
        print('KHOP ban phat hanh: %s' % SHA_DICH[h] if h in SHA_DICH
              else 'KHONG KHOP - dia goc co the khac ban chuan')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
