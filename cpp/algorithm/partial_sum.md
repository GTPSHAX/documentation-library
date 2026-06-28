---
title: std::partial_sum
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/partial_sum
---


```cpp
**Header:** `<`numeric`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt >
OutputIt partial_sum( InputIt first, InputIt last,
OutputIt d_first );
dcla|num=2|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt, class BinaryOp >
OutputIt partial_sum( InputIt first, InputIt last,
OutputIt d_first, BinaryOp op );
```

1. If [first, last) is empty, does nothing.
@@ Otherwise, performs the following operations in order:
# Creates an accumulator `acc`, whose type is the value type of `InputIt`, and initializes it with `*first`.
# Assigns `acc` to `*d_first`.
# For each integer `i` in [1, std::distance(first, last)), performs the following operations in order:
::@a@ Computes <sup>(until C++20)</sup> `acc + *iter`<sup>(since C++20)</sup> `std::move(acc) + *iter`, where `iter` is the next `i` iterator of `first`.
::@b@ Assigns the result to `acc`.
::@c@ Assigns `acc` to `*dest`, where `dest` is the next `i` iterator of `d_first`.
2. Same as , but computes <sup>(until C++20)</sup> `op(acc, *iter)`<sup>(since C++20)</sup> `op(std::move(acc), *iter)` instead.
Given `binary_op` as the actual binary operation:
* If any of the following conditions is satisfied, the program is ill-formed:
:* The value type of `InputIt` is not constructible from `*first`.
:* `acc` is not writable to `d_first`.
:* The result of <sup>(until C++20)</sup> `binary_op(acc, *iter)`<sup>(since C++20)</sup> `binary_op(std::move(acc), *iter)` is not implicitly convertible to the value type of `InputIt`.
* Given `d_last` as the iterator to be returned, if any of the following conditions is satisfied, the behavior is undefined:
:* `binary_op` modifies any element of [first, last) or [d_first, d_last).
:* `binary_op` invalidates any iterator or subrange in  or .

## Parameters


### Parameters

- `d_first` - the beginning of the destination range; may be equal to `first`

**Type requirements:**

- `InputIt`
- `OutputIt`

## Return value

Iterator to the element past the last element written, or `d_first` if [first, last) is empty.

## Complexity

Given  as `std::distance(first, last)`:
1. Exactly  applications of `operator+`.
2. Exactly  applications of the binary function `op`.

## Possible implementation

eq impl
|title1=partial_sum (1)|ver1=1|1=
template<class InputIt, class OutputIt>
constexpr // since C++20
OutputIt partial_sum(InputIt first, InputIt last, OutputIt d_first)
{
if (first == last)
return d_first;
typename std::iterator_traits<InputIt>::value_type sum = *first;
*d_first = sum;
while (++first != last)
{
sum = std::move(sum) + *first; // std::move since C++20
*++d_first = sum;
}
return ++d_first;
// or, since C++14:
// return std::partial_sum(first, last, d_first, std::plus<>());
}
|title2=partial_sum (2)|ver2=2|2=
template<class InputIt, class OutputIt, class BinaryOp>
constexpr // since C++20
OutputIt partial_sum(InputIt first, InputIt last,
OutputIt d_first, BinaryOp op)
{
if (first == last)
return d_first;
typename std::iterator_traits<InputIt>::value_type acc = *first;
*d_first = acc;
while (++first != last)
{
acc = op(std::move(acc), *first); // std::move since C++20
*++d_first = acc;
}
return ++d_first;
}

## Notes

`acc` was introduced because of the resolution of . The reason of using `acc` rather than directly summing up the results (i.e. `1=*(d_first + 2) = (*first + *(first + 1)) + *(first + 2);`) is because the semantic of the latter is confusing if the following types mismatch:
* the value type of `InputIt`
* the writable type(s) of `OutputIt`
* the types of the parameters of `operator+` or `op`
* the return type of `operator+` or `op`
`acc` serves as the intermediate object to store and provide the values for each step of the computation:
* its type is the value type of `InputIt`
* it is written to `d_first`
* its value is passed to `operator+` or `op`
* it stores the return value of `operator+` or `op`

```cpp
enum not_int { x = 1, y = 2 };

char i_array[4] = {100, 100, 100, 100};
not_int e_array[4] = {x, x, y, y};
int  o_array[4];

// OK: uses operator+(char, char) and assigns char values to int array
std::partial_sum(i_array, i_array + 4, o_array);

// Error: cannot assign not_int values to int array
std::partial_sum(e_array, e_array + 4, o_array);

// OK: performs conversions when needed
// 1. creates “acc” of type char (the value type)
// 2. the char arguments are used for long multiplication (char -> long)
// 3. the long product is assigned to “acc” (long -> char)
// 4. “acc” is assigned to an element of “o_array” (char -> int)
// 5. go back to step 2 to process the remaining elements in the input range
std::partial_sum(i_array, i_array + 4, o_array, std::multiplies<long>{});
```


## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

int main()
{
    std::vector<int> v(10, 2); // v = {2, 2, 2, 2, 2, 2, 2, 2, 2, 2}

    std::cout << "The first " << v.size() << " even numbers are: ";
    // write the result to the cout stream
    std::partial_sum(v.cbegin(), v.cend(), 
                     std::ostream_iterator<int>(std::cout, " "));
    std::cout << '\n';

    // write the result back to the vector v
    std::partial_sum(v.cbegin(), v.cend(),
                     v.begin(), std::multiplies<int>());

    std::cout << "The first " << v.size() << " powers of 2 are: ";
    for (int n : v)
        std::cout << n << ' ';
    std::cout << '\n';
}
```


**Output:**
```
The first 10 even numbers are: 2 4 6 8 10 12 14 16 18 20 
The first 10 powers of 2 are: 2 4 8 16 32 64 128 256 512 1024
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-539 | C++98 | the type requirements needed for the result<br>evaluations and assignments to be valid were missing | added |


## See also


| cpp/algorithm/dsc adjacent_difference | (see dedicated page) |
| cpp/algorithm/dsc accumulate | (see dedicated page) |
| cpp/algorithm/dsc inclusive_scan | (see dedicated page) |
| cpp/algorithm/dsc exclusive_scan | (see dedicated page) |

