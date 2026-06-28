---
title: std::shift_left
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/shift
---


```cpp
**Header:** `<`algorithm`>`
dcl|num=1|since=c++20|1=
template< class ForwardIt >
constexpr ForwardIt shift_left( ForwardIt first, ForwardIt last,
typename std::iterator_traits<ForwardIt>::
difference_type n );
dcl|num=2|since=c++20|1=
template< class ExecutionPolicy, class ForwardIt >
ForwardIt shift_left( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
typename std::iterator_traits<ForwardIt>::
difference_type n );
dcl|num=3|since=c++20|1=
template< class ForwardIt >
constexpr ForwardIt shift_right( ForwardIt first, ForwardIt last,
typename std::iterator_traits<ForwardIt>::
difference_type n );
dcl|num=4|since=c++20|1=
template< class ExecutionPolicy, class ForwardIt >
ForwardIt shift_right( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last,
typename std::iterator_traits<ForwardIt>::
difference_type n );
```

Shifts the elements in the range [first, last) by `n` positions.
1. Shifts the elements towards the beginning of the range.
* If `1=n == 0 , there are no effects.
* Otherwise, for every integer `i` in [0, last - first - n), moves the element originally at position `first + n + i` to position `first + i`.
@@ The moves are performed in increasing order of `i` starting from `0`.
3. Shifts the elements towards the end of the range.
* If `1=n == 0 , there are no effects.
* Otherwise, for every integer `i` in [0, last - first - n), moves the element originally at position `first + i` to position `first + n + i`.
@@ If `ForwardIt` meets the *BidirectionalIterator* requirements, then the moves are performed in decreasing order of `i` starting from `last - first - n - 1`.
@2,4@ Same as  and , respectively, but executed according to `policy` and the moves may be performed in any order.
@@ .
Elements that are in the original range but not the new range are left in a valid but unspecified state.
If any of the following conditions is satisfied, the behavior is undefined:
* `1=n >= 0` is not `true`.
* The type of `*first` is not *MoveAssignable*.
* For `shift_right`, `ForwardIt` is neither *BidirectionalIterator* nor *ValueSwappable*.

## Parameters


### Parameters

- `n` - the number of positions to shift
- `policy` - execution policy

**Type requirements:**

- `ForwardIt`

## Return value

@1,2@ The end of the resulting range.
* If `n` is less than `std::distance(first, last)`, returns an iterator equal to `std::next(first, (std::distance(first, last) - n))`.
* Otherwise, returns `first`.
@3,4@ The beginning of the resulting range.
* If `n` is less than `std::distance(first, last)`, returns an iterator equal to `std::next(first, n)`.
* Otherwise, returns `last`.

## Complexity

@1,2@ At most `std::distance(first, last) - n` assignments.
@3,4@ At most `std::distance(first, last) - n` assignment or swaps.

## Exceptions


## Notes


## Example


### Example


**Output:**
```
vector<S>       vector<int>     vector<string>
1 2 3 4 5 6 7   1 2 3 4 5 6 7   α β γ δ ε ζ η
4 5 6 7 . . .   4 5 6 7 5 6 7   δ ε ζ η . . .
. . 4 5 6 7 .   4 5 4 5 6 7 5   . . δ ε ζ η .
. . 4 5 6 7 .   4 5 4 5 6 7 5   . . δ ε ζ η .
```


## See also


| cpp/algorithm/dsc move | (see dedicated page) |
| cpp/algorithm/dsc move_backward | (see dedicated page) |
| cpp/algorithm/dsc rotate | (see dedicated page) |
| cpp/algorithm/ranges/dsc shift | (see dedicated page) |

