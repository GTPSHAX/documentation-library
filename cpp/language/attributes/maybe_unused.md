---
title: attribute: maybe_unused
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes/maybe_unused
---

Suppresses warnings on unused entities.

## Syntax


**Syntax:**

- `sdsc|`
- `**``maybe_unused``**`

## Explanation

This attribute can appear in the declaration of the following entities:
* class: `struct maybe_unused S;`
* `cpp/language/typedef`, including those declared by alias declaration: `maybe_unused typedef S* PS;`, `1=using PS maybe_unused = S*;`
* variable, including static data member: `maybe_unused int x;`
* non-static data member: },
* : `maybe_unused void f();`
* enumeration: }
* enumerator: }
* : `1=maybe_unused auto [a, b] = std::make_pair(42, 0.23);`
rrev|since=c++26|
* result binding: `post(r maybe_unused : this->empty())`
For entities declared `maybe_unused`, if the entities or their structured bindings are unused, the warning on unused entities issued by the compiler is suppressed.
rrev|since=c++26|
For labels declared `maybe_unused`, if they are unused, the warning on unused labels issued by the compiler is suppressed.

## Example


### Example

```cpp
#include <cassert>

[[maybe_unused]] void f([[maybe_unused]] bool thing1,
                        [[maybe_unused]] bool thing2)
{
    [[maybe_unused]] lbl: // the label “lbl” is not used, no warning
    [[maybe_unused]] bool b = not false and not true;
    assert(b); // in release mode, assert is compiled out, and “b” is unused
               // no warning because it is declared [[maybe_unused]]
} // parameters “thing1” and “thing2” are not used, no warning

int main() {}
```


## Defect reports


## References


## See also

