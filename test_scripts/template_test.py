from test_runner.test_runner import TestRunner

class TemplateTest(TestRunner):

    def __init__(self):
        super(TemplateTest, self).__init__()

    def initialiaze(self):
        super(TemplateTest, self).initialiaze()

    def test(self):
        pass

def main():
    test = TemplateTest()
    test.run_test()

if __name__ == "__main__":
    main()