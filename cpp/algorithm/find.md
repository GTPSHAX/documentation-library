---
title: std::find
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/find
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|constexpr1=c++20|until1=c++26
|dcl1=
template< class InputIt, class T >
InputIt find( InputIt first, InputIt last, const T& value );
|dcl2=
template< class InputIt, class T = typename std::iterator_traits
<InputIt>::value_type >
constexpr InputIt find( InputIt first, InputIt last, const T& value );
dcla|num=2|constexpr=c++20|
template< class InputIt, class UnaryPred >
InputIt find_if( InputIt first, InputIt last, UnaryPred p );
dcla|num=3|since=c++11|constexpr=c++20|
template< class InputIt, class UnaryPred >
InputIt find_if_not( InputIt first, InputIt last, UnaryPred q );
dcl rev multi|num=4|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy, class ForwardIt, class T >
ForwardIt find( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
|dcl2=
template< class ExecutionPolicy,
class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
ForwardIt find( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
dcl|num=5|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
ForwardIt find_if( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
dcl|num=6|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
ForwardIt find_if_not( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred q );
```

Returns an iterator to the first element in the source range [first, last) that satisfies specific criteria (or `last` if there is no such iterator).
1. `find` searches for the first element equal to `value` (using `1=operator==`).
2. `find_if` searches for the first element for which predicate `p` returns `true`.
3. `find_if_not` searches for the first element for which predicate `q` returns `false`.
@4-6@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[range=source, simple=yes}})` - 
- `value` - value to compare the elements to
- `policy` - execution policy

**Type requirements:**

- `InputIt`
- `ForwardIt`
- `UnaryPredicate`

## Return value

The first iterator `it` in the source range satisfying the following condition or `last` if there is no such iterator:
@1,4@ `1=*it == value` is `true`.
@2,5@ `1=p(*it)` is `true`.
@3,6@ `1=q(*it)` is `false`.

## Complexity

Given  as `std::distance(first, last)`:
1. At most  comparisons with `value` using `1=operator==`.
2. At most  applications of `p`.
3. At most  applications of `q`.
4. } comparisons with `value` using `1=operator==`.
5. } applications of `p`.
6. } applications of `q`.

## Exceptions

@4-6@

## Possible implementation

eq impl
|title1=find|ver1=1|1=
template<class InputIt, class T = typename std::iterator_traits<InputIt>::value_type>
constexpr InputIt find(InputIt first, InputIt last, const T& value)
{
for (; first != last; ++first)
if (*first == value)
return first;
return last;
}
|title2=find_if|ver2=2|2=
template<class InputIt, class UnaryPred>
constexpr InputIt find_if(InputIt first, InputIt last, UnaryPred p)
{
for (; first != last; ++first)
if (p(*first))
return first;
return last;
}
|title3=find_if_not|ver3=3|3=
template<class InputIt, class UnaryPred>
constexpr InputIt find_if_not(InputIt first, InputIt last, UnaryPred q)
{
for (; first != last; ++first)
if (!q(*first))
return first;
return last;
}

## Notes

If C++11 is not available, an equivalent to `std::find_if_not` is to use `std::find_if` with the negated predicate.
eq fun|
template<class InputIt, class UnaryPred>
InputIt find_if_not(InputIt first, InputIt last, UnaryPred q)
{
return std::find_if(first, last, std::not1(q));
}

## Example


### Example

```cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <complex>
#include <initializer_list>
#include <iostream>
#include <vector>

bool is_even(int i)
{
    return i % 2 == 0;
}

void example_contains()
{
    const auto haystack = {1, 2, 3, 4};

    for (const int needle : {3, 5})
        if (std::find(haystack.begin(), haystack.end(), needle) == haystack.end())
            std::cout << "haystack does not contain " << needle << '\n';
        else
            std::cout << "haystack contains " << needle << '\n';
}

void example_predicate()
{
    for (const auto& haystack : {std::array{3, 1, 4}, {1, 3, 5}<!---->})
    {
        const auto it = std::find_if(haystack.begin(), haystack.end(), is_even);
        if (it != haystack.end())
            std::cout << "haystack contains an even number " << *it << '\n';
        else
            std::cout << "haystack does not contain even numbers\n";
    }
}

void example_list_init()
{
    std::vector<std::complex<double>> haystack{<!---->{4.0, 2.0}<!---->};
#ifdef __cpp_lib_algorithm_default_value_type
    // T gets deduced making list-initialization possible
    const auto it = std::find(haystack.begin(), haystack.end(), {4.0, 2.0});
#else
    const auto it = std::find(haystack.begin(), haystack.end(), std::complex{4.0, 2.0});
#endif
    assert(it == haystack.begin());  
}

int main()
{
    example_contains();
    example_predicate();
    example_list_init();
}
```


**Output:**
```
haystack contains 3
haystack does not contain 5
haystack contains an even number 4
haystack does not contain even numbers
```


## Defect reports


## See also


| cpp/algorithm/ranges/dsc find | (see dedicated page) |
| cpp/algorithm/dsc adjacent_find | (see dedicated page) |
| cpp/algorithm/dsc find_end | (see dedicated page) |
| cpp/algorithm/dsc find_first_of | (see dedicated page) |
| cpp/algorithm/dsc mismatch | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |

