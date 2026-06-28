---
title: attribute: nodiscard
type: Language
source: https://en.cppreference.com/w/cpp/language/attributes/nodiscard
---

If a function declared `nodiscard` or a function returning an enumeration or class declared `nodiscard` by value is called from a discarded-value expression other than a cast to `void`, the compiler is encouraged to issue a warning.

## Syntax


**Syntax:**

- `|`
- `**``nodiscard``**`
- `|`
- `**``[[`nodiscard`(``** *string-literal* **``)]]``**`

### Parameters

- `{{spar` - string-literal|an unevaluated string literal that could be used to explain the rationale for why the result should not be discarded

## Explanation

Appears in a function declaration, enumeration declaration, or class declaration.
If, from a discarded-value expression other than a cast to `void`,
* a function declared `nodiscard` is called, or
* a function returning an enumeration or class declared `nodiscard` by value is called, or
* a constructor declared `nodiscard` is called by explicit type conversion or `cpp/language/static_cast`, or
* an object of an enumeration or class type declared `nodiscard` is initialized by explicit type conversion or `cpp/language/static_cast`,
the compiler is encouraged to issue a warning.
<sup>(since C++20)</sup> The *string-literal, if specified, is usually included in the warnings.*

## Example


### Example

```cpp
struct [[nodiscard]] error_info { /*...*/ };

error_info enable_missile_safety_mode() { /*...*/ return {}; }

void launch_missiles() { /*...*/ }

void test_missiles()
{
    enable_missile_safety_mode(); // compiler may warn on discarding a nodiscard value
    launch_missiles();
}

error_info& foo() { static error_info e; /*...*/ return e; }

void f1() { foo(); } // nodiscard type is not returned by value, no warning

// nodiscard( string-literal ) (since C++20):
[[nodiscard("PURE FUN")]] int strategic_value(int x, int y) { return x ^ y; }

int main()
{
    strategic_value(4, 2); // compiler may warn on discarding a nodiscard value
    auto z = strategic_value(0, 0); // OK: return value is not discarded
    return z;
}
```


**Output:**
```
game.cpp:5:4: warning: ignoring return value of function declared with ⮠
 'nodiscard' attribute
game.cpp:17:5: warning: ignoring return value of function declared with ⮠
 'nodiscard' attribute: PURE FUN
```

rrev|until=c++26|1=

## Standard library

The following standard functions are declared with `nodiscard` attribute:


#### Allocation functions

| cpp/memory/new/dsc operator new | (see dedicated page) |
| cpp/memory/allocator/dsc allocate | (see dedicated page) |
| cpp/memory/allocator_traits/dsc allocate | (see dedicated page) |
| cpp/memory/memory_resource/dsc allocate | (see dedicated page) |
| cpp/memory/polymorphic_allocator/dsc allocate | (see dedicated page) |
| cpp/memory/scoped_allocator_adaptor/dsc allocate | (see dedicated page) |

#### Indirect access

| cpp/utility/dsc launder | (see dedicated page) |
| cpp/memory/dsc assume_aligned | (see dedicated page) |

#### Emptiness-checking functions

| cpp/iterator/dsc empty | (see dedicated page) |
| cpp/container/dsc empty|array | (see dedicated page) |
| cpp/string/basic_string/dsc empty | (see dedicated page) |
| cpp/string/basic_string_view/dsc empty | (see dedicated page) |
| cpp/container/dsc empty|deque | (see dedicated page) |
| cpp/container/dsc empty|forward_list | (see dedicated page) |
| cpp/container/dsc empty|list | (see dedicated page) |
| cpp/container/dsc empty|map | (see dedicated page) |
| cpp/regex/match_results/dsc empty | (see dedicated page) |
| cpp/container/dsc empty|multimap | (see dedicated page) |
| cpp/container/dsc empty|multiset | (see dedicated page) |
| cpp/container/dsc empty|priority_queue | (see dedicated page) |
| cpp/container/dsc empty|queue | (see dedicated page) |
| cpp/container/dsc empty|set | (see dedicated page) |
| cpp/container/span/dsc empty | (see dedicated page) |
| cpp/container/dsc empty|stack | (see dedicated page) |
| cpp/container/dsc empty|unordered_map | (see dedicated page) |
| cpp/container/dsc empty|unordered_multimap | (see dedicated page) |
| cpp/container/dsc empty|unordered_multiset | (see dedicated page) |
| cpp/container/dsc empty|unordered_set | (see dedicated page) |
| cpp/container/dsc empty|vector | (see dedicated page) |
| cpp/filesystem/path/dsc empty | (see dedicated page) |

#### Miscellaneous

| cpp/thread/dsc async | (see dedicated page) |


## Defect reports


## References


## See also


| cpp/utility/tuple/dsc ignore | (see dedicated page) |

