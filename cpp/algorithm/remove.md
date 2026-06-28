---
title: std::remove
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/remove
---


```cpp
**Header:** `<`algorithm`>`
dcl rev multi|num=1|notes1=<sup>(constexpr C++20)</sup>|until1=c++26
|dcl1=
template< class ForwardIt, class T >
ForwardIt remove( ForwardIt first, ForwardIt last, const T& value );
|dcl2=
template< class ForwardIt, class T = typename std::iterator_traits
<ForwardIt>::value_type >
constexpr ForwardIt remove( ForwardIt first, ForwardIt last,
const T& value );
dcl rev multi|num=2|since1=c++17|until1=c++26
|dcl1=
template< class ExecutionPolicy, class ForwardIt, class T >
ForwardIt remove( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
|dcl2=
template< class ExecutionPolicy, class ForwardIt,
class T = typename std::iterator_traits
<ForwardIt>::value_type >
ForwardIt remove( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, const T& value );
dcla|num=3|constexpr=c++20|
template< class ForwardIt, class UnaryPred >
ForwardIt remove_if( ForwardIt first, ForwardIt last, UnaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy, class ForwardIt, class UnaryPred >
ForwardIt remove_if( ExecutionPolicy&& policy,
ForwardIt first, ForwardIt last, UnaryPred p );
```

Removes all elements satisfying specific criteria from the range [first, last) and returns a past-the-end iterator for the new end of the range.
1. Removes all elements that are equal to `value` (using `1=operator==`).
3. Removes all elements for which predicate `p` returns `true`.
@2,4@ Same as , but executed according to `policy`.
@@
rev|until=c++11|
If the value type of `ForwardIt` is not *CopyAssignable*, the behavior is undefined.
rev|since=c++11|
If the type of `*first` is not *MoveAssignable*, the behavior is undefined.

## Explanation

Removing is done by shifting the elements in the range in such a way that the elements that are not to be removed appear in the beginning of the range.
* Shifting is done by <sup>(until C++11)</sup> <sup>(since C++11)</sup> .
* The removing operation is stable: the relative order of the elements not to be removed stays the same.
* The underlying sequence of [first, last) is not shortened by the removing operation. Given `result` as the returned iterator:
:* All iterators in [result, last) are still dereferenceable.
rrev|since=c++11|
:* Each element of [result, last) has a valid but unspecified state, because move assignment can eliminate elements by moving from elements that were originally in that range.

## Parameters


### Parameters

- `value` - the value of elements to remove
- `policy` - execution policy

**Type requirements:**

- `ForwardIt`
- `UnaryPredicate`

## Return value

Past-the-end iterator for the new range of values (if this is not `end`, then it points to an unspecified value, and so do iterators to any values between this iterator and `end`).

## Complexity

Given  as `std::distance(first, last)`:
@1,2@ Exactly  comparisons using `1=operator==`.
@3,4@ Exactly  applications of the predicate `p`.

## Exceptions


## Possible implementation

eq impl
|title1=remove (1)|ver1=1|1=
template<class ForwardIt, class T = typename std::iterator_traits<ForwardIt>::value_type>
ForwardIt remove(ForwardIt first, ForwardIt last, const T& value)
{
first = std::find(first, last, value);
if (first != last)
for (ForwardIt i = first; ++i != last;)
if (!(*i == value))
*first++ = std::move(*i);
return first;
}
|title2=remove_if (3)|ver2=3|2=
template<class ForwardIt, class UnaryPred>
ForwardIt remove_if(ForwardIt first, ForwardIt last, UnaryPred p)
{
first = std::find_if(first, last, p);
if (first != last)
for (ForwardIt i = first; ++i != last;)
if (!p(*i))
*first++ = std::move(*i);
return first;
}

## Notes

A call to `remove` is typically followed by a call to a container's `erase` member function to actually remove elements from the container. These two invocations together constitute a so-called [erase-remove idiom](https://en.wikipedia.org/wiki/erase-remove idiom).
rrev|since=c++20|
The same effect can also be achieved by the following non-member functions:
* `std::erase`, which has overloads for all standard sequence containers.
* `std::erase_if`, which has overloads for all standard containers.
The similarly-named container member functions , , , and  erase the removed elements.
These algorithms cannot be used with associative containers such as `std::set` and `std::map` because their iterator types do not dereference to *MoveAssignable* types (the keys in these containers are not modifiable).
The standard library also defines an overload of  in , which takes a `const char*` and is used to delete files.
Because `std::remove` takes `value` by reference, it can have unexpected behavior if it is a reference to an element of the range [first, last).

## Example


### Example

```cpp
#include <algorithm>
#include <cassert>
#include <cctype>
#include <complex>
#include <iomanip>
#include <iostream>
#include <string>
#include <string_view>
#include <vector>

int main()
{
    std::string str1{"Quick  Red  Dog"};
    std::cout << "1) " << std::quoted(str1) << '\n';
    const auto noSpaceEnd = std::remove(str1.begin(), str1.end(), ' ');
    std::cout << "2) " << std::quoted(str1) << '\n';

    // The spaces are removed from the string only logically.
    // Note, we use view, the original string is still not shrunk:
    std::cout << "3) " << std::quoted(std::string_view(str1.begin(), noSpaceEnd))
              << ", size: " << str1.size() << '\n';

    str1.erase(noSpaceEnd, str1.end());
    // The spaces are removed from the string physically.
    std::cout << "4) " << std::quoted(str1) << ", size: " << str1.size() << '\n';

    std::string str2 = "Jumped\n Over\tA\vLazy \t  Fox\r\n";
    str2.erase(std::remove_if(str2.begin(), 
                              str2.end(),
                              [](unsigned char x) { return std::isspace(x); }),
               str2.end());
    std::cout << "5) " << std::quoted(str2) << '\n';

    std::vector<std::complex<double>> nums{<!---->{2, 2}, {1, 3}, {4, 8}<!---->};
    #ifdef __cpp_lib_algorithm_default_value_type
        nums.erase(std::remove(nums.begin(), nums.end(), {1, 3}), nums.end());
    #else
        nums.erase(std::remove(nums.begin(), nums.end(), std::complex<double>{1, 3}),
                   nums.end());
    #endif
    assert((nums == std::vector<std::complex<double>>{<!---->{2, 2}, {4, 8}<!---->}));
}
```


**Output:**
```
1) "Quick  Red  Dog"
2) "QuickRedDog Dog"
3) "QuickRedDog", size: 15
4) "QuickRedDog", size: 11
5) "JumpedOverALazyFox"
```


## Defect reports


## See also


| cpp/algorithm/dsc remove_copy | (see dedicated page) |
| cpp/algorithm/dsc unique | (see dedicated page) |
| cpp/algorithm/ranges/dsc remove | (see dedicated page) |

