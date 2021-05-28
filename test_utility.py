import utility

'''
Unit tests for utility.py.
'''

# test put request using asdf as id. changes values to first=nice last=one
def test_request_assert():
    print("")

def test_content_assert():
    print("")

# test generate pass msg using num 1
def test_generate_pass_msg():
    assert utility.generate_pass_msg(1) == "Test 1 passed"

# test generate pass msg using num 1
def test_generate_error_msg():
    try:
        raise AssertionError("test error")
    except AssertionError as e:
        error = e

    assert utility.generate_error_msg(1, error) == "Test 1 test error"

