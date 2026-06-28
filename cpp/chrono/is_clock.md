---
title: std::chrono::is_clock
type: Utilities
source: https://en.cppreference.com/w/cpp/chrono/is_clock
---

ddcl|header=chrono|since=c++20|
template< class T >
struct is_clock;
If `T` satisfies the *Clock* requirements, provides the member constant `value` equal `true`. For any other type, `value` is `false`.
For the purpose of this trait, the extent to which an implementation determines that a type cannot meet the *Clock* requirements is unspecified, except that a minimum `T` shall not qualify as a *Clock* unless it meets all following conditions:
* Each of the following  is valid and denotes a type:
:* `T::rep`
:* `T::period`
:* `T::duration`
:* `T::time_point`
* Each of the following expressions is well-formed when treated as an unevaluated operand:
:* `T::is_steady`
:* `T::now()`

## Template parameters


### Parameters

- `T` - a type to check

## Helper variable template

ddcl|since=c++20|1=
template< class T >
constexpr bool is_clock_v = is_clock<T>::value;

## Possible implementation

eq fun|
template<class>
struct is_clock : std::false_type {};
template<class T>
requires
requires
{
typename T::rep;
typename T::period;
typename T::duration;
typename T::time_point;
T::is_steady; // type is not checked
T::now();     // return type is not checked
}
struct is_clock<T> : std::true_type {};

## Notes

If `T` otherwise meets the *Clock* requirements, but `T::is_steady` is not of type `const bool`, or `T::now()` is not of type `T::time_point`, the result of `is_clock_v<T>` is unspecified.

## Example


### Example

```cpp
#include <chrono>
#include <ratio>

static_assert
(
    std::chrono::is_clock_v<std::chrono::utc_clock> and
    not std::chrono::is_clock_v<std::chrono::duration<int, std::exa>>
);

int main() {}
```

