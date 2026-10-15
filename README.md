# Predicting Software Execution Time Using Code Complexity Metrics

## 1. Main Idea of the Project

The main idea is to **use machine learning to estimate how long a program will take to execute before actually running it**, based on measurable characteristics of its source code.

Normally, developers run a program and measure its execution time to find out how fast or slow it is. This project explores whether a machine learning model can estimate that time using information about the code.

For example, a developer writes a program with 150 lines of code and a cyclomatic complexity of 12. A trained model could use those measurements, along with other relevant features, to estimate the program's runtime.

The estimate is not guaranteed to be correct. Its usefulness depends on the quality of the dataset, the features used, and how similar the new program is to the training examples.

**Main research question:** Can Linear Regression predict software execution time reasonably well using code complexity metrics?

### How the project works

1. **Input:** Provide source code and extract features such as lines of code, cyclomatic complexity, and possibly input size or algorithmic complexity.
2. **Training:** Train a Linear Regression model on examples with known, measured execution times.
3. **Prediction:** Give the model features from a new program so it can estimate its runtime.
4. **Evaluation:** Compare predictions with actual runtimes for programs the model did not train on.

---

## 2. Why Is This Project Important?

The project investigates whether runtime predictions could help developers make better decisions before spending time running and testing programs.

### 1. Early performance estimation
Developers could get an initial estimate of runtime before executing a program, helping them identify code that may deserve closer performance testing.

### 2. Performance optimization
If the model flags a program as potentially slow, developers can investigate its algorithms, loops, and data processing to find possible bottlenecks.

### 3. Resource planning
Runtime estimates may help with preliminary planning for batch jobs or other workloads. Reliable resource planning also requires information about hardware, memory, and workload size.

### 4. Data-driven software engineering
Instead of relying entirely on intuition, developers can use measured data and prediction errors to evaluate whether code metrics are useful for estimating performance.

**Important limitation:** The model does not automatically make code faster, identify every bottleneck, or eliminate the need for testing. Its purpose is to provide an estimate that may support development decisions.

---

## 3. Time Complexity

### Definition

**Time complexity describes how the amount of computational work an algorithm performs grows as the size of its input increases.**

It is usually expressed using Big-O notation, such as `O(1)`, `O(n)`, or `O(n²)`.

Time complexity does not directly measure seconds. Instead, it describes the growth rate of an algorithm's workload as the input gets larger.

### Example: `O(n)`

```python
def find_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
```

The function processes every number in the input list once.

- If the list has 10 elements, it processes 10 elements.
- If the list has 100 elements, it processes 100 elements.
- If the list has 1,000 elements, it processes 1,000 elements.

The work grows approximately in proportion to the input size `n`. Therefore, its time complexity is **`O(n)`**, or linear time.

### Common time complexities

| Big-O notation | Meaning | Example |
|---|---|---|
| `O(1)` | Constant growth | Accessing an array element by index |
| `O(log n)` | Logarithmic growth | Binary search in a sorted array |
| `O(n)` | Linear growth | Traversing a list once |
| `O(n log n)` | Linearithmic growth | Typical merge sort |
| `O(n²)` | Quadratic growth | Comparing every pair of elements in a list |

### Why time complexity matters

Time complexity helps explain how an algorithm scales as its input grows. For example, an `O(n²)` algorithm may become much slower on large inputs than a suitable `O(n log n)` algorithm.

However, knowing an algorithm's Big-O complexity without knowing the input size is not enough to estimate its runtime reliably. Determining an algorithm's Big-O complexity may also require analyzing its logic or using additional tools.

---

## 4. Cyclomatic Complexity

### Definition

**Cyclomatic complexity measures the number of linearly independent paths through a program's control flow.**

In simpler terms, it measures how many different logical routes a program can take because of its decisions.

### Example

```python
if score >= 75:
    print("Passed")
else:
    print("Failed")
```

There is one decision: `score >= 75`. The program has two possible paths:

- The condition is true, so it prints `Passed`.
- The condition is false, so it prints `Failed`.

For a simple, connected control-flow graph, a basic formula is:

`M = D + 1`

Where:

- `M` is cyclomatic complexity.
- `D` is the number of decision points.

For this example:

`M = 1 + 1 = 2`

