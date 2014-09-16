import pypi
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=pypi.__version__)
    args = parser.parse_args()
