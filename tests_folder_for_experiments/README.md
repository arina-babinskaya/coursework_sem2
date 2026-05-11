# Tenrek C++ test files

Suggested checks:

```bash
tenrek file 01_simple_green.cpp
tenrek file 02_cyclomatic_yellow_red.cpp
tenrek file 03_deep_nesting.cpp
tenrek file 04_long_lines.cpp
tenrek file 05_god_class.cpp
tenrek file 06_lcom_candidate.cpp
tenrek file 07_methods_and_args.cpp

tenrek folder . --exclude "08_exclude_me.cpp"
tenrek metrics
tenrek metrics cyclomatic
```

Expected purpose:

- 01_simple_green.cpp: mostly green baseline
- 02_cyclomatic_yellow_red.cpp: high cyclomatic/cognitive complexity
- 03_deep_nesting.cpp: nesting threshold check
- 04_long_lines.cpp: longest_string and average_string_lenght check
- 05_god_class.cpp: god_class = methods + fields for one class
- 06_lcom_candidate.cpp: cohesion / LCOM checks
- 07_methods_and_args.cpp: methods, args_count, cyclomatic for methods
- 08_exclude_me.cpp: folder exclude test
```

Note: exact metric values may differ depending on your implementation of each metric.
```
