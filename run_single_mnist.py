#!/usr/bin/env python
from __future__ import print_function

import subprocess


def main():
    subprocess.run("mpiexec --allow-run-as-root -n 4 python examples/mnist/train_mnist.py", shell=True, check=True)

if __name__ == '__main__':
    main()
