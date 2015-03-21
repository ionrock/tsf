# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime
from argparse import ArgumentParser


__author__ = 'Eric Larson'
__email__ = 'eric@ionrock.org'
__version__ = '0.1.0'


def stamp(filename):
    return '%s-%s' % (
        datetime.now().strftime('%Y%m%d-%H%M%S'),
        filename
    )


def parse_args(args=None):
    p = ArgumentParser()
    p.add_argument('filename')
    p.add_argument('-d', '--use-dir', action='store_true', default=False)
    return p.parse_args(args)


def main():
    args = parse_args()

    fname = stamp(args.filename)

    if args.use_dir:
        dirname = os.path.abspath(args.filename)
        try:
            os.mkdir(dirname)
        except OSError:
            pass

        fname = os.path.join(dirname, fname)

    with open(fname, 'w+') as fh:
        for chunk in sys.stdin:
            fh.write(chunk)
