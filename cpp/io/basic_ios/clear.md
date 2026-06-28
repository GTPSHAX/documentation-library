---
title: std::basic_ios::clear
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/clear
---


```cpp
dcl|1=
void clear( std::ios_base::iostate state = std::ios_base::goodbit );
```

Sets the stream error state flags by assigning them the value of `state`. By default, assigns `std::ios_base::goodbit` which has the effect of clearing all error state flags.
If `rdbuf()` is a null pointer (i.e. there is no associated stream buffer), then `state  is assigned.

## Parameters


### Parameters

- `state` - new error state flags setting. It can be a combination of the following constants:

## Return value

(none)

## Exceptions

If the new error state includes a bit that is also included in the `exceptions()` mask, throws an exception of type `failure`.

## Example


### Example

```cpp
#include <iostream>
#include <string>

int main()
{
    for (char c : {'\n', '4', '1', '.', '3', '\n', 'Z', 'Y', 'X'})
        std::cin.putback(c); // emulate user's input (not portable: see ungetc Notes)

    double n;
    while (std::cout << "Please, enter a number: " && !(std::cin >> n))
    {
        std::cin.clear();
        std::string line;
        std::getline(std::cin, line);
        std::cout << line << "\nI am sorry, but '" << line << "' is not a number\n";
    }
    std::cout << n << "\nThank you for entering the number " << n << '\n';
}
```


**Output:**
```
Please, enter a number: XYZ
I am sorry, but 'XYZ' is not a number
Please, enter a number: 3.14
Thank you for entering the number 3.14
```


## Defect reports


## See also


| cpp/io/basic_ios/dsc setstate | (see dedicated page) |
| cpp/io/basic_ios/dsc rdstate | (see dedicated page) |

