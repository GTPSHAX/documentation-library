---
title: std::transform_exclusive_scan
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/transform_exclusive_scan
---


```cpp
**Header:** `<`numeric`>`
|
template< class InputIt, class OutputIt, class T,
class BinaryOp, class UnaryOp >
OutputIt transform_exclusive_scan
( InputIt first, InputIt last, OutputIt d_first, T init,
BinaryOp binary_op, UnaryOp unary_op );
dcl|since=c++17|num=2|1=
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class T,
class BinaryOp, class UnaryOp >
ForwardIt2 transform_exclusive_scan
( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last, ForwardIt2 d_first, T init,
BinaryOp binary_op, UnaryOp unary_op );
```

1. Computes the exclusive prefix sum using `op`.
@@ For each integer `i` in [0, std::distance(first, last)), performs the following operations in order:
# Creates a sequence which is formed by `init` followed by the values transformed from the elements of [first, iter) in order by `unary_op`, where `iter` is the next `i` iterator of `first`.
# Computes the generalized noncommutative sum of the sequence over `binary_op`.
# Assigns the result to `*dest`, where `dest` is the next `i` iterator of `d_first`.
2. Same as , but executed according to `policy`.
@@
The ''generalized noncommutative sum'' of a sequence of elements over a binary operation `binary_op` is defined as follows:
* If the sequence only has one element, the sum is the value of the element.
* Otherwise, performs the following operations in order:
# Selects any two adjacent elements `elem1` and `elem2` from the sequence.
# Calculates `binary_op(elem1, elem2)` and replaces the two elements in the sequence with the result.
# Repeats steps 1 and 2 until there is only one element in the sequence.
The result is non-deterministic if the `binary_op` is not associative (such as floating-point addition).
If any of the following values is not convertible to `T`, the program is ill-formed:
* `binary_op(init, init)`
* `binary_op(init, unary_op(*first))`
* `binary_op(unary_op(*first), unary_op(*first))`
If any of the following conditions is satisfied, the behavior is undefined:
* `T` is not *MoveConstructible*.
* `unary_op` or `binary_op` modifies any element of [first, last).
* `unary_op` or `binary_op` invalidates any iterator or subrange of .

## Parameters


### Parameters

- `d_first` - the beginning of the destination range, may be equal to `first`
- `policy` - execution policy
- `init` - the initial value
- `unary_op` - unary *FunctionObject* that will be applied to each element of the input range. The return type must be acceptable as input to `binary_op`.
- `binary_op` - binary *FunctionObject* that will be applied in to the result of `unary_op`, the results of other `binary_op`, and `init`.

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`

## Return value

Iterator to the element past the last element written.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@  applications of `unary_op` and `binary_op` respectively.

## Exceptions


## Notes

`unary_op` is never applied to `init`.

## Example


## See also


| cpp/algorithm/dsc partial_sum | (see dedicated page) |
| cpp/algorithm/dsc exclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc transform_inclusive_scan | (see dedicated page) |

