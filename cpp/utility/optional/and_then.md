---
title: std::optional::and_then
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/optional/and_then
---


```cpp
dcl|num=1|since=c++23|1=
template< class F >
constexpr auto and_then( F&& f ) &;
dcl|num=2|since=c++23|1=
template< class F >
constexpr auto and_then( F&& f ) const&;
dcl|num=3|since=c++23|1=
template< class F >
constexpr auto and_then( F&& f ) &&;
dcl|num=4|since=c++23|1=
template< class F >
constexpr auto and_then( F&& f ) const&&;
```

If `*this` contains a value, invokes `f` with the contained value as an argument, and returns the result of that invocation; otherwise, returns an empty `std::optional`.
The return type (see below) must be a specialization of `std::optional` (unlike `transform()`). Otherwise, the program is ill-formed.
1. Equivalent to:

```cpp
if (*this)
    return std::invoke(std::forward<F>(f), value());
else
    return std::remove_cvref_t<std::invoke_result_t<F, T&>>{};
```

2. Equivalent to:

```cpp
if (*this)
    return std::invoke(std::forward<F>(f), value());
else
    return std::remove_cvref_t<std::invoke_result_t<F, const T&>>{};
```

3. Equivalent to:

```cpp
if (*this)
    return std::invoke(std::forward<F>(f), std::move(value()));
else
    return std::remove_cvref_t<std::invoke_result_t<F, T>>{};
```

4. Equivalent to:

```cpp
if (*this)
    return std::invoke(std::forward<F>(f), std::move(value());
else
    return std::remove_cvref_t<std::invoke_result_t<F, const T>>{};
```


## Parameters


### Parameters

- `f` - a suitable function or *Callable* object that returns an `std::optional`

## Return value

The result of `f` or an empty `std::optional`, as described above.

## Notes

Some languages call this operation ''flatmap''.

## Example


### Example

```cpp
#include <charconv>
#include <iomanip>
#include <iostream>
#include <optional>
#include <ranges>
#include <string>
#include <string_view>
#include <vector>

std::optional<int> to_int(std::string_view sv)
{
    int r{};
    auto [ptr, ec]{std::from_chars(sv.data(), sv.data() + sv.size(), r)};
    if (ec == std::errc())
        return r;
    else
        return std::nullopt;
}

int main()
{
    using namespace std::literals;

    const std::vector<std::optional<std::string>> v
    {
        "1234", "15 foo", "bar", "42", "5000000000", " 5", std::nullopt, "-43"
    };

    for (auto&& x : v {{!
```

[](auto&& o)
{
// debug print the content of input optional<string>
std::cout << std::left << std::setw(13)
<< std::quoted(o.value_or("nullopt")) << " -> ";
return o
// if optional is nullopt convert it to optional with "" string
.or_else([]{ return std::optional{""s}; })
// flatmap from strings to ints (making empty optionals where it fails)
.and_then(to_int)
// map int to int + 1
.transform([](int n) { return n + 1; })
// convert back to strings
.transform([](int n) { return std::to_string(n); })
// replace all empty optionals that were left by
// and_then and ignored by transforms with "NaN"
.value_or("NaN"s);
}))
std::cout << x << '\n';
}
|output=
"1234"        -> 1235
"15 foo"      -> 16
"bar"         -> NaN
"42"          -> 43
"5000000000"  -> NaN
" 5"          -> NaN
"nullopt"     -> NaN
"-43"         -> -42

## See also


| cpp/utility/optional/dsc value_or | (see dedicated page) |
| cpp/utility/optional/dsc transform | (see dedicated page) |
| cpp/utility/optional/dsc or_else | (see dedicated page) |

