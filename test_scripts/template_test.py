from test_runner.test_runner import TestRunner


class TemplateTest(TestRunner):

    def __init__(self):
        super(TemplateTest, self).__init__()

    def initialize(self):
        super(TemplateTest, self).initialize()

    def test(self):
        pass


def main():
    test = TemplateTest()
    test.run_test()


if __name__ == "__main__":
    main()
