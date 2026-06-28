---
title: std::unique_ptr::get
type: Utilities
source: https://en.cppreference.com/w/cpp/memory/unique_ptr/get
---

ddcl|since=c++11|notes=|1=
pointer get() const noexcept;
Returns a pointer to the managed object or `nullptr` if no object is owned.

## Parameters

(none)

## Return value

Pointer to the managed object or `nullptr` if no object is owned.

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>
#include <utility>

class Res
{
    std::string s;

public:
    Res(std::string arg) : s{std::move(arg)}
    {
        std::cout << "Res::Res(" << std::quoted(s) << ");\n";
    }

    ~Res()
    {
        std::cout << "Res::~Res();\n";
    }

private:
    friend std::ostream& operator<<(std::ostream& os, Res const& r)
    {
        return os << "Res { s = " << std::quoted(r.s) << "; }";
    }
};

int main()
{
    std::unique_ptr<Res> up(new Res{"Hello, world!"});
    Res* res = up.get();
    std::cout << *res << '\n';
}
```


**Output:**
```
Res::Res("Hello, world!");
Res { s = "Hello, world!"; }
Res::~Res();
```


## See also


| cpp/memory/unique_ptr/dsc release | (see dedicated page) |

