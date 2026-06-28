---
title: std::is_object
type: Metaprogramming
source: https://en.cppreference.com/w/cpp/types/is_object
---

cpp/types/traits/is|1=is_object
|description=
If `T` is an object type (that is any possibly cv-qualified type other than function, reference, or `void` types), provides the member constant `value` equal `true`. For any other type, `value` is `false`.
|inherit_desc=`T` is an object type

## Possible implementation

eq fun
|1=
template<class T>
struct is_object : std::integral_constant<bool,
std::is_scalar<T>::value
std::is_array<T>::value
std::is_union<T>::value
std::is_class<T>::value> {};

## Example


### Example

```cpp
#include <iomanip>
#include <iostream>
#include <type_traits>

#define IS_OBJECT(...) \
    std::cout << std::boolalpha << std::left << std::setw(9) << #__VA_ARGS__ \
              << (std::is_object_v<__VA_ARGS__> ? " is object\n" \
                                                : " is not an object\n")

int main()
{
    class cls {};

    IS_OBJECT(void);
    IS_OBJECT(int);
    IS_OBJECT(int&);
    IS_OBJECT(int*);
    IS_OBJECT(int*&);
    IS_OBJECT(cls);
    IS_OBJECT(cls&);
    IS_OBJECT(cls*);
    IS_OBJECT(int());
    IS_OBJECT(int(*)());
    IS_OBJECT(int(&)());
}
```


**Output:**
```
void      is not an object
int       is object
int&      is not an object
int*      is object
int*&     is not an object
cls       is object
cls&      is not an object
cls*      is object
int()     is not an object
int(*)()  is object
int(&)()  is not an object
```


## See also


| cpp/types/dsc is_scalar | (see dedicated page) |
| cpp/types/dsc is_array | (see dedicated page) |
| cpp/types/dsc is_union | (see dedicated page) |
| cpp/types/dsc is_class | (see dedicated page) |

