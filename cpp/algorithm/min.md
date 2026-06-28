---
title: std::min
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/min
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++14|
template< class T >
const T& min( const T& a, const T& b );
dcla|num=2|constexpr=c++14|
template< class T, class Compare >
const T& min( const T& a, const T& b, Compare comp );
dcla|num=3|since=c++11|constexpr=c++14|
template< class T >
T min( std::initializer_list<T> ilist );
dcla|num=4|since=c++11|constexpr=c++14|
template< class T, class Compare >
T min( std::initializer_list<T> ilist, Compare comp );
```

Returns the smaller of the given values.
@1,2@ Returns the smaller of `a` and `b`.
:@1@ Uses `operator<` to compare the values.
:@@ If `T` is not *LessThanComparable*, the behavior is undefined.
:@2@ Use the comparison function `comp` to compare the values.
@3,4@ Returns the smallest of the values in initializer list `ilist`.
@@ If `ilist.size()` is zero, or `T` is not *CopyConstructible*, the behavior is undefined.
:@3@ Uses `operator<` to compare the values.
:@@ If `T` is not *LessThanComparable*, the behavior is undefined.
:@4@ Use the comparison function `comp` to compare the values.

## Parameters


### Parameters

- `a, b` - the values to compare
- `ilist` - initializer list with the values to compare

## Return value

@1,2@ The smaller of `a` and `b`. If the values are equivalent, returns `a`.
@3,4@ The smallest value in `ilist`. If several values are equivalent to the smallest, returns the leftmost such value.

## Complexity

1. Exactly one comparison using `operator<`.
2. Exactly one application of the comparison function `comp`.
@3,4@ Given  as `ilist.size()`:
:@3@ Exactly  comparisons using `operator<`.
:@4@ Exactly  applications of the comparison function `comp`.

## Possible implementation

eq impl
|title1=min (1)|ver1=1|1=
template<class T>
const T& min(const T& a, const T& b)
{
return (b < a) ? b : a;
}
|title2=min (2)|ver2=2|2=
template<class T, class Compare>
const T& min(const T& a, const T& b, Compare comp)
{
return (comp(b, a)) ? b : a;
}
|title3=min (3)|ver3=3|3=
template<class T>
T min(std::initializer_list<T> ilist)
{
return *std::min_element(ilist.begin(), ilist.end());
}
|title4=min (4)|ver4=4|4=
template<class T, class Compare>
T min(std::initializer_list<T> ilist, Compare comp)
{
return *std::min_element(ilist.begin(), ilist.end(), comp);
}

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iostream>
#include <string_view>

int main()
{
    std::cout << "smaller of 10 and 010 is " << std::min(10, 010) << '\n'
              << "smaller of 'd' and 'b' is '" << std::min('d', 'b') << "'\n"
              << "shortest of \"foo\", \"bar\", and \"hello\" is \""
              << std::min({"foo", "bar", "hello"},
                          [](const std::string_view s1, const std::string_view s2)
                          {
                              return s1.size() < s2.size();
                          }) << "\"\n";
}
```


**Output:**
```
smaller of 10 and 010 is 8
smaller of 'd' and 'b' is 'b'
shortest of "foo", "bar", and "hello" is "foo"
```


## Defect reports


## See also


| cpp/algorithm/dsc max | (see dedicated page) |
| cpp/algorithm/dsc minmax | (see dedicated page) |
| cpp/algorithm/dsc min_element | (see dedicated page) |
| cpp/algorithm/dsc clamp | (see dedicated page) |
| cpp/algorithm/ranges/dsc min | (see dedicated page) |

