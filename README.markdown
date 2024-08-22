# Tests

To run tests for a file in specific:


```
python3 -m unittest discover  -p 'test*linear*.py'
```

The above run for the `test/test_1_linear_search.py`.

With Neotest you can use `:lua require('neotest').watch.toggle()` to watch
a test file that will run each time you save the source/test file.

More info [here](https://github.com/nvim-neotest/neotest#watch-tests).