The cyclomatic complexity is **2** because there are two independent paths.

For more complex control flow, a standard graph-based formula is:

`M = E - N + 2P`

Where:

- `E` = number of control-flow edges.
- `N` = number of nodes.
- `P` = number of connected components.

For a single connected function, `P = 1`.

### Example with higher complexity

```python
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Passed")
elif score >= 50:
    print("Remedial")
else:
    print("Failed")
```

Under the basic decision-point counting convention, there are three decision points, so the cyclomatic complexity is `3 + 1 = 4`.

Higher cyclomatic complexity generally means more independent paths to consider during testing and maintenance. It can make code more difficult to test and understand.

**Important:** Higher cyclomatic complexity does not necessarily mean longer execution time. A program with many branches might run quickly, while a simple loop might process millions of elements and take much longer.

### Why cyclomatic complexity matters

It provides a numerical description of a program's logical structure that can be used as a potential machine learning feature. The experiment should determine whether this metric actually improves runtime predictions.

---

## 5. Why Is Predicting Execution Time Important?

Imagine two programs:

- **Program A:** Low cyclomatic complexity, but it processes millions of records using an inefficient algorithm.
- **Program B:** Higher cyclomatic complexity, but it uses an efficient algorithm and processes only a small input.

You cannot confidently say which one will finish first just by looking at cyclomatic complexity or lines of code.

The model attempts to learn relationships from previous examples where actual runtime is known. When it receives a new program's features, it estimates the runtime based on what it has learned.

The prediction lets you investigate these questions:

1. Can code metrics provide useful information about execution time?
2. How accurate are the model's predictions on programs it has never seen?
3. Which features contribute to better predictions, and which are insufficient on their own?

This makes the project a testable machine learning study rather than just a tool that reports code complexity.

---

## 6. How the Concepts Fit Together

| Component | Role in the project |
|---|---|
| Lines of code | Measures program size |
| Cyclomatic complexity | Describes independent control-flow paths |
| Time complexity | Describes how computational work scales with input size |
| Actual execution time | The measured value used as the training target |
| Linear Regression | Learns a relationship between numerical features and runtime |
| MAE, RMSE, and R² | Help evaluate prediction quality |

### Linear Regression in this project

Linear Regression learns a relationship between input features and a numerical target. A simplified equation is:

`Predicted time = b0 + b1 × LOC + b2 × Cyclomatic Complexity`

Where:

- `LOC` is lines of code.
- `b0`, `b1`, and `b2` are coefficients learned during training.

The real model can use additional features, such as input size, if reliable values are available.

### Training and testing

- **Training data:** Examples the model uses to learn relationships between features and runtime.
- **Testing data:** Separate examples used to evaluate how well the model predicts unseen programs.

For example, you might use 80% of the data for training and 20% for testing. The split should be designed to avoid information leakage between training and test examples.

### Evaluation metrics

| Metric | What it tells you |
|---|---|
| MAE | The average absolute difference between predicted and actual runtime |
| RMSE | Prediction error that penalizes large mistakes more heavily |
| R² | How well the model explains variation in observed runtimes relative to a mean-based baseline |

An MAE of `0.02` seconds means the average absolute prediction error is 0.02 seconds on the evaluated examples. R² can be negative if the model performs worse than predicting the test-set mean.

---

## 7. Important Limitations

Code complexity does not equal execution time. Runtime can also be affected by:

- **Algorithm efficiency:** A short program using an inefficient algorithm can be slower than a longer program using an efficient one.
- **Input size:** Processing 10 items differs from processing 10 million items.
- **Hardware:** The same program can run at different speeds on different computers.
- **Runtime environment:** Programming language, compiler, libraries, and system load can affect performance.
- **Loops and recursion:** The number of iterations and stopping conditions can matter more than the number of lines of code.

For a fair experiment, measure runtimes under consistent conditions. Consider adding relevant features such as input size or algorithmic complexity if you can determine them reliably.

Avoid claiming that the model can predict the runtime of *any* program. A more defensible claim is that it estimates runtime for programs similar to those represented in the training data and under comparable measurement conditions.

### Important dataset requirement

The proposed source is [Facebook's BigOBench dataset on Hugging Face](https://huggingface.co/datasets/facebook/BigOBench).