---
title: std::equal
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/equal
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2 >
bool equal( InputIt1 first1, InputIt1 last1,
InputIt2 first2 );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
bool equal( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2 );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class BinaryPred >
bool equal( InputIt1 first1, InputIt1 last1,
InputIt2 first2, BinaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryPred >
bool equal( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, BinaryPred p );
dcla|num=5|since=c++14|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2 >
bool equal( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2 );
dcl|num=6|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
bool equal( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
dcla|num=7|since=c++14|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class BinaryPred >
bool equal( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, BinaryPred p );
dcl|num=8|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryPred >
bool equal( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2, BinaryPred p );
```

Checks whether [first1, last1) and a range starting from `first2` are equal:
* For overloads , the second range has `std::distance(first1, last1)` elements.
* For overloads , the second range is [first2, last2).
@1,5@ Elements are compared using `1=operator==`.
@3,7@ Elements are compared using the given binary predicate `p`.
@2,4,6,8@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `policy` - execution policy

**Type requirements:**

- `InputIt1, InputIt2`
- `ForwardIt1, ForwardIt2`
- `BinaryPred`

## Return value

@1-4@ If each corresponding elements in the two ranges are equal, returns `true`. Otherwise returns `false`.
@5-8@ If `std::distance(first1, last1)` and `std::distance(first2, last2)` are equal, and each corresponding elements in the two ranges are equal, returns `true`. Otherwise returns `false`.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
1. At most  comparisons using `1=operator==`.
2. ) comparisons using `1=operator==`.
3. At most  applications of the predicate `p`.
4. ) applications of the predicate `p`.
@5-8@ If `InputIt1` and `InputIt2` are both *RandomAccessIterator*, and `1=last1 - first1 != last2 - first2` is `true`, no comparison will be made.
@@ Otherwise, given  as ,N):
:@5@ At most  comparisons using `1=operator==`.
:@6@  comparisons using `1=operator==`.
:@7@ At most  applications of the predicate `p`.
:@8@  applications of the predicate `p`.

## Exceptions


## Possible implementation

eq impl
|title1=equal (1)|ver1=1|1=
template<class InputIt1, class InputIt2>
constexpr //< since C++20
bool equal(InputIt1 first1, InputIt1 last1, InputIt2 first2)
{
for (; first1 != last1; ++first1, ++first2)
if (!(*first1 == *first2))
return false;
return true;
}
|title2=equal (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class BinaryPred>
constexpr //< since C++20
bool equal(InputIt1 first1, InputIt1 last1,
InputIt2 first2, BinaryPred p)
{
for (; first1 != last1; ++first1, ++first2)
if (!p(*first1, *first2))
return false;
return true;
}
|title3=equal (5)|ver3=5|3=
namespace detail
{
// random-access iterator implementation (allows quick range size detection)
template<class RandomIt1, class RandomIt2>
constexpr //< since C++20
bool equal(RandomIt1 first1, RandomIt1 last1, RandomIt2 first2, RandomIt2 last2,
std::random_access_iterator_tag, std::random_access_iterator_tag)
{
if (last1 - first1 != last2 - first2)
return false;
for (; first1 != last1; ++first1, ++first2)
if (!(*first1 == *first2))
return false;
return true;
}
// input iterator implementation (needs to manually compare with “last2”)
template<class InputIt1, class InputIt2>
constexpr //< since C++20
bool equal(InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2,
std::input_iterator_tag, std::input_iterator_tag)
{
for (; first1 != last1 && first2 != last2; ++first1, ++first2)
if (!(*first1 == *first2))
return false;
return first1 == last1 && first2 == last2;
}
}
template<class InputIt1, class InputIt2>
constexpr //< since C++20
bool equal(InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2)
{
details::equal(first1, last1, first2, last2,
typename std::iterator_traits<InputIt1>::iterator_category(),
typename std::iterator_traits<InputIt2>::iterator_category());
}
|title4=equal (7)|ver4=7|4=
namespace detail
{
// random-access iterator implementation (allows quick range size detection)
template<class RandomIt1, class RandomIt2, class BinaryPred>
constexpr //< since C++20
bool equal(RandomIt1 first1, RandomIt1 last1,
RandomIt2 first2, RandomIt2 last2, BinaryPred p,
std::random_access_iterator_tag, std::random_access_iterator_tag)
{
if (last1 - first1 != last2 - first2)
return false;
for (; first1 != last1; ++first1, ++first2)
if (!p(*first1, *first2))
return false;
return true;
}
// input iterator implementation (needs to manually compare with “last2”)
template<class InputIt1, class InputIt2, class BinaryPred>
constexpr //< since C++20
bool equal(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, BinaryPred p,
std::input_iterator_tag, std::input_iterator_tag)
{
for (; first1 != last1 && first2 != last2; ++first1, ++first2)
if (!p(*first1, *first2))
return false;
return first1 == last1 && first2 == last2;
}
}
template<class InputIt1, class InputIt2, class BinaryPred>
constexpr //< since C++20
bool equal(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, BinaryPred p)
{
details::equal(first1, last1, first2, last2, p,
typename std::iterator_traits<InputIt1>::iterator_category(),
typename std::iterator_traits<InputIt2>::iterator_category());
}

## Notes

`std::equal` should not be used to compare the ranges formed by the iterators from `std::unordered_set`, `std::unordered_multiset`, `std::unordered_map`, or `std::unordered_multimap` because the order in which the elements are stored in those containers may be different even if the two containers store the same elements.
When comparing entire containers <sup>(since C++17)</sup> or string views for equality, `1=operator==` for the corresponding type are usually preferred.
Sequential `std::equal` is not guaranteed to be short-circuit. E.g. if the first pair elements of both ranges do not compare equal, the rest of elements may also be compared. Non-short-circuit comparison may happen when the ranges are compared with `std::memcmp` or implementation-specific vectorized algorithms.

## Example


### Example

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string_view>

constexpr bool is_palindrome(const std::string_view& s)
{
    return std::equal(s.cbegin(), s.cbegin() + s.size() / 2, s.crbegin());
}

void test(const std::string_view& s)
{
    std::cout << std::quoted(s)
              << (is_palindrome(s) ? " is" : " is not")
              << " a palindrome\n";
}

int main()
{
    test("radar");
    test("hello");
}
```


**Output:**
```
"radar" is a palindrome
"hello" is not a palindrome
```


## See also


| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/dsc lexicographical_compare | (see dedicated page) |
| cpp/algorithm/dsc mismatch | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc equal | (see dedicated page) |
| cpp/utility/functional/dsc equal_to | (see dedicated page) |
| cpp/algorithm/dsc equal_range | (see dedicated page) |

