---
title: std::time_get::do_date_order
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/time_get/date_order
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|
public:
dateorder date_order() const;
dcl|num=2|
protected:
virtual dateorder do_date_order() const;
```

1. Public member function, calls the protected virtual member function `do_date_order` of the most derived class.
2. Returns a value of type `std::time_base::dateorder`, which describes the default date format used by this locale (expected by `get_date()` and produced by `std::strftime()` with format specifier `'%x'`).
The valid values (inherited from `std::time_base`) are:

## Return value

A value of type `dateorder`.

## Notes

This function is optional, it may return `no_order` in every case.

## Example


### Example

```cpp
#include <iostream>
#include <locale>

void show_date_order()
{
    std::time_base::dateorder d =
        std::use_facet<std::time_get<char>>(std::locale()).date_order();
    switch (d)
    {
        case std::time_base::no_order:
            std::cout << "no_order\n";
            break;
        case std::time_base::dmy:
            std::cout << "day, month, year\n";
            break;
        case std::time_base::mdy:
            std::cout << "month, day, year\n";
            break;
        case std::time_base::ymd:
            std::cout << "year, month, day\n";
            break;
        case std::time_base::ydm:
            std::cout << "year, day, month\n";
            break;
    }
}

int main()
{
    std::locale::global(std::locale("en_US.utf8"));
    std::cout << "In U.S. locale, the default date order is: ";
    show_date_order();

    std::locale::global(std::locale("ja_JP.utf8"));
    std::cout << "In Japanese locale, the default date order is: ";
    show_date_order();

    std::locale::global(std::locale("de_DE.utf8"));
    std::cout << "In German locale, the default date order is: ";
    show_date_order();
}
```


**Output:**
```
In U.S. locale, the default date order is: month, day, year
In Japanese locale, the default date order is: year, month, day
In German locale, the default date order is: day, month, year
```


## See also


| cpp/locale/time_get/dsc do_get_date | (see dedicated page) |
| cpp/locale/dsc time_base | (see dedicated page) |

