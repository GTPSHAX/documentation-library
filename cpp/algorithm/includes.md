---
title: std::includes
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/includes
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2 >
bool includes( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2 );
dcl|num=2|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2 >
bool includes( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2 );
dcla|num=3|notes=<sup>(constexpr C++20)</sup>|
template< class InputIt1, class InputIt2, class Compare >
bool includes( InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, Compare comp );
dcl|num=4|since=c++17|
template< class ExecutionPolicy,
class ForwardIt1, class ForwardIt2, class Compare >
bool includes( ExecutionPolicy&& policy,
ForwardIt1 first1, ForwardIt1 last1,
ForwardIt2 first2, ForwardIt2 last2, Compare comp );
```

Returns `true` if the sorted range [first2, last2) is a [subsequence](https://en.wikipedia.org/wiki/subsequence) of the sorted range [first1, last1) (a subsequence need not be contiguous).
1. If [first1, last1) or [first2, last2) is not `sorted` with respect to <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}, the behavior is undefined.
3. If [first1, last1) or [first2, last2) is not sorted with respect to `comp`, the behavior is undefined.
@2,4@ Same as , but executed according to `policy`.
@@

## Parameters


### Parameters

- `[first1, last1)` - 
- `[first2, last2)` - 
- `policy` - execution policy
- `comp` - comparison function

**Type requirements:**

- `InputIt1, InputIt2`
- `ForwardIt1, ForwardIt2`
- `Compare`

## Return value

`true` if [first2, last2) is a subsequence of [first1, last1); otherwise `false`.
An empty sequence is a subsequence of any sequence, so `true` is returned if [first2, last2) is empty.

## Complexity

Given  as `std::distance(first1, last1)` and  as `std::distance(first2, last2)`:
@1,2@ At most +N)-1 comparisons using <sup>(until C++20)</sup> `operator<`rev inl|since=c++20|}.
@3,4@ At most +N)-1 applications of the comparison function `comp`.

## Exceptions


## Possible implementation

eq impl
|title1=include (1)|ver1=1|1=
template<class InputIt1, class InputIt2>
bool includes(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2)
{
for (; first2 != last2; ++first1)
{
if (first1 == last1  *first2 < *first1)
return false;
if (!(*first1 < *first2))
++first2;
}
return true;
}
|title2=include (3)|ver2=3|2=
template<class InputIt1, class InputIt2, class Compare>
bool includes(InputIt1 first1, InputIt1 last1,
InputIt2 first2, InputIt2 last2, Compare comp)
{
for (; first2 != last2; ++first1)
{
if (first1 == last1  comp(*first2, *first1))
return false;
if (!comp(*first1, *first2))
++first2;
}
return true;
}

## Example


### Example


**Output:**
```
a b c f h x
includes:
a b c   : true
a c     : true
a a b   : false
g       : false
a c g   : false
A B C   : true (case-insensitive)
```


## Defect reports


## See also


| cpp/algorithm/dsc set_difference | (see dedicated page) |
| cpp/algorithm/dsc search | (see dedicated page) |
| cpp/algorithm/ranges/dsc includes | (see dedicated page) |

