from hexlet_pytest.reverse import reverse

def test_reverse():
    assert reverse('AbCdEf') == 'fEdCbA'
    assert reverse('') == ''
    assert reverse('Hello, World!') == '!dlroW ,olleH' 
