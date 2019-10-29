from functools import wraps

def tags(tag_list):
    def _wapper(func):
        _wapper.__dict__['tags'] = tag_list
        @wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    print(_wapper.__dict__)
    return _wapper


if __name__ == '__main__':
    import unittest
    class Base(unittest.TestCase):
        tags = 'abc'
    class TestA(Base):
        @tags(['a','b'])
        def test_a(self):
            pass

    suite = unittest.TestSuite()
    suite.addTest(TestA('test_a'))
    for case in suite:
        print(case.__getattribute__('test_a').__dict__)