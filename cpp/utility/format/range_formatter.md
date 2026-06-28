---
title: std::range_formatter
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/range_formatter
---


```cpp
**Header:** `<`format`>`
dcl|since=c++23|1=
template< class T, class CharT = char >
requires std::same_as<std::remove_cvref_t<T>, T> && std::formattable<T, CharT>
class range_formatter;
```

`std::range_formatter` is a helper class template for implementing range `std::formatter` specializations.

## Range format specification

The syntax of *range-format-spec* is:

**Syntax:**

- `sdsc|`
- `*range-fill-and-align* (optional) *width* (optional) **`n`** *range-type* (optional) *range-underlying-spec* (optional)`
The *range-fill-and-align* is interpreted the same way as a *fill-and-align* except that the *fill* in *range-fill-and-align* is any character other than **`{`**, }, or **`:`**.
The *width* is described in `standard format width specification`.
The **`n`** option causes the range to be formatted without the opening and closing brackets.

```cpp
assert(std::format("{}", views::iota(1, 5)) == "[1, 2, 3, 4]");
assert(std::format("{:n}", views::iota(1, 5)) == "1, 2, 3, 4");
```

The *format-spec* in a *range-underlying-spec* (its syntax is equivalent to `:` *format-spec*), if any, is interpreted by the range element formatter `std::formatter<T, CharT>`.

```cpp
std::array ints{12, 10, 15, 14};

assert(std::format("{}", ints) == "[12, 10, 15, 14]");
assert(std::format("{::X}", ints) == "[C, A, F, E]");
assert(std::format("{:n:_^4}", ints) == "_12_, _10_, _15_, _14_");
```

The *range-type* changes the way a range is formatted, with certain options only valid with certain argument types.
The available range presentation types are:
* **`m`**: Indicates that the opening bracket should be `"{"`, the closing bracket should be c|"}", the separator should be `", "`, and each range element should be formatted as if **`m`** were specified for its *tuple-type* (in *tuple-format-spec*).
:* If **`m`** is chosen as the *range-type*, the program is ill-formed unless `T` is either a specialization of:
::* `std::pair`, or
::* `std::tuple` such that `1=std::tuple_size_v<T> == 2` is `true`.

```cpp
std::array char_pairs
{
    std::pair{'A', 5}, std::pair{'B', 10}, std::pair{'C', 12}
};

assert(std::format("{}", char_pairs) == "[('A', 5), ('B', 10), ('C', 12)]");
assert(std::format("{:m}", char_pairs) == "{'A': 5, 'B': 10, 'C': 12}");
```

* **`s`**: Indicates that the range should be formatted as a string.
* **`?s`**: Indicates that the range should be formatted as an `escaped string`.
:* If **`s`** or **`?s`** is chosen as the *range-type*, both **`n`** option and *range-underlying-spec* should not be included in the format specifier, and
:* the program is ill-formed unless `T` is `CharT`.

```cpp
std::array star{'S', 'T', 'A', 'R'};

assert(std::format("{}", star) == "['S', 'T', 'A', 'R']");
assert(std::format("{:s}", star) == "STAR");
assert(std::format("{:?s}", star) == "\"STAR\"");
```


## Data members


| Item | Description |
|------|-------------|
| **Member name** | Definition |


## Member functions

member|1=set_separator|2=

```cpp
dcl|1=
constexpr void set_separator( std::basic_string_view<CharT> sep ) noexcept;
```

Assigns `sep` to .
member|1=set_brackets|2=

```cpp
dcl|1=
constexpr void set_brackets( std::basic_string_view<CharT> opening,
std::basic_string_view<CharT> closing ) noexcept;
```

Assigns `opening` and `closing` to  and , respectively.
member|1=underlying|2=

```cpp
dcl|num=1|1=
constexpr std::formatter<T, CharT>& underlying();
dcl|num=2|1=
constexpr const std::formatter<T, CharT>& underlying() const;
```

Returns  (the underlying formatter).
member|1=parse|2=

```cpp
dcl|1=
template< class ParseContext >
constexpr auto parse( ParseContext& ctx ) -> ParseContext::iterator;
```

Parses the format specifiers as a *range-format-spec* and stores the parsed specifiers in the current object.
Calls  to parse *format-spec* in *range-format-spec* or, if the latter is not present, an empty *format-spec*.
If *range-type* or the **`n`** option is present, the values of , , and  are modified as required.
It calls  if:
* the *range-type* is neither **`s`** nor **`?s`**,
*  is a valid expression, and
* there is no *range-underlying-spec*.
Returns an iterator past the end of the *range-format-spec*.
member|1=format|2=

```cpp
dcl|1=
template< ranges::input_range R, class FormatContext >
requires std::formattable<ranges::range_reference_t<R>, CharT> &&
std::same_as<std::remove_cvref_t<ranges::range_reference_t<R>>, T>
auto format( R&& r, FormatContext& ctx ) const -> FormatContext::iterator;
```

If the *range-type* was either **`s`** or **`?s`**, it writes the formatted `std::basic_string<CharT>(std::from_range, r)` as a string or an escaped string, respectively, into `ctx.out()`.
Otherwise, it writes the following into `ctx.out()` as specified by *range-format-spec*, in order:
* ,
* for each formattable element `e` of the range `r`:
:* the result of writing `e` via , and
:* , unless `e` is the last element of `r`, and
* .
Returns an iterator past the end of the output range.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3892 | c++23 | the formatting of nested ranges was incorrect | corrected |


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |

