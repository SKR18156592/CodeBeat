# CodeBeat

**CodeBeat** is a line-by-line Python function tracer for debugging and performance analysis. It measures execution time per line across multiple runs, showing mean and standard deviation to identify bottlenecks in loops, branches, math operations, and list comprehensions.

## Features
- Tracks individual line execution times with statistical summaries (mean/std in ms).
- Handles nested loops, conditionals, math functions, and dynamic list operations.
- Runs functions multiple times (e.g., 10-12 iterations) for reliable profiling.
- Displays formatted tables with line numbers, code, and timing metrics.

## Installation
1. Clone the repo: `git clone https://github.com/SKR18156592/CodeBeat.git`
2. Install: `pip install -r requirements.txt` (assumes `codebeat` as package).
3. Import: `from codebeat import code_tracker`

## Quick Start
```python
from codebeat import code_tracker

def fun1(x, y):
    m = 0
    for i in range(x):
        for j in range(y):
            m += i*j
    return m

obj = code_tracker(fun1, 12)  # Optional iteration count
result = obj(3, 4)  # Executes 12x, prints timing table
```
**Sample Output:**
```
===========================================================================================
|> Function Name: fun1, #iter:12, mean_time(in ms):0.031, std_time(in ms):0.066
===========================================================================================
| line No | Line               | mean_time(in ms) | std_time(in ms)
===========================================================================================
| 0       | m = 0              | 0.000            | 0.000
| 1       | for i in range(x): | 0.012            | 0.021
| 2       | for j in range(y): | 0.008            | 0.021
| 3       | m += i*j           | 0.007            | 0.020
| 4       | return m           | nan              | nan
-------------------------------------------------------------------------------------------
```
Reveals nested loop overhead—outer loop takes ~50% more time than inner.

## Examples
- **Matrix Sum**: Compares outer vs inner loop costs.
- **Branch Counter**: Highlights expensive `else` branches.
- **Math Series**: Trig/exp functions add measurable latency.
- **List Builder**: `append()` dominates micro-benchmarks.

## Project Structure
```
CodeBeat/
├── codebeat/
│   └── __init__.py     # code_tracker class
├── example.ipynb       # Demos above
├── README.md
└── requirements.txt
``` 

## License
MIT