import pytest
from src.index import isPrime,PrimeNumbers
from unittest.mock import patch
import os

@pytest.mark.parametrize(
    "a, output",
    [
        (2, True),  # Test case 1
        (5, True),  # Test case 2
        (10, False),  # Test case 3
    ],
)
def test_is_Prime(a,output):
    assert isPrime(a)==output

@pytest.fixture
def mockIsPrime(mocker,isPrime):
    mocker.patch("src.index.isPrime", return_value =isPrime)

@pytest.mark.parametrize(
    "n,isPrime,output",
    [
        (3,(True,True),[2,3]),
        (5,(True,True,False,True),[2,3,5]),

    ]
)
@pytest.mark.usefixtures("mockIsPrime")
def test_Prime_Numbers(n,output):
    assert (PrimeNumbers(n)==output)



