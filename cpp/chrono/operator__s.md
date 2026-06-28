---
title: std::literals::chrono_literals::operator""s
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/operator""s
---


```cpp
**Header:** `<`chrono`>`
dcl|num=1|since=c++14|
constexpr std::chrono::seconds
operator""s( unsigned long long secs );
dcl|num=2|since=c++14|
constexpr std::chrono::duration</*unspecified*/>
operator""s( long double secs );
```

Forms a `std::chrono::duration` literal representing seconds.
1. Integer literal, returns exactly `std::chrono::seconds(secs)`.
2. Floating-point literal, returns a floating-point duration equivalent to `std::chrono::seconds`.

## Parameters


### Parameters

- `secs` - the number of seconds

## Return value

The `std::chrono::duration` literal.

## Possible implementation

eq fun
|1=
constexpr std::chrono::seconds operator""s(unsigned long long s)
{
return std::chrono::seconds(s);
}
constexpr std::chrono::duration<long double> operator""s(long double s)
{
return std::chrono::duration<long double>(s);
}

## Notes

`std::string` also defines `operator""s`, to represent literal objects of type `std::string`, but it is a string literal: `10s` is ten seconds, but `"10"s` is a two-character string.

## Example


### Example

```cpp
#include <chrono>
#include <iostream>

int main()
{
    using namespace std::chrono_literals;

    std::chrono::seconds halfmin = 30s;
    std::cout << "Half a minute is " << halfmin.count() << " seconds"
        " (" << halfmin << ").\n"
        "A minute and a second is " << (1min + 1s).count() << " seconds.\n";

    std::chrono::duration moment = 0.1s;
    std::cout << "A moment is " << moment.count() << " seconds"
        " (" << moment << ").\n"
        "And thrice as much is " << (moment + 0.2s).count() << " seconds.\n";
}
```


**Output:**
```
Half a minute is 30 seconds (30s).
A minute and a second is 61 seconds.
A moment is 0.1 seconds (0.1s).
And thrice as much is 0.3 seconds.
```


## See also


| cpp/chrono/duration/dsc constructor | (see dedicated page) |

