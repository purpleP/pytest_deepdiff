import pytest
from deepdiff import DeepDiff as diff
import pprint


def pytest_assertrepr_compare(op, left, right):
    if op == "==":
        return pprint.pformat(diff(left, right), indent=4).split('\n')
