---
title: std::get_money
type: Input/output
source: https://en.cppreference.com/w/cpp/io/manip/get_money
---

ddcl|header=iomanip|since=c++11|1=
template< class MoneyT >
/*unspecified*/ get_money( MoneyT& mon, bool intl = false );
When used in an expression `in >> get_money(mon, intl)`, parses the character input as a monetary value, as specified by the `std::money_get` facet of the locale currently imbued in `in`, and stores the value in `mon`.
The extraction operation in `in >> get_money(mon, intl)` behaves as a *FormattedInputFunction*.

## Parameters


### Parameters

- `mon` - variable where monetary value will be written. Can be either `long double` or `std::basic_string`
- `intl` - expects to find required international currency strings if `true`, expects optional currency symbols otherwise 

## Return value


## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <locale>
#include <sstream>

int main()
{
    std::istringstream in("$1,234.56 2.22 USD  3.33");
    long double v1, v2;
    std::string v3;

    in.imbue(std::locale("en_US.UTF-8"));
    in >> std::get_money(v1) >> std::get_money(v2) >> std::get_money(v3, true);

    if (in)
        std::cout << std::quoted(in.str()) << " parsed as: "
                  << v1 << ", " << v2 << ", " << v3 << '\n';
    else
        std::cout << "Parse failed";
}
```


**Output:**
```
"$1,234.56 2.22 USD  3.33" parsed as: 123456, 222, 333
```


## See also


| cpp/locale/dsc money_get | (see dedicated page) |
| cpp/io/manip/dsc put_money | (see dedicated page) |

