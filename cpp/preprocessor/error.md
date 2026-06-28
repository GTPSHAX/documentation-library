---
title: Diagnostic directives
type: Language
source: https://en.cppreference.com/w/cpp/preprocessor/error
---


# Diagnostic directives

Shows the given error message and renders the program ill-formed<sup>(since C++23)</sup> , or shows the given warning message without affecting the validity of the program.

## Syntax


**Syntax:**

- `*diagnostic-message*`
- `|**`#warning`** *diagnostic-message*`

## Explanation

1. After encountering the `#error` directive, an implementation displays the message *diagnostic-message* and renders the program ill-formed (the compilation stops).
2. Same as , except the validity of the program is not affected and the compilation continues.
*diagnostic-message* can consist of several words not necessarily in quotes.

## Notes

Before its standardization in C++23, `#warning` has been provided by many compilers in all modes as a conforming extension.

## Example


### Example

```cpp
#if __STDC_HOSTED__ != 1
#   error "Not a hosted implementation"
#endif

#if __cplusplus >= 202302L
#   warning "Using #warning as a standard feature"
#endif

#include <iostream>

int main()
{
    std::cout << "The implementation used is hosted\n";
}
```


**Output:**
```
The implementation used is hosted
```


## References


## See also

