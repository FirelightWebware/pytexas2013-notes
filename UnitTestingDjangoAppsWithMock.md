# Title: Unit Testing Django Apps with Mock
_Speaker: Jeremy Boyd_

github.com/boydjj
@jeremyboyd

Unit tests are tests of independent bits of logic -- strong bias against dependence on external resources.

## patch

`patch` replaces your target object with _something_

    from mock import patch
    
    def mock_sum(*args):
        return 42
        
    with patch('__builtin__.sum', mock_sum):
        print sum(1,2,3)
        print sum()
        print sum(1)
        
    outputs
    42
    42
    42
    
## magicmock

A mock is an object that 'has' every attribute, as well as some extra attributes for asking the mock questions.

A magicmock is just a mock with all the 'magic' methods predefined and ready to go.

## testing views

Focus on writing tests that never touch the database.

* don't use the TestCase client (it uses the database) - but you can use SimpleTestCase
* Django provides RequestFactory to generate requests that can be passed to views
* [see repo for code]

patch where it's being used, not where the test is being used 

nest calls to patch when you need to patch more than one thing (that seems silly). there's a better way with starting patches in your setUp and stopping them in your tearDown

patch the method that reads the db directly (not the object or the manager)

or just use github dcramer/mock-django

if you are patching a whole bunch of stuff, you probably need a functional test instead -- but check to see if you need to simplify your code

see full example at: https://github.com/boydjj/mocking_django

if you create your unit tests so they never touch the db (and with the test runner in the repo above… without even the ability to hit a db) you will run them fast and more often.