from mypackage import myModule

def test_top_n(n):
    """
    make sure top_n works properly

    """

    assert myModule.top_n([7, 2, 9, 42, 48, 59, 30]) == [59, 48, 42], "incorrect"