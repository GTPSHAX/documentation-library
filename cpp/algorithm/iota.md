---
title: std::iota
type: Algorithm
source: https://en.cppreference.com/w/cpp/algorithm/iota
---

ddcl|header=numeric|since=c++11|notes=<sup>(constexpr C++20)</sup>|
template< class ForwardIt, class T >
void iota( ForwardIt first, ForwardIt last, T value );
Fills the range [first, last) with sequentially increasing values, starting with `value` and repetitively evaluating `++value`.
Equivalent operation (assuming `++value` returns the incremented value):

```cpp
*first   = value;
*++first = ++value;
*++first = ++value;
*++first = ++value;
// repeats until “last” is reached
```

If any of the following conditions is satisfied, the program is ill-formed:
* `T` is not convertible to the value type of `ForwardIt`.
* The expression `++val` is ill-formed, where `val` is a variable of type `T`.

## Parameters


### Parameters

- `[3=to fill with sequentially increasing values starting with {{c, value}}}})` - 
- `value` - initial value to store

## Complexity

Exactly `std::distance(first, last)` increments and assignments.

## Possible implementation

eq fun
|1=
template<class ForwardIt, class T>
constexpr // since C++20
void iota(ForwardIt first, ForwardIt last, T value)
{
for (; first != last; ++first, ++value)
*first = value;
}

## Notes

The function is named after the integer function <span style="font-size: 1.5em">⍳</span>  from the programming language [APL (programming language)|APL](https://en.wikipedia.org/wiki/APL (programming language)|APL). It was one of the [https://web.archive.org/web/20220816102741/http://www.martinbroadhurst.com/stl/iota.html STL components] that were not included in C++98, but made it into the standard library in C++11.

## Example


### Example

```cpp
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <list>
#include <numeric>
#include <random>
#include <vector>

class BigData // inefficient to copy
{
    int data[1024]; /* some raw data */
public:
    explicit BigData(int i = 0) { data[0] = i; /* ... */ }
    operator int() const { return data[0]; }
    BigData& operator=(int i) { data[0] = i; return *this; }
    /* ... */
};

int main()
{
    std::list<BigData> l(10);
    std::iota(l.begin(), l.end(), -4);

    std::vector<std::list<BigData>::iterator> v(l.size());
    std::iota(v.begin(), v.end(), l.begin());
    // Vector of iterators (to original data) is used to avoid expensive copying,
    // and because std::shuffle (below) cannot be applied to a std::list directly.

    std::shuffle(v.begin(), v.end(), std::mt19937{std::random_device{}()});

    std::cout << "Original contents of the list l:\t";
    for (const auto& n : l)
        std::cout << std::setw(2) << n << ' ';
    std::cout << '\n';

    std::cout << "Contents of l, viewed via shuffled v:\t";
    for (const auto i : v)
        std::cout << std::setw(2) << *i << ' ';
    std::cout << '\n';
}
```


**Output:**
```
Original contents of the list l:	-4 -3 -2 -1  0  1  2  3  4  5
Contents of l, viewed via shuffled v:	-1  5 -4  0  2  1  4 -2  3 -3
```


## See also


| cpp/algorithm/ranges/dsc iota | (see dedicated page) |
| cpp/algorithm/dsc fill | (see dedicated page) |
| cpp/algorithm/ranges/dsc fill | (see dedicated page) |
| cpp/algorithm/dsc generate | (see dedicated page) |
| cpp/algorithm/ranges/dsc generate | (see dedicated page) |
| cpp/ranges/dsc iota_view | (see dedicated page) |
| cpp/ranges/dsc views indices | (see dedicated page) |
| cpp/ranges/dsc enumerate_view | (see dedicated page) |

