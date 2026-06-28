---
title: Namespace aliases
type: Language
source: https://en.cppreference.com/w/cpp/language/namespace_alias
---


# Namespace aliases

Namespace aliases allow the programmer to define an alternate name for a namespace.
They are commonly used as a convenient shortcut for long or deeply-nested namespaces.

## Syntax


**Syntax:**

- `sdsc|num=1|`
- `**`namespace`** *alias_name*  *ns_name***`;`**`
- `sdsc|num=2|`
- `**`namespace`** *alias_name*  **`::`***ns_name***`;`**`
- `sdsc|num=3|`
- `**`namespace`** *alias_name*  *nested_name***`::`***ns_name***`;`**`
- `|`
- `**`namespace`** *alias_name*  *splice-specifier***`;`**`

### Parameters

- `{{spar` - alias_name|an identifier
- `{{spar` - ns_name|a (possibly `qualified`) identifier that names a namespace or namespace alias
- `{{spar` - splice-specifier|a `splice specifier` that designates a namespace that is not the global namespace

## Explanation

The new alias *alias_name* provides an alternate method of accessing *ns_name*<sup>(since C++26)</sup>  or the namespace designated by *splice-specifier*.
*alias_name* must be a name not previously used. *alias_name* is valid for the duration of the scope in which it is introduced.

## Keywords

`cpp/keyword/namespace`

## Example


### Example

```cpp
#include <iostream>

namespace foo
{
    namespace bar
    {
         namespace baz
         {
             int qux = 42;
         }
    }
}

namespace fbz = foo::bar::baz;

int main()
{
    std::cout << fbz::qux << '\n';
}
```


**Output:**
```
42
```


## See also


| cpp/language/dsc namespace | (see dedicated page) |
| cpp/language/dsc type alias | (see dedicated page) |

