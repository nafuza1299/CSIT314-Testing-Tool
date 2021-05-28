import json

'''
Utility functions
'''


# function used to assert status code. raises an assertion error if fails.
def request_assert(res, code):
    try:
        assert int(res) == int(code)
    except:
        raise AssertionError("Status Code Error: " + str(res) + " " + str(code))
    

# function used to assert json content. raises an assertion error if fails.
def content_assert(input, output):
    #load output content
    get_Content = json.loads(output.content)

    #loop through the content body
    try:
        for key in input:
            output = get_Content[key]
            input = input[key]
            for i in input:
                input_data = input[i]
                output_data = output[i]
                assert str(input_data) == str(output_data)
    except:
        raise AssertionError("Content Error: \n" + str(input) + "\nAnd\n" + str(output))

# function used to generate test pass message
def generate_pass_msg(num):
    return "Test " + str(num) + " passed"

# function used to generate test error message
def generate_error_msg(num, error):
    return "Test " + str(num) + " " + str(error)

