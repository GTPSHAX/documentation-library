---
title: std::codecvt::out
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt/out
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
result out( StateT& state,
const InternT* from,
const InternT* from_end,
const InternT*& from_next,
ExternT* to,
ExternT* to_end,
ExternT*& to_next ) const;
dcl|num=2|1=
protected:
virtual result do_out( StateT& state,
const InternT* from,
const InternT* from_end,
const InternT*& from_next,
ExternT* to,
ExternT* to_end,
ExternT*& to_next ) const;
```

1. Public member function, calls the member function `do_out` of the most derived class.
2. If this `codecvt` facet defines a conversion, translates the internal characters from the source range [from, from_end) to external characters, placing the results in the subsequent locations starting at `to`. Converts no more than `from_end - from` internal characters and writes no more than `to_end - to` external characters. Leaves `from_next` and `to_next` pointing one beyond the last element successfully converted.
If this `codecvt` facet does not define a conversion, no characters are converted. `to_next` is set to be equal to `to`, `state` is unchanged, and `std::codecvt_base::noconv` is returned.
`do_out(state, from, from + 1, from_next, to, to_end, to_next)` must return `ok` if
* this `codecvt` facet is used by `cpp/io/basic_filebuf`, and
* `do_out(state, from, from_end, from_next, to, to_end, to_next)` would return `ok` where `1=from != from_end`.

## Return value

A value of type `std::codecvt_base::result`, indicating the success status as follows:
The non-converting specialization `std::codecvt<char, char, std::mbstate_t>` always returns `std::codecvt_base::noconv`.

## Notes

Requires that `1=from <= from_end && to <= to_end` and that `state` either representing the initial shift state or obtained by converting the preceding characters in the sequence.
While `codecvt` supports N:M conversions (e.g. UTF-16 to UTF-8, where two internal characters may be necessary to decide what external characters to output), `std::basic_filebuf` can only use `codecvt` facets that define a 1:N conversion, that is it must be able to process one internal character at a time when writing to a file.
When performing N:M conversions, this function may return `std::codecvt_base::partial` after consuming all source characters (`1=from_next == from_end`). This means that another internal character is needed to complete the conversion (e.g. when converting UTF-16 to UTF-8, if the last character in the source buffer is a high surrogate).
The effect on `state` is deliberately unspecified. In standard facets, it is used to maintain shift state like when calling `std::wcsrtombs`, and is therefore updated to reflect the shift state after the last successfully converted character, but a user-defined facet is free to use it to maintain any other state, e.g. count the number of special characters encountered.

## Example


### Example

```cpp
#include <iostream>
#include <locale>
#include <string>

int main()
{
    std::locale::global(std::locale("en_US.utf8"));
    auto& f = std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>(std::locale());
    std::wstring internal = L"z\u00df\u6c34\U0001f34c"; // L"zß水🍌"

    // note that the following can be done with wstring_convert
    std::mbstate_t mb{}; // initial shift state
    std::string external(internal.size() * f.max_length(), '\0'); 
    const wchar_t* from_next;
    char* to_next;
    f.out(mb, &internal[0], &internal[internal.size()], from_next,
              &external[0], &external[external.size()], to_next);
    // error checking skipped for brevity
    external.resize(to_next - &external[0]);

    std::cout << "The string in narrow multibyte encoding: " << external << '\n';
}
```


**Output:**
```
The string in narrow multibyte encoding: zß水🍌
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-76 | C++98 | it was unclear whether the conversion is required<br>to support taking one internal character at a time | only required if used<br>by ltt |


## See also


| cpp/io/basic_filebuf/dsc overflow | (see dedicated page) |
| cpp/locale/wstring_convert/dsc to_bytes | (see dedicated page) |
| cpp/string/multibyte/dsc wcsrtombs | (see dedicated page) |
| cpp/locale/codecvt/dsc do_in | (see dedicated page) |

