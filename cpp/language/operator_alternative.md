---
title: Alternative operator representations
type: Language
source: https://en.cppreference.com/w/cpp/language/operator_alternative
---


# Alternative operator representations

C++ (and C) source code may be written in any non-ASCII 7-bit character set that includes the [ISO 646|ISO 646:1983](https://en.wikipedia.org/wiki/ISO 646|ISO 646:1983) invariant character set. However, several C++ operators and punctuators require characters that are outside of the ISO 646 codeset: }. To be able to use character encodings where some or all of these symbols do not exist (such as the German [DIN 66003](https://en.wikipedia.org/wiki/DIN 66003)), C++ defines the following alternatives composed of ISO 646 compatible characters.

## Alternative tokens

There are alternative spellings for several operators and other tokens that use non-ISO646 characters. In all respects of the language, each alternative token behaves exactly the same as its primary token, except for its spelling (the stringification operator can make the spelling visible). The two-letter alternative tokens are sometimes called "digraphs". Despite being four-letters long, `%:%:` is also considered a digraph.


| - |
| Primary |
| Alternative |
| - |
| tt | && |
| ltt | cpp/keyword/and |
| - |
| tt | 1=&= |
| ltt | cpp/keyword/and_eq |
| - |
| tt | & |
| ltt | cpp/keyword/bitand |
| - |
| tt | &#124; |
| ltt | cpp/keyword/bitor |
| - |
| tt | ~ |
| ltt | cpp/keyword/compl |
| - |
| tt | ! |
| ltt | cpp/keyword/not |
| - |
| tt | 1=!= |
| ltt | cpp/keyword/not_eq |
| - |
| tt | &#124;&#124; |
| ltt | cpp/keyword/or |
| - |
| tt | 1=&#124;= |
| ltt | cpp/keyword/or_eq |
| - |
| tt | ^ |
| ltt | cpp/keyword/xor |
| - |
| tt | 1=^= |
| ltt | cpp/keyword/xor_eq |
| - |
| tt | { | tt | <% |
| - |
| tt | } | tt | %> |
| - |
| tt | [ | tt | <: |
| - |
| tt | ] | tt | :> |
| - |
| tt | # | tt | %: |
| - |
| tt | ## | tt | %:%: |


## Trigraphs

The following three-character groups (trigraphs) are `parsed before comments and string literals are recognized`, and each appearance of a trigraph is replaced by the corresponding primary character:


| -style="text-align: left;" |
| Primary |
| Trigraph |
| - |
| tt | { | tt | ??< |
| - |
| tt | } | tt | ??> |
| - |
| tt | [ | tt | ??( |
| - |
| tt | ] | tt | ??) |
| - |
| tt | # | tt | 1=??= |
| - |
| tt | \ | tt | ??/ |
| - |
| tt | ^ | tt | ??' |
| - |
| tt | <nowiki> | </nowiki> | tt | ??! |
| - |
| tt | ~ | tt | ??- |

Because trigraphs are processed early, a comment such as `// Will the next line be executed?????/` will effectively comment out the following line, and the string literal such as `"Enter date ??/??/??"` is parsed as `"Enter date \\??"`.

## Notes

The characters `&` and `!` are invariant under ISO-646, but alternatives are provided for the tokens that use these characters anyway to accommodate even more restrictive historical charsets.
There is no alternative spelling (such as `eq`) for the equality operator `1===` because the character `1==` was present in all supported charsets.

## Compatibility with C

The same words are defined in the C programming language in the include file  as macros. Because in C++ these are built into the language, the C++ version of `cpp/header/ciso646|<iso646.h>`, as well as , does not define anything. The non-word digraphs (e.g `<%`), however, are part of the core language and can be used without including any header (otherwise, they would be unusable on any charset that lacks `#`).

## Keywords

`cpp/keyword/and`,
`cpp/keyword/and_eq`,
`cpp/keyword/bitand`,
`cpp/keyword/bitor`,
`cpp/keyword/compl`,
`cpp/keyword/not`,
`cpp/keyword/not_eq`,
`cpp/keyword/or`,
`cpp/keyword/or_eq`,
`cpp/keyword/xor`,
`cpp/keyword/xor_eq`

## Example


### Example

```cpp
%:include <iostream>

struct X
<%
    compl X() <%%> // destructor
    X() <%%>
    X(const X bitand) = delete; // copy constructor
    // X(X and) = delete; // move constructor

    bool operator not_eq(const X bitand other)
    <%
       return this not_eq bitand other;
    %>
%>;

int main(int argc, char* argv<::>) 
<%
    // lambda with reference-capture:
    auto greet = <:bitand:>(const char* name)
    <%
        std::cout << "Hello " << name
                  << " from " << argv<:0:> << '\n';
    %>;

    if (argc > 1 and argv<:1:> not_eq nullptr)
        greet(argv<:1:>);
    else
        greet("Anon");
%>
```


**Output:**
```
Hello Anon from ./a.out
```


## References


## See also

