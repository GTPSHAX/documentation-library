---
title: std::exclusive_scan
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/exclusive_scan
---


```cpp
**Header:** `<`numeric`>`
|
template< class InputIt, class OutputIt, class T >
OutputIt exclusive_scan( InputIt first, InputIt last,
OutputIt d_first, T init );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class T >
ForwardIt2 exclusive_scan( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, T init );
|
template< class InputIt, class OutputIt,
class T, class BinaryOp >
OutputIt exclusive_scan( InputIt first, InputIt last,
OutputIt d_first, T init, BinaryOp op );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class T, class BinaryOp >
ForwardIt2 exclusive_scan( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, T init, BinaryOp op );
```

1. Equivalent to `exclusive_scan(first, last, d_first, init, std::plus<>()`.
3. Computes the exclusive prefix sum using `op`.
@@ For each integer `i` in [0, std::distance(first, last)), performs the following operations in order:
# Creates a sequence which is formed by `init` followed by the elements of [first, iter) in order, where `iter` is the next `i` iterator of `first`.
# Computes the generalized noncommutative sum of the sequence over `op`.
# Assigns the result to `*dest`, where `dest` is the next `i` iterator of `d_first`.
@2,4@ Same as , but executed according to `policy`.
@@
The ''generalized noncommutative sum'' of a sequence of elements over a binary operation `binary_op` is defined as follows:
* If the sequence only has one element, the sum is the value of the element.
* Otherwise, performs the following operations in order:
# Selects any two adjacent elements `elem1` and `elem2` from the sequence.
# Calculates `binary_op(elem1, elem2)` and replaces the two elements in the sequence with the result.
# Repeats steps 1 and 2 until there is only one element in the sequence.
Given `binary_op` as the actual binary operation:
* The result is non-deterministic if the `binary_op` is not associative (such as floating-point addition).
* If any of the following values is not convertible to `T`, the program is ill-formed:
:* `binary_op(init, *first)`
:* `binary_op(init, init)`
:* `binary_op(*first, *first)`
* If any of the following conditions is satisfied, the behavior is undefined:
:* `T` is not *MoveConstructible*.
:* `binary_op` modifies any element of [first, last).
:* `binary_op` invalidates any iterator or subrange of .

## Parameters


### Parameters

- `d_first` - the beginning of the destination range; may be equal to `first`
- `policy` - execution policy
- `init` - the initial value
- `op` - binary *FunctionObject* that will be applied in to the result of dereferencing the input iterators, the results of other `op`, and `init`

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`

## Return value

Iterator to the element past the last element written.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@  applications of `std::plus<>()`.
@3,4@  applications of `op`.

## Exceptions


## Example


## See also


| cpp/algorithm/dsc adjacent_difference | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc partial_sum | (see dedicated page) |
| cpp/algorithm/dsc transform_exclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc inclusive_scan | (see dedicated page) |

