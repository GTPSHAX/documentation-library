---
title: va_start
type: Utilities
source: https://en.cppreference.com/w/cpp/utility/variadic/va_start
---


```cpp
**Header:** `<`cstdarg`>`
dcl rev multi|until1=c++26|dcl1=
void va_start( std::va_list ap, parmN );
|dcl2=
void va_start( std::va_list ap, ... );
```

The `va_start` macro enables access to the variable arguments<sup>(until C++26)</sup> following the named argument `parmN`.
`va_start` shall be invoked with an instance to a valid `std::va_list` object `ap` before any calls to `va_arg`.
rev|until=c++26|
rrev|since=c++11|
If `parm_n` is a  or an entity resulting from a , the program is ill-formed, no diagnostic required.
If `parm_n` is of reference type, or of a type not compatible with the type that results from default argument promotions, the behavior is undefined.
rev|since=c++26|
If more than one argument is present for `va_start`, the preprocessing tokens comprising the second and subsequent arguments are discarded. If any of those arguments expands to include unbalanced parentheses, or a preprocessing token that does not convert to a token, the program is ill-formed, no diagnostic required.

## Parameters


### Parameters

- `ap` - an object of the `va_list` type
- `parm_n` - the named parameter preceding the first variable parameter

## Expanded value

(none)

## Notes

rrev|until=c++26|
`va_start` is required to support `parm_n` with overloaded `operator&`.

## Example


### Example

```cpp
#include <cstdarg>
#include <iostream>

int add_nums(int count...)
{
    int result = 0;
    std::va_list args;
    va_start(args, count); // count can be omitted since C++26
    for (int i = 0; i < count; ++i)
        result += va_arg(args, int);
    va_end(args);
    return result;
}

int main()
{
    std::cout << add_nums(4, 25, 25, 50, 50) << '\n';
}
```


**Output:**
```
150
```


## Defect reports


## See also


| cpp/utility/variadic/dsc va_arg | (see dedicated page) |
| cpp/utility/variadic/dsc va_end | (see dedicated page) |

