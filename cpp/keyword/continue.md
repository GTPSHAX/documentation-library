---
title: keyword: continue
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/continue
---


## Usage

* `continue` statement: as the declaration of the statement

## Example


### Example

```cpp
#include <iostream>
#include <string>

[[nodiscard]] constexpr auto get_digits(const std::string& string) noexcept
{
    std::string digits{};

    for (const auto& character: string)
    {
        if (character < '0' {{!!
```

continue; // conditionally skips the following statement
digits += character;
}
return digits;
}
int main() noexcept
{
std::cout << get_digits("H3LL0, W0RLD!");
}
|output=
300

## See also

