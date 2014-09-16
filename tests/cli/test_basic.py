import sys
import subprocess

import pypi

def test_simple_invocation():
    subprocess.check_call(['pypi'])

def test_python_m_invocation():
    subprocess.check_call([sys.executable, '-m', 'pypi'])

def test_help_arg():
    out = subprocess.check_output(
            [sys.executable, '-m', 'pypi', '--help'],
            universal_newlines=True)
    assert 'usage' in out

def test_version_arg():
    out = subprocess.check_output(
            [sys.executable, '-m', 'pypi', '--version'],
            universal_newlines=True)
    assert pypi.__version__ in out
