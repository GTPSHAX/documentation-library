---
title: keyword: goto
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword/goto
---


## Usage

* `cpp/language/goto` statement: as the declaration of the statement

## Example


### Example

```cpp
#include <cassert>
#include <string>

[[nodiscard]] auto get_first_line(const std::string& string)
{
    std::string first_line{};
    for (const auto character : string)
        switch (character)
        {
            case '\n':
                goto past_for; // breaks from 'range-for loop'
            default:
                first_line += character;
                break;
        }
past_for:
    return first_line;
}

int main()
{
    assert(get_first_line("Hello\nworld!") == "Hello");
}
```


## See also

