---
title: std::ios_base::precision
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/precision
---


```cpp
dcl|num=1|
streamsize precision() const;
dcl|num=2|
streamsize precision( streamsize new_precision );
```

Manages the precision (i.e. how many digits are generated) of floating point output performed by `std::num_put::do_put`.
1. Returns the current precision.
2. Sets the precision to the given one. Returns the previous precision.
The default precision, as established by `std::basic_ios::init`, is 6.

## Parameters


### Parameters

- `new_precision` - new precision setting

## Return value

The precision before the call to the function

## Example


### Example

```cpp
#include <iostream>

int main()
{
    const double d = 12.345678901234;
    std::cout << "The  default precision is " << std::cout.precision() << "\n\n";
    std::cout << "With default precision d is " << d << '\n';
    std::cout.precision(8);
    std::cout << "With high    precision d is " << d << '\n';
}
```


**Output:**
```
The  default precision is 6

With default precision d is 12.3457
With high    precision d is 12.345679
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| lwg-189 | C++98 | 'precision' was defined as 'the number of digits after<br>the decimal point', but it is not correct in some cases | corrected |


## See also


| cpp/io/ios_base/dsc width | (see dedicated page) |
| cpp/io/manip/dsc setprecision | (see dedicated page) |

