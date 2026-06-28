---
title: asm declaration
type: Language
source: https://en.cppreference.com/w/cpp/language/asm
---


# tt|asm

''asm-declaration'' gives the ability to embed assembly language source code within a C++ program. This declaration is <sup>(since C++11)</sup> conditionally-supported and implementation defined,
meaning that <sup>(since C++11)</sup> it may not be present and, even when provided by the implementation, it does not have a fixed meaning.

## Syntax


**Syntax:**

- `|`
- `*attr* (optional) **`asm (`** *string-literal* **`)`** **`;`**`
- `|`
- `*attr* (optional) **`asm (`** *balanced-token-seq* **`)`** **`;`**`

### Parameters

- `{{spar` - attr|<sup>(C++11)</sup> any number of `attributes`
- `{{spar` - string-literal|same as in `string literal`, including raw string literals
- `{{spar` - balanced-token-seq|a sequence of tokens where parentheses, brackets and braces are balanced; any restrictions on the *balanced-token-seq* and its meaning are implementation-defined

## Explanation

The *balanced-token-seq* is typically a string literal that represents a short program written in assembly language, which is executed whenever this declaration is executed. Different C++ compilers have wildly varying rules for asm-declarations, and different conventions for the interaction with the surrounding C++ code.
As other `block declarations`, this declaration can appear inside a block (a function body or another compound statement), and, as all other declarations, this declaration can also appear outside a block.

## Notes


## Keywords

`cpp/keyword/asm`

## Example


### Example

```cpp
#include <iostream>

extern "C" int func(int x);
// the definition of func is written in assembly language
// raw string literal could be very useful
asm(R"(
.globl func
    .type func, @function
    func:
    .cfi_startproc
    movl %edi, %eax /* x is in RDI, see x86-64 calling convention */
    addl $1, %eax
    ret
    .cfi_endproc
)");

int main()
{
    int n = func(0110);
    // formerly non-standard inline assembly, made comforming by P2361R6
    asm ("leal (%0,%0,4),%0"
         : "=r" (n)
         : "0" (n));
    std::cout << "73*5 = " << n << std::endl; // flush is intentional

    // standard inline assembly
    asm ("movq $60, %rax\n" // the exit syscall number on Linux
         "movq $2,  %rdi\n" // this program returns 2
         "syscall");
}
```


**Output:**
```
73*5 = 365
```


## Defect reports


### Defect Reports

| WG | Std | Before | After |
|----|------|--------|-------|
| cwg-195 | C++98 | it was required to support all asm declarations | made conditionally-supported |
| cwg-2262 | C++11 | attributes could not be applied to asm declarations | allowed |


## References


## See also

*

## External links

