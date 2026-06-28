---
title: keywords
type: Keywords
source: https://en.cppreference.com/w/cpp/keyword
---


# C++ keywords

This is a list of reserved keywords in C++. Since they are used by the language, these keywords are not available for re-definition or overloading.<sup>(since C++11)</sup>  As an exception, they are not considered reserved in


| - |
| A – C!!D – P!!R – Z |
| -style="vertical-align:top;" |
|  |
|  |
|  |

*  — alternative represenation (see below).
*  — meaning changed or new meaning added in C++11.
*  — new meaning added in C++14.
*  — meaning changed or new meaning added in C++17.
*  — meaning changed or new meaning added in C++20.
*  — new meaning added in C++23.
Note that: , , , , , , , , ,  and  (along with digraphs: `<%`, `%>`, `<:`, `:>`, `%:`, `%:%:`<sup>(until C++17)</sup> removed=yes| and trigraphs: `??<`, `??>`, `??(`, `??)`, `1=??=`, `??/`, `??'`, `??!`, `??-`) provide an alternative way to represent standard tokens.<sup>(since C++11)</sup>  These keywords are also considered reserved in attributes (excluding attribute argument lists), but some implementations handle them the same as the others.
In addition to keywords, there are ''identifiers with special meaning'', which may be used as names of objects or functions, but have special meaning in certain contexts.


| - |
|  |

Also, all  that contain a double underscore `__` in any position and each identifier that begins with an underscore followed by an uppercase letter is always reserved, and all identifiers that begin with an underscore are reserved for use as names in the global namespace. See  for more details.
The namespace `std` is used to place names of the standard C++ library. See Extending namespace std for the rules about adding names to it.
<sup>(since C++11)</sup> The name `posix` is reserved for a future top-level namespace. The behavior is undefined if a program declares or defines anything in that namespace.
The following tokens are recognized by the `preprocessor` when in context of a preprocessor directive:


| - |
|  |
|  |
|  |
|  |
|  |
|  |

The following tokens are recognized by the `preprocessor` ''outside'' the context of a preprocessor directive:


| - |
|  |


## See also

