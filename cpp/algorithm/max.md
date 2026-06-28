---
title: std::max
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/max
---


```cpp
**Header:** `<`algorithm`>`
dcla|num=1|constexpr=c++14|
template< class T >
const T& max( const T& a, const T& b );
dcla|num=2|constexpr=c++14|
template< class T, class Compare >
const T& max( const T& a, const T& b, Compare comp );
dcla|num=3|since=c++11|constexpr=c++14|
template< class T >
T max( std::initializer_list<T> ilist );
dcla|num=4|since=c++11|constexpr=c++14|
template< class T, class Compare >
T max( std::initializer_list<T> ilist, Compare comp );
```

Returns the greater of the given values.
@1,2@ Returns the greater of `a` and `b`.
:@1@ Uses `operator<` to compare the values.
:@@ If `T` is not *LessThanComparable*, the behavior is undefined.
:@2@ Use the comparison function `comp` to compare the values.
@3,4@ Returns the greatest of the values in initializer list `ilist`.
@@ If `ilist.size()` is zero, or `T` is not *CopyConstructible*, the behavior is undefined.
:@3@ Uses `operator<` to compare the values.
:@@ If `T` is not *LessThanComparable*, the behavior is undefined.
:@4@ Use the comparison function `comp` to compare the values.

## Parameters


### Parameters

- `a, b` - the values to compare
- `ilist` - initializer list with the values to compare

## Return value

@1,2@ The greater of `a` and `b`. If they are equivalent, returns `a`.
@3,4@ The greatest value in `ilist`. If several values are equivalent to the greatest, returns the leftmost one.

## Complexity

1. Exactly one comparison using `operator<`.
2. Exactly one application of the comparison function `comp`.
@3,4@ Given  as `ilist.size()`:
:@3@ Exactly  comparisons using `operator<`.
:@4@ Exactly  applications of the comparison function `comp`.

## Possible implementation

eq impl
|title1=max (1)|ver1=1|1=
template<class T>
const T& max(const T& a, const T& b)
{
return (a < b) ? b : a;
}
|title2=max (2)|ver2=2|2=
template<class T, class Compare>
const T& max(const T& a, const T& b, Compare comp)
{
return (comp(a, b)) ? b : a;
}
|title3=max (3)|ver3=3|3=
template<class T>
T max(std::initializer_list<T> ilist)
{
return *std::max_element(ilist.begin(), ilist.end());
}
|title4=max (4)|ver4=4|4=
template<class T, class Compare>
T max(std::initializer_list<T> ilist, Compare comp)
{
return *std::max_element(ilist.begin(), ilist.end(), comp);
}

## Notes


## Example


### Example

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string_view>

int main()
{
    auto longest = [](const std::string_view s1, const std::string_view s2)
                   {
                       return s1.size() < s2.size();
                   };

    std::cout << "Larger of 69 and 96 is " << std::max(69, 96) << "\n"
                 "Larger of 'q' and 'p' is '" << std::max('q', 'p') << "'\n"
                 "Largest of 010, 10, 0X10, and 0B10 is "
              << std::max({010, 10, 0X10, 0B10}) << '\n'
              << R"(Longest of "long", "short", and "int" is )"
              << std::quoted(std::max({"long", "short", "int"}, longest)) << '\n';
}
```


**Output:**
```
Larger of 69 and 96 is 96
Larger of 'q' and 'p' is 'q'
Largest of 010, 10, 0X10, and 0B10 is 16
Longest of "long", "short", and "int" is "short"
```


## Defect reports


## See also


| cpp/algorithm/dsc min | (see dedicated page) |
| cpp/algorithm/dsc minmax | (see dedicated page) |
| cpp/algorithm/dsc max_element | (see dedicated page) |
| cpp/algorithm/dsc clamp | (see dedicated page) |
| cpp/algorithm/ranges/dsc max | (see dedicated page) |

