import pytest

def sum(n):
    return n*(n+1)/2
def test_sum():
    assert sum(5)==15
def fact(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
def test_fact():
    assert fact(2)==2
def printnum(n):
    x=0
    y=0
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
            y=y+1
    return y
def test_printnum():
    assert printnum(5)==2