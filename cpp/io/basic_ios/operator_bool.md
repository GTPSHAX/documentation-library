---
title: std::basic_ios::operator bool
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_ios/operator_bool
---


```cpp
dcl|num=1|until=c++11|
operator /* unspecified-boolean-type */() const;
dcl|num=2|since=c++11|
explicit operator bool() const;
```

Checks whether the stream has no errors.
1. Returns a value that evaluates to `false` in a boolean context if `fail()` returns `true`, otherwise returns a value that evaluates to `true` in a boolean context.
2. Returns `true` if the stream has no errors and is ready for I/O operations. Specifically, returns `!fail()`.
This operator makes it possible to use streams and functions that return references to streams as loop conditions, resulting in the idiomatic C++ input loops such as } or }. Such loops execute the loop's body only if the input operation succeeded.

## Parameters

(none)

## Return value

1. A value that evaluates to `true` in a boolean context if the stream has no errors, a value that evaluates to `false` in a boolean context otherwise.
2. `true` if the stream has no errors, `false` otherwise.

## Notes

This conversion can be used in contexts where a `bool` is expected (e.g. an if condition). However, implicit conversions (e.g. to `int`) that can occur with `bool` are not allowed.
In C++98, `operator bool` could not be provided directly due to the safe bool problem. The initial solution in C++98 is to provide `operator void*`, which returns a null pointer if `fail()` returns `true` or a non-null pointer otherwise. It is replaced by the resolution of , which allows [https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms/Safe_bool Safe Bool idiom] to be applied.
Since C++11, conversion functions can be `cpp/language/explicit`. The resolution of  introduced the explicit `operator bool` and the boolean conversion is now safe.

## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::istringstream s("1 2 3 error");
    int n;

    std::cout << std::boolalpha << "s is " << static_cast<bool>(s) << '\n';
    while (s >> n)
        std::cout << n << '\n';
    std::cout << "s is " << static_cast<bool>(s) << '\n';
}
```


**Output:**
```
s is true
1
2
3
s is false
```


## Defect reports


## See also

