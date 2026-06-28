---
title: std::moneypunct::pos_format
type: Localizations
source: https://en.cppreference.com/w/cpp/locale/moneypunct/pos_format
---


```cpp
**Header:** `<`locale`>`
dcl|num=1|1=
public:
pattern pos_format() const;
dcl|num=2|1=
public:
pattern neg_format() const;
dcl|num=3|1=
protected:
virtual pattern do_pos_format() const;
dcl|num=4|1=
protected:
virtual pattern do_neg_format() const;
```

1. Public member function, calls the member function `do_pos_format` of the most derived class.
2. Public member function, calls the member function `do_neg_format` of the most derived class.
3. Returns the format structure (of type `cpp/locale/money_base|std::money_base::format`) which describes the formatting of positive monetary values.
4. Returns the format structure (of type `cpp/locale/money_base|std::money_base::format`) which describes the formatting of negative monetary values.
The standard specializations of `std::moneypunct` return the pattern }.

## Return value

The object of type `cpp/locale/money_base|std::money_base::format` describing the formatting used by this locale.

## Notes

While `std::money_put` uses `pos_format` for formatting positive values and neg_format for formatting negative values, `std::money_get` uses `neg_format` for parsing all monetary values: it assumes that `neg_format` is compatible with `pos_format`.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>

struct my_punct : std::moneypunct_byname<char, false>
{
    my_punct(const char* name) : moneypunct_byname(name) {}
    pattern do_pos_format() const { return {value, space, symbol, sign}; }
    pattern do_neg_format() const { return {value, space, symbol, sign}; }
};

int main()
{
    std::cout.imbue(std::locale("en_US.utf8"));
    std::cout << "american locale: " << std::showbase
              << std::put_money(12345678.0) << '\n';

    std::cout.imbue(std::locale(std::cout.getloc(), new my_punct("en_US.utf8")));
    std::cout << "locale with modified moneypunct:\n"
              << std::put_money(12345678.0) << '\n'
              << std::put_money(-12345678.0) << '\n';
}
```


**Output:**
```
american locale: $123,456.78
locale with modified moneypunct:
123,456.78 $
123,456.78 $-
```


## See also


| cpp/locale/moneypunct/dsc do_curr_symbol | (see dedicated page) |
| cpp/locale/moneypunct/dsc do_positive_sign | (see dedicated page) |
| cpp/locale/money_get/dsc do_get | (see dedicated page) |
| cpp/locale/money_put/dsc do_put | (see dedicated page) |

