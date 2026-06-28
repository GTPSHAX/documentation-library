---
title: std::wstring_convert::wstring_convert
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/wstring_convert/wstring_convert
---


```cpp
dcl|num=1|
wstring_convert() : wstring_convert( new Codecvt ) {}
dcl|num=2|
explicit wstring_convert( Codecvt* pcvt );
dcla|num=3|
wstring_convert( Codecvt* pcvt, state_type state );
dcla|num=4|1=
explicit wstring_convert( const byte_string& byte_err,
const wide_string& wide_err = wide_string() );
dcl|num=5|since=c++14|1=
wstring_convert( const std::wstring_convert& ) = delete;
```


| rowspan=2 | Overload |
| colspan=5 | rlps | /#Data members |
| - |
| style="font-weight: normal;" | tti | byte_err_string |
| style="font-weight: normal;" | tti | wide_err_string |
| style="font-weight: normal;" | tti | cvtptr |
| style="font-weight: normal;" | tti | cvtstate |
| style="font-weight: normal;" | tti | cvtcount |
| - |
| v | 1 |
| rowspan=3 colspan=2 | [[cpp/language/default initialization | default-initialized]] |
| c | new Codecvt |
| rowspan=2 | default-initialized |
| rowspan=4 | uninitialized |
| - |
| v | 2 |
| rowspan=2 | c | pcvt |
| - |
| v | 3 |
| c | state |
| - |
| v | 4 |
| c | byte_err |
| c | wide_err |
| c | new Codecvt |
| c | state_type() |

@2,3@ If `pcvt` is a null pointer, the behavior is undefined.
5. The copy constructor is deleted, `wstring_convert` is not *CopyConstructible*.

## Parameters


### Parameters

- `pcvt` - pointer to the conversion facet
- `state` - initial value of the conversion shift state
- `byte_err` - narrow string to display on errors
- `wide_err` - wide string to display on errors

## Example


### Example

```cpp
#include <codecvt>
#include <locale>
#include <utility>

// utility wrapper to adapt locale-bound facets for wstring/wbuffer convert
template<class Facet>
struct deletable_facet : Facet
{
    using Facet::Facet; // inherit constructors
    ~deletable_facet() {}
};

int main()
{
    // UTF-16le / UCS4 conversion
    std::wstring_convert
        <std::codecvt_utf16<char32_t, 0x10ffff, std::little_endian>> u16to32;

    // UTF-8 / wide string conversion with custom messages
    std::wstring_convert<std::codecvt_utf8<wchar_t>> u8towide("Error!", L"Error!");

    // GB18030 / wide string conversion facet
    using F = deletable_facet<std::codecvt_byname<wchar_t, char, std::mbstate_t>>;
    std::wstring_convert<F> gbtowide(new F("zh_CN.gb18030"));
}
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-2176 | C++11 | constructors accepting single argument were implicit | made explicit |

