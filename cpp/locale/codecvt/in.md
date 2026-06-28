---
title: std::codecvt::in
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/codecvt/in
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
result in( StateT& state,
const ExternT* from,
const ExternT* from_end,
const ExternT*& from_next,
InternT* to,
InternT* to_end,
InternT*& to_next ) const;
dcl|num=2|1=
protected:
virtual result do_in( StateT& state,
const ExternT* from,
const ExternT* from_end,
const ExternT*& from_next,
InternT* to,
InternT* to_end,
InternT*& to_next ) const;
```

1. Public member function, calls the member function `do_in` of the most derived class.
2. If this `codecvt` facet defines a conversion, translates the external characters from the source range [from, from_end) to internal characters, placing the results in the subsequent locations starting at `to`. Converts no more than `from_end - from` external characters and writes no more than `to_end - to` internal characters. Leaves `from_next` and `to_next` pointing one beyond the last element successfully converted.
If this `codecvt` facet does not define a conversion, no characters are converted. `to_next` is set to be equal to `to`, `state` is unchanged, and `std::codecvt_base::noconv` is returned.
`do_in(state, from, from_end, from_next, to, to + 1, to_next)` must return `ok` if
* this `codecvt` facet is used by `cpp/io/basic_filebuf`, and
* `do_in(state, from, from_end, from_next, to, to_end, to_next)` would return `ok` where `1=to != to_end`.

## Return value

A value of type `std::codecvt_base::result`, indicating the success status as follows:
The non-converting specialization `std::codecvt<char, char, std::mbstate_t>` always returns `std::codecvt_base::noconv`.

## Notes

Requires that `1=from <= from_end && to <= to_end` and that `state` either representing the initial shift state or obtained by converting the preceding characters in the sequence.
The effect on `state` is deliberately unspecified. In standard facets, it is used to maintain shift state like when calling `std::mbsrtowcs`, and is therefore updated to reflect the conversion state after the last processed external character, but a user-defined facet is free to use it to maintain any other state, e.g. count the number of special characters encountered.

## Example


### Example

```cpp
#include <iostream>
#include <locale>
#include <string>

int main()
{
    std::locale::global(std::locale("en_US.utf8"));
    auto const& f = std::use_facet<std::codecvt<wchar_t, char, std::mbstate_t>>
        (std::locale());
    std::string external = "z\u00df\u6c34\U0001d10b"; // or u8"zß水𝄋"
                     // or "\x7a\xc3\x9f\xe6\xb0\xb4\xf0\x9d\x84\x8b"

    // note that the following can be done with wstring_convert
    std::mbstate_t mb = std::mbstate_t(); // initial shift state
    std::wstring internal(external.size(), '\0'); 
    const char* from_next;
    wchar_t* to_next;
    f.in(mb, &external[0], &external[external.size()], from_next,
             &internal[0], &internal[internal.size()], to_next);
    // error checking skipped for brevity
    internal.resize(to_next - &internal[0]);

    std::wcout << L"The string in wide encoding: " << internal << '\n';
}
```


**Output:**
```
The string in wide encoding: zß水𝄋
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-76 | C++98 | it was unclear whether the conversion is required to<br>support producing one internal character at a time | only required if used<br>by ltt |


## See also


| cpp/io/basic_filebuf/dsc underflow | (see dedicated page) |
| cpp/locale/wstring_convert/dsc from_bytes | (see dedicated page) |
| cpp/string/multibyte/dsc mbsrtowcs | (see dedicated page) |
| cpp/locale/codecvt/dsc do_out | (see dedicated page) |

