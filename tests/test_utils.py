from app.utils import add
 
def test_add_success():
    assert add(2, 3) == 5  # Pass
 
def test_add_failure():
    assert add(2, 2) == 5  #  Fail intentionally