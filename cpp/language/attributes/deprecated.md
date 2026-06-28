---
title: attribute: deprecated
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes/deprecated
---

Indicates that the name or entity declared with this attribute is deprecated, that is, the use is allowed, but discouraged for some reason.

## Syntax


**Syntax:**

- `sdsc|num=1|1=`
- `**``deprecated``**`
- `sdsc|num=2|1=`
- `**``[[`deprecated`(``** *string-literal* **``)]]``**`

### Parameters

- `{{spar` - string-literal|an unevaluated string literal that could be used to explain the rationale for deprecation and/or to suggest a replacing entity

## Explanation

Indicates that the use of the name or entity declared with this attribute is allowed, but discouraged for some reason. Compilers typically issue warnings on such uses. The *string-literal*, if specified, is usually included in the warnings.
This attribute is allowed in declarations of the following names or entities:
* class/struct/union, e.g., `struct deprecated S;`,
* typedef-name, including those declared by alias declaration, e.g.,
:* `deprecated typedef S* PS;`,
:* `1=using PS deprecated = S*;`,
* (non-member) variable, e.g., `deprecated int x;`,
* static data member, e.g., c|struct S { deprecated static constexpr char CR{13}; };,
* non-static data member, e.g., },
* , e.g., `deprecated void f();`,
* , e.g., },
* enumeration, e.g., },
rrev|since=c++17|1=
* enumerator, e.g., },
* , e.g., }.
A name declared non-deprecated may be redeclared deprecated. A name declared deprecated cannot be un-deprecated by redeclaring it without this attribute.

## Example


### Example

```cpp
#include <iostream>

[[deprecated]]
void TriassicPeriod()
{
    std::clog << "Triassic Period: [251.9 - 208.5] million years ago.\n";
}

[[deprecated("Use NeogenePeriod() instead.")]]
void JurassicPeriod()
{
    std::clog << "Jurassic Period: [201.3 - 152.1] million years ago.\n";
}

[[deprecated("Use calcSomethingDifferently(int).")]]
int calcSomething(int x)
{
    return x * 2;
}

int main()
{
    TriassicPeriod();
    JurassicPeriod();
}
```


**Output:**
```
Triassic Period: [251.9 - 208.5] million years ago.
Jurassic Period: [201.3 - 152.1] million years ago.

main.cpp:20:5: warning: 'TriassicPeriod' is deprecated [-Wdeprecated-declarations]
    TriassicPeriod();
    ^
main.cpp:3:3: note: 'TriassicPeriod' has been explicitly marked deprecated here
[[deprecated]]
  ^
main.cpp:21:5: warning: 'JurassicPeriod' is deprecated: Use NeogenePeriod() instead ⮠
 [-Wdeprecated-declarations]
    JurassicPeriod();
    ^
main.cpp:8:3: note: 'JurassicPeriod' has been explicitly marked deprecated here
[[deprecated("Use NeogenePeriod() instead")]]
  ^
2 warnings generated.
```


## References


## See also

