---
title: std::mismatch
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/mismatch
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2 >
std::pair<InputIt1, InputIt2>
mismatch( InputIt1 first1, InputIt1 last1,
InputIt2 first2 );
dcl|num=2|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
std::pair<ForwardIt1, ForwardIt2>
mismatch( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2 );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class BinaryPred >
std::pair<InputIt1, InputIt2>
mismatch( InputIt1 first1, InputIt1 last1,
InputIt2 first2, BinaryPred p );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryPred >
std::pair<ForwardIt1, ForwardIt2>
mismatch( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, BinaryPred p );
dcla|num=5|since=c++14|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2 >
std::pair<InputIt1, InputIt2>
mismatch( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2 );
dcl|num=6|since=c++17|
template< class ExecutionPolicy, class ForwardIt1, class ForwardIt2 >
std::pair<ForwardIt1, ForwardIt2>
mismatch( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
dcla|num=7|since=c++14|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class BinaryPred >
std::pair<InputIt1, InputIt2>
mismatch( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, BinaryPred p );
dcl|num=8|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class BinaryPred >
std::pair<ForwardIt1, ForwardIt2>
mismatch( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2, BinaryPred p );
```

Returns a pair of iterators to the first mismatching of elements from [first1, last1) and a range starting from `first2`:
* For overloads , the second range has `std::distance(first1, last1)` elements.
* For overloads , the second range is [first2, last2).
:* If `std::distance(first1, last1)` and `std::distance(first2, last2)` are different, the comparison stops when `last1` or `last2` is reached.
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

- `InputIt1`
- `InputIt2`
- `ForwardIt1`
- `ForwardIt2`
- `BinaryPred`

## Return value

`std::pair` with iterators to the first two non-equal elements.
If `last1` is reached, the second iterator in the pair is the `std::distance(first1, last1)` iterator after `first2`.
For overloads , if `last2` is reached, the first iterator in the pair is the `std::distance(first2, last2)` iterator after `first1`.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
@1,2@ At most  comparisons using `1=operator==`.
@3,4@ At most  applications of the predicate `p`.
@5,6@ At most ,N) comparisons using `1=operator==`.
@7,8@ At most ,N) applications of the predicate `p`.

## Exceptions


## Possible implementation

eq impl
|title1=mismatch (1)|ver1=1|1=
template<class InputIt1, class InputIt2>
std::pair<InputIt1, InputIt2>
mismatch(InputIt1 first1, InputIt1 last1, InputIt2 first2)
{
while (first1 != last1 && *first1 == *first2)
++first1, ++first2;
return std::make_pair(first1, first2);
}
|title2=mismatch (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class BinaryPred>
std::pair<InputIt1, InputIt2>
mismatch(InputIt1 first1, InputIt1 last1, InputIt2 first2, BinaryPred p)
{
while (first1 != last1 && p(*first1, *first2))
++first1, ++first2;
return std::make_pair(first1, first2);
}
|title3=mismatch (5)|ver3=5|3=
template<class InputIt1, class InputIt2>
std::pair<InputIt1, InputIt2>
mismatch(InputIt1 first1, InputIt1 last1, InputIt2 first2, InputIt2 last2)
{
while (first1 != last1 && first2 != last2 && *first1 == *first2)
++first1, ++first2;
return std::make_pair(first1, first2);
}
|title4=mismatch (7)|ver4=7|4=
template<class InputIt1, class InputIt2, class BinaryPred>
std::pair<InputIt1, InputIt2>
mismatch(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, BinaryPred p)
{
while (first1 != last1 && first2 != last2 && p(*first1, *first2))
++first1, ++first2;
return std::make_pair(first1, first2);
}

## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string>

std::string mirror_ends(const std::string& in)
{
    return std::string(in.begin(),
                       std::mismatch(in.begin(), in.end(), in.rbegin()).first);
}

int main()
{
    std::cout << mirror_ends("abXYZba") << '\n'
              << mirror_ends("abca") << '\n'
              << mirror_ends("aba") << '\n';
}
```


**Output:**
```
ab
a
aba
```


## See also


| cpp/algorithm/dsc equal | (see dedicated page) |
| cpp/algorithm/dsc find | (see dedicated page) |
| cpp/algorithm/dsc lexicographical_compare | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc mismatch | (see dedicated page) |

