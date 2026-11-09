import json,sys,unittest
sys.path.insert(0,sys.argv[1])
suite=unittest.defaultTestLoader.discover(sys.argv[1],pattern='tests_submission.py')
result=unittest.TextTestRunner(verbosity=1).run(suite)
print('TEST_RESULT '+json.dumps(dict(run=result.testsRun,failures=len(result.failures),errors=len(result.errors),skipped=len(result.skipped),expected=len(result.expectedFailures),unexpected=len(result.unexpectedSuccesses))))
