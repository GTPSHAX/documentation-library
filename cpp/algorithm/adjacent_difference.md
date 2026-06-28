---
title: std::adjacent_difference
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/adjacent_difference
---


```cpp
**Header:** `<`numeric`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt >
OutputIt adjacent_difference( InputIt first, InputIt last,
OutputIt d_first );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2 >
ForwardIt2 adjacent_difference( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt, class BinaryOp >
OutputIt adjacent_difference( InputIt first, InputIt last,
OutputIt d_first, BinaryOp op );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryOp >
ForwardIt2 adjacent_difference( ExecutionPolicy&& policy,
ForwardIt1 first, ForwardIt1 last,
ForwardIt2 d_first, BinaryOp op );
```

Let `T` be the value type of `decltype(first)`.
1. If [first, last) is empty, does nothing.
@@ Otherwise, performs the following operations in order:
# Creates an accumulator `acc` of type `T`, and initializes it with `*first`.
# Assigns `acc` to `*d_first`.
# For each iterator `iter` in [++first, last) in order, performs the following operations in order:
::@a@ Creates an object `val` of type `T`, and initializes it with `*iter`.
::@b@ Computes <sup>(until C++20)</sup> `val - acc`<sup>(since C++20)</sup> `val - std::move(acc)`.
::@c@ Assigns the result to `*++d_first`.
::@d@ <sup>(until C++20)</sup> Copy<sup>(since C++20)</sup> Move assigns from `val` to `acc`.
2. If [first, last) is empty, does nothing.
@@ Otherwise, performs the following operations in order:
# Assigns `*first` to `*d_first`.
# For each integer `i` in [1, std::distance(first, last)), performs the following operations in order:
::@a@ Computes `curr - prev`, where `curr` is the next `i` iterator of `first`, and `prev` is the next `i - 1` iterator of `first`.
::@b@ Assigns the result to `*dest`, where `dest` is the next `i` iterator of `d_first`.
3. Same as , but computes <sup>(until C++20)</sup> `op(val, acc)`<sup>(since C++20)</sup> `op(val, std::move(acc))` instead.
4. Same as , but computes `op(curr, prev)` instead.
Given `binary_op` as the actual binary operation:
* If any of the following conditions is satisfied, the program is ill-formed:
:* For overloads :
::* `T` is not constructible from `*first`.
::* `acc` is not writable to `d_first`.
::* The result of <sup>(until C++20)</sup> `binary_op(val, acc)`<sup>(since C++20)</sup> `binary_op(val, std::move(acc))` is not writable to `d_first`.
:* For overloads :
::* `*first` is not writable to `d_first`.
::* The result of `binary_op(*first, *first)` is not writable to `d_first`.
* Given `d_last` as the iterator to be returned, if any of the following conditions is satisfied, the behavior is undefined:
rrev|since=c++20|
:* For overloads , `T` is not *MoveAssignable*.
:* For overloads , [first, last) and [d_first, d_last) overlaps.
:* `binary_op` modifies any element of [first, last) or [d_first, d_last).
:* `binary_op` invalidates any iterator or subrange in  or .

## Parameters


### Parameters

- `d_first` - the beginning of the destination range
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `OutputIt`
- `ForwardIt1, ForwardIt2`

## Return value

Iterator to the element past the last element written, or `d_first` if [first, last) is empty.

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  applications of `operator-`.
@3,4@ Exactly  applications of the binary function `op`.

## Exceptions


## Possible implementation

eq impl
|title1=adjacent_difference (1)|ver1=1|1=
template<class InputIt, class OutputIt>
constexpr // since C++20
OutputIt adjacent_difference(InputIt first, InputIt last, OutputIt d_first)
{
if (first == last)
return d_first;
typedef typename std::iterator_traits<InputIt>::value_type value_t;
value_t acc = *first;
*d_first = acc;
while (++first != last)
{
value_t val = *first;
*++d_first = val - std::move(acc); // std::move since C++20
acc = std::move(val);
}
return ++d_first;
}
|title2=adjacent_difference (3)|ver2=3|2=
template<class InputIt, class OutputIt, class BinaryOp>
constexpr // since C++20
OutputIt adjacent_difference(InputIt first, InputIt last,
OutputIt d_first, BinaryOp op)
{
if (first == last)
return d_first;
typedef typename std::iterator_traits<InputIt>::value_type value_t;
value_t acc = *first;
*d_first = acc;
while (++first != last)
{
value_t val = *first;
*++d_first = op(val, std::move(acc)); // std::move since C++20
acc = std::move(val);
}
return ++d_first;
}

## Notes

`acc` was introduced because of the resolution of . The reason of using `acc` rather than directly calculating the differences is because the semantic of the latter is confusing if the following types mismatch:
* the value type of `InputIt`
* the writable type(s) of `OutputIt`
* the types of the parameters of `operator-` or `op`
* the return type of `operator-` or `op`
`acc` serves as the intermediate object to cache values of the iterated elements:
* its type is the value type of `InputIt`
* the value written to `d_first` (which is the return value of `operator-` or `op`) is assigned to it
* its value is passed to `operator-` or `op`

```cpp
char i_array[4] = {100, 100, 100, 100};
int  o_array[4];

// OK: performs conversions when needed
// 1. creates “acc” of type char (the value type)
// 2. “acc” is assigned to the first element of “o_array”
// 3. the char arguments are used for long multiplication (char -> long)
// 4. the long product is assigned to the output range (long -> int)
// 5. the next value of “i_array” is assigned to “acc”
// 6. go back to step 3 to process the remaining elements in the input range
std::adjacent_difference(i_array, i_array + 4, o_array, std::multiplies<long>{});
```


## Example


### Example

```cpp
#include <array>
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

void println(auto comment, const auto& sequence)
{
    std::cout << comment;
    for (const auto& n : sequence)
        std::cout << n << ' ';
    std::cout << '\n';
};

int main()
{
    // Default implementation - the difference between two adjacent items
    std::vector v{4, 6, 9, 13, 18, 19, 19, 15, 10};
    println("Initially, v = ", v);
    std::adjacent_difference(v.begin(), v.end(), v.begin());
    println("Modified v = ", v);

    // Fibonacci
    std::array<int, 10> a {1};
    std::adjacent_difference(std::begin(a), std::prev(std::end(a)),
                             std::next(std::begin(a)), std::plus<>{});
    println("Fibonacci, a = ", a);
}
```


**Output:**
```
Initially, v = 4 6 9 13 18 19 19 15 10 
Modified v = 4 2 3 4 5 1 0 -4 -5 
Fibonacci, a = 1 1 2 3 5 8 13 21 34 55
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-539 | C++98 | the type requirements needed for the result<br>evaluations and assignments to be valid were missing | added |


## See also


| cpp/algorithm/dsc partial_sum | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |

