#Django Extreme TDD

[![Build Status](https://drone.io/github.com/flaviamissi/django-extreme-tdd/status.png)](https://drone.io/github.com/flaviamissi/django-extreme-tdd/latest)

Django is an amazing framework to build websites, but it lacks the tools to aid a really important part of the
software development process: Test Driven Development.

##Django already supports testing, why this project?

Django has a list of test cases classes to use, and supports running tests much better than it used to,
but still, if you want to write a functional test that access the database, and you also want to leave
the database cleaning process to Django, the default TestCase class will take care of all that for you. But
not without a cost.

For the TDD process of writing tests, the cost added by the default TestCase is too high
to bare. Django's TestCase wraps every single test on a suite with a transaction, so every test has a clean
environment to be run in.

A clean environment for every test is indeed a good thing to have. If you don't cleanup your DB after your
tests, you'll endup with impredictable results, which we should avoid as much as we can on a testing environment.

The transaction wrapping solution that Django uses for cleanup is not good enough because it's **very** slow.
You can see it with your own eyes, use this steps to reproduce:

    - write a test that uses the database, do no cleanup by yourself and inherit from django.test.TestCase
    - run only the new test and write down the time spent (Django gives the time taken for the test to run without
    taking into account DB initial setup, you can use this value)
    - change your TestCase class from Django to unittest.TestCase.
    - perform all cleanup needed (consider using setUpClass/tearDownClass here and use'em if you can)
    - run the modified test again and compare the time spent before and after using unittest.TestCase

TODO: actually perform the above steps and show results (results must be reproducible)

You now know why we need a better cleanup solution.

##Why don't we do the cleanup on our own TestCase implementation?

One could simply extend unittest.TestCase and add an attribute to keep all objects
that were added on a test case and remove then manually, one by one, right?

Yes, this is one way to fix the problem, but if you really think about it, will that be much faster
than what Django's TestCase does? Maybe. If it is considerably faster, you may find yourself with
your database dirty anyways. This solution won't care for deleting objects in cascade, it will only
work if the object you created have an FK to another object, but if the opposite is true, you will not
be able to do the cleanup properly.

We could still improving this imaginary solution and eventually make it work, but I don't think it's worth the
effort. Why?

##Leave database cleanup to the database

And that's why. Whatever we try to do programatically, the database can do way better with its own functionality.
This is the idea behing the TestCase implemented in this project.

extreme.TestCase is designed to perform cleanup at setUpClass/tearDownClass. This means that a test case inheriting
from extreme.TestCase will have a whole clean database for it to use.

But it also means that we don't cover cleanup for each single test. But it doesn't mean that we can't extend it.
If the need to cleanup before/after every test on a test case exists, extend extreme.TestCase and open a Pull Request!
Just call the same cleanup method we call on setUpClass/tearDownClass on setUp/tearDown instead! BAHM, problem solved.

##How does it work?

TODO
