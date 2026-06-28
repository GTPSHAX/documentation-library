---
title: std::basic_ios::imbue
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/imbue
---

ddcl|
std::locale imbue( const std::locale& loc );
Replaces the current locale. Effectively calls `ios_base::imbue(loc)` and if there is an associated stream buffer (`rdbuf() !), then calls `rdbuf()->pubimbue(loc)`.

## Parameters


### Parameters

- `loc` - the new locale

## Return value

The previous locale, as returned by `ios_base::imbue(loc)`.

## Example


### Example

```cpp
#include <iostream>
#include <locale>
#include <sstream>

int main()
{
    std::istringstream iss;
    iss.imbue(std::locale("en_US.UTF8"));

    std::cout << "Current locale: " << iss.getloc().name() << '\n';

    iss.imbue(std::locale());
    std::cout << "Global locale : " << iss.getloc().name() << '\n';
}
```


**Output:**
```
Current locale: en_US.UTF8
Global locale : C
```

