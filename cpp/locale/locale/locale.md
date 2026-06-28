---
title: std::locale::locale
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/locale/locale
---


```cpp
dcl rev multi|num=1|until1=c++11
|dcl1=
locale() throw();
|dcl2=
locale() noexcept;
dcl rev multi|num=2|until1=c++11
|dcl1=
locale( const locale& other ) throw();
|dcl2=
locale( const locale& other ) noexcept;
dcl|num=3|
explicit locale( const char* std_name );
dcl|num=4|since=c++11|
explicit locale( const std::string& std_name );
dcl|num=5|
locale( const locale& other, const char* std_name, category cats );
dcl|num=6|since=c++11|
locale( const locale& other, const std::string& std_name, category cats );
dcla|num=7|
template< class Facet >
locale( const locale& other, Facet* f );
dcl|num=8|
locale( const locale& other, const locale& one, category cats );
```

Constructs a new locale object.
1. Default constructor. Constructs a copy of the global C++ locale, which is the locale most recently used as the argument to `std::locale::global` or a copy of `std::locale::classic()` if no call to `std::locale::global` has been made.
2. Copy constructor. Constructs a copy of `other`.
@3,4@ Constructs a copy of the system locale with specified `std_name` (such as `"C"`, or `"POSIX"`, or `"en_US.UTF-8"`, or `"English_US.1251"`), if such locale is supported by the operating system. The locale constructed in this manner has a name.
4. Equivalent to `locale(std_name.c_str())`.
5. Constructs a copy of `other` except for all the facets identified by the `cats` argument, which are copied from the system locale identified by its `std_name`. The locale constructed in this manner has a name if and only if `other` has a name.
6. Equivalent to `locale(other, std_name.c_str(), cats)`.
7. Constructs a copy of `other` except for the facet of type `Facet` (typically deduced from the type of the argument) which is installed from `f`. If `f` is a null pointer, the constructed locale is a full copy of `other`. The program is ill-formed if `Facet` is not a `facet` or it is a volatile-qualified facet.
@@ If `f` is null, the constructed locale has the same name as `other`. Otherwise, the constructed locale has no name.
8. Constructs a copy of `other` except for all the facets identified by the `cats` argument, which are copied from `one`.
@@ If `cats` is equal to `locale::none`, the constructed locale has a name if and only if `other` has a name. Otherwise, the constructed locale has a name if and only if `other` and `one` both have names.

## Parameters


### Parameters

- `other` - another locale to copy
- `std_name` - name of the system locale to use
- `f` - pointer to a facet to merge with `other`
- `cats` - the facet categories used to identify the facets to merge with `other`
- `one` - another locale to take facets from

## Exceptions

@3,5@ `std::runtime_error` if the operating system has no locale named `std_name` or if `std_name` is a null pointer.
@4,6@ `std::runtime_error` if the operating system has no locale named `std_name`.

## Notes

Overload  is typically called with its second argument, `f`, obtained directly from a new-expression: the locale is responsible for calling the matching `delete` from its own destructor.

## Example


### Example

```cpp
#include <codecvt>
#include <iostream>
#include <locale>

std::ostream& operator<< (std::ostream& os, const std::locale& loc)
{
    if (loc.name().length() <= 80)
        os << loc.name();
    else
        for (const auto c : loc.name())
            os << c << (c == ';' ? "\n  " : "");

    return os << '\n';
}

int main()
{
    std::locale l1;
    std::cout << "Name of a copy of the classic \"C\" locale: " << l1;

    std::locale l2("en_US.UTF-8");
    std::cout << "Name of unicode locale: " << l2;

    std::locale l3(l1, new std::codecvt_utf8<wchar_t>);
    std::cout << "Name of \"C\" locale except for codecvt: " << l3;

    std::locale l4(l1, l2, std::locale::ctype);
    std::cout << "Name of \"C\" locale except for ctype, which is unicode:\n  " << l4;
}
```


**Output:**
```
Name of a copy of the classic "C" locale: C
Name of unicode locale: en_US.UTF-8
Name of "C" locale except for codecvt: *
Name of "C" locale except for ctype, which is unicode:
  LC_CTYPE=en_US.UTF-8;
  LC_NUMERIC=C;
  LC_TIME=C;
  LC_COLLATE=C;
  LC_MONETARY=C;
  LC_MESSAGES=C;
  LC_PAPER=C;
  LC_NAME=C;
  LC_ADDRESS=C;
  LC_TELEPHONE=C;
  LC_MEASUREMENT=C;
  LC_IDENTIFICATION=C
```


## Defect reports


## See also


| cpp/locale/locale/dsc ~locale | (see dedicated page) |


## External links

