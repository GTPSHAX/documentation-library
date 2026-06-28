---
title: std::transform
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/transform
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt, class OutputIt, class UnaryOp >
OutputIt transform( InputIt first1, InputIt last1,
OutputIt d_first, UnaryOp unary_op );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class UnaryOp >
ForwardIt2 transform( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 d_first, UnaryOp unary_op );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2,
class OutputIt, class BinaryOp >
OutputIt transform( InputIt1 first1, InputIt1 last1, InputIt2 first2,
OutputIt d_first, BinaryOp binary_op );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2,
class ForwardIt3, class BinaryOp >
ForwardIt3 transform( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2,
ForwardIt3 d_first, BinaryOp binary_op );
```

`std::transform` applies the given function to the elements of the given input range(s), and stores the result in an output range starting from `d_first`.
1. The unary operation `unary_op` is applied to the elements of [first1, last1).
@@ If `unary_op` invalidates an iterator or modifies an element in any of the following ranges, the behavior is undefined:
* .
* The range of `std::distance(first1, last1) + 1` elements starting from `d_first`.
3. The binary operation `binary_op` is applied to pairs of elements from two ranges: [first1, last1) and another range of `std::distance(first1, last1)` elements starting from `first2`.
@@ If `binary_op` invalidates an iterator or modifies an element in any of the following ranges, the behavior is undefined:
* .
* The range of `std::distance(first1, last1) + 1` elements starting from `first2`.
* The range of `std::distance(first1, last1) + 1` elements starting from `d_first`.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[first1, last1)` - 
- `first2` - the beginning of the second range of elements to transform,  only
- `d_first` - the beginning of the destination range, may be equal to `first1` or `first2`
- `policy` - execution policy

**Type requirements:**

- `InputIt, InputIt1, InputIt2`
- `OutputIt`
- `ForwardIt1, ForwardIt2, ForwardIt3`

## Return value

Output iterator to the element that follows the last element transformed.

## Complexity

Given  as `std::distance(first1, last1)`:
@1,2@ Exactly  applications of `unary_op`.
@3,4@ Exactly  applications of `binary_op`.

## Exceptions


## Possible implementation

eq impl
|title1=transform (1)|ver1=1|1=
template<class InputIt, class OutputIt, class UnaryOp>
constexpr //< since C++20
OutputIt transform(InputIt first1, InputIt last1,
OutputIt d_first, UnaryOp unary_op)
{
for (; first1 != last1; ++d_first, ++first1)
*d_first = unary_op(*first1);
return d_first;
}
|title2=transform (3)|ver2=3|2=
template<class InputIt1, class InputIt2,
class OutputIt, class BinaryOp>
constexpr //< since C++20
OutputIt transform(InputIt1 first1, InputIt1 last1, InputIt2 first2,
OutputIt d_first, BinaryOp binary_op)
{
for (; first1 != last1; ++d_first, ++first1, ++first2)
*d_first = binary_op(*first1, *first2);
return d_first;
}

## Notes

`std::transform` does not guarantee in-order application of `unary_op` or `binary_op`. To apply a function to a sequence in-order or to apply a function that modifies the elements of a sequence, use `std::for_each`.

## Example


### Example

```cpp
#include <algorithm>
#include <cctype>
#include <iomanip>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

void print_ordinals(const std::vector<unsigned>& ordinals)
{
    std::cout << "ordinals: ";
    for (unsigned ord : ordinals)
        std::cout << std::setw(3) << ord << ' ';
    std::cout << '\n';
}

char to_uppercase(unsigned char c)
{
    return std::toupper(c);
}

void to_uppercase_inplace(char& c)
{
    c = to_uppercase(c);
}

void unary_transform_example(std::string& hello, std::string world)
{
    // Transform string to uppercase in-place

    std::transform(hello.cbegin(), hello.cend(), hello.begin(), to_uppercase);
    std::cout << "hello = " << std::quoted(hello) << '\n';

    // for_each version (see Notes above)
    std::for_each(world.begin(), world.end(), to_uppercase_inplace);
    std::cout << "world = " << std::quoted(world) << '\n';
}

void binary_transform_example(std::vector<unsigned> ordinals)
{
    // Transform numbers to doubled values

    print_ordinals(ordinals);

    std::transform(ordinals.cbegin(), ordinals.cend(), ordinals.cbegin(),
                   ordinals.begin(), std::plus<>{});

    print_ordinals(ordinals);
}

int main()
{
    std::string hello("hello");
    unary_transform_example(hello, "world");

    std::vector<unsigned> ordinals;
    std::copy(hello.cbegin(), hello.cend(), std::back_inserter(ordinals));
    binary_transform_example(std::move(ordinals));
}
```


**Output:**
```
hello = "HELLO"
world = "WORLD"
ordinals:  72  69  76  76  79 
ordinals: 144 138 152 152 158
```


## Defect reports


## See also


| cpp/algorithm/dsc for_each | (see dedicated page) |
| cpp/algorithm/ranges/dsc transform | (see dedicated page) |

