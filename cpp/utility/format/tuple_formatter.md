---
title: std::formatter<pair-or-tuple>
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/format/tuple_formatter
---


# formattersmall|<''pair-or-tuple''>


```cpp
**Header:** `<`format`>`
dcl|since=c++23|1=
template< class CharT, std::formattable<CharT>... Ts >
struct formatter</*pair-or-tuple*/<Ts...>, CharT>;
```

The template specialization of `std::formatter` for the `std::pair` and `std::tuple` allows users to convert a pair or a tuple to its textual representation as a collection of elements using formatting functions.
The exposition-only name `/*pair-or-tuple*/` denotes either class template `std::pair` or `std::tuple`.
This specialization meets the *Formatter* requirements if `(std::formattable<const Ts, CharT> && ...)` is `true`. It always meets the *BasicFormatter* requirements.

## Format specification

The syntax of *tuple-format-spec* is:

**Syntax:**

- `sdsc|`
- `*tuple-fill-and-align* (optional) *width* (optional) *tuple-type* (optional)`
The *tuple-fill-and-align* is interpreted the same way as a *fill-and-align* except that the *fill* in *tuple-fill-and-align* is any character other than **`{`**, }, or **`:`**.
The *width* is described in `standard format width specification`.
The *tuple-type* changes the way a tuple is formatted, with certain options only valid with certain argument types.
The available tuple presentation types are:
* **`m`**: Indicates that both opening and closing brackets should be `""` while the separator should be `": "`.
:* If **`m`** is chosen as the *tuple-type*, the program is ill-formed unless `1=sizeof...(Ts) == 2` is `true`.
* **`n`**: Indicates that separator, opening and closing brackets should be `""`.

## Member objects


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
member|1=parse|2=

```cpp
dcl|1=
template< class ParseContext >
constexpr auto parse( ParseContext& ctx ) -> ParseContext::iterator;
```

Parses the format specifiers as a *tuple-format-spec* and stores the parsed specifiers in the current object.
If *tuple-type* or the **`n`** option is present, the values of , , and  are modified as required.
For each element `e` in , calls `e.parse(ctx)` to parse an empty *format-spec* and, if `e.set_debug_format()` is a valid expression, calls `e.set_debug_format()`.
Returns an iterator past the end of the *tuple-format-spec*.
member|1=format|2=

```cpp
dcl|1=
template< class FormatContext >
FormatContext::iterator
format( /*maybe-const-pair-or-tuple*/<Ts...>& elems, FormatContext& ctx ) const;
```

`/*maybe-const-pair-or-tuple*/` denotes:
* `const /*pair-or-tuple*/`, if `(std::formattable<const Ts, CharT> && ...)` is `true`,
* `/*pair-or-tuple*/` otherwise.
Writes the following into `ctx.out()` as specified by *tuple-format-spec*, in order:
* ,
* for each index `I` in [0, sizeof...(Ts)):
:* if `1=I != 0`, ,
:* the result of writing `std::get<I>(elems)` via , and
* .
Returns an iterator past the end of the output range.

## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-3892 | c++23 | the formatting of nested tuples was incorrect | corrected |


## See also


| cpp/utility/format/dsc formatter | (see dedicated page) |

