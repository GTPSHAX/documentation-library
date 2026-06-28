---
title: std::placeholders::_N
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/functional/placeholders
---


```cpp
**Header:** `<`functional`>`
dcl|
/* see below */ _1;
/* see below */ _2;
.
.
/* see below */ _N;
```

The `std::placeholders` namespace contains the placeholder objects `[_1, ..., _N]` where `N` is an implementation defined maximum number.
When used as an argument in a `std::bind` expression, the placeholder objects are stored in the generated function object, and when that function object is invoked with unbound arguments, each placeholder `_N` is replaced by the corresponding Nth unbound argument.
rev|until=c++17|
Each placeholder is declared as if by `extern /* unspecified */ _1;`.
rev|since=c++17|
Implementations are encouraged to declare the placeholders as if by `inline constexpr /* unspecified */ _1;`, although declaring them by `extern /* unspecified */ _1;` is still allowed by the standard.
The types of the placeholder objects are *DefaultConstructible* and *CopyConstructible*, their default copy/move constructors do not throw exceptions, and for any placeholder `_N`, the type `std::is_placeholder<decltype(_N)>` is defined, where `std::is_placeholder<decltype(_N)>` is derived from `std::integral_constant<int, N>`.

## Example


### Example

```cpp
#include <functional>
#include <iostream>
#include <string>

void goodbye(const std::string& s)
{
    std::cout << "Goodbye " << s << '\n';
}

class Object
{
public:
    void hello(const std::string& s)
    {
        std::cout << "Hello " << s << '\n';
    }
};

int main()
{
    using namespace std::placeholders;

    using ExampleFunction = std::function<void(const std::string&)>;
    Object instance;
    std::string str("World");

    ExampleFunction f = std::bind(&Object::hello, &instance, _1);
    f(str); // equivalent to instance.hello(str)

    f = std::bind(&goodbye, std::placeholders::_1);
    f(str); // equivalent to goodbye(str)

    auto lambda = [](std::string pre, char o, int rep, std::string post)
    {
        std::cout << pre;
        while (rep-- > 0)
            std::cout << o;
        std::cout << post << '\n';
    };

    // binding the lambda:
    std::function<void(std::string, char, int, std::string)> g =
        std::bind(&decltype(lambda)::operator(), &lambda, _1, _2, _3, _4);
    g("G", 'o', 'o'-'g', "gol");
}
```


**Output:**
```
Hello World
Goodbye World
Goooooooogol
```


## See also


| cpp/utility/functional/dsc bind | (see dedicated page) |
| cpp/utility/functional/dsc is_placeholder | (see dedicated page) |
| cpp/utility/tuple/dsc ignore | (see dedicated page) |

