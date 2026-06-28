---
title: #line directive
type: Language
source: https://en.cppreference.com/w/cpp/preprocessor/line
---


# Filename and line information

Changes the source code's line number and, optionally, the current file name, in the preprocessor.

## Syntax


**Syntax:**

- `*lineno* *new-line*`
- `*lineno* **`"`***filename***`"`** *new-line*`
- `*pp-tokens* *new-line*`
1. Changes the current preprocessor line number to *lineno*.
2. Also changes the current preprocessor file name to *filename*.
3. If neither  nor  is matched, *pp-tokens* will undergo macro replacement. The directive after replacement will be tried to match with  or  again.

### Parameters

- `{{spar` - new-line|The new-line character
- `{{spar` - lineno|A sequence of one or more decimal digits (`0` to `9`)<sup>(since C++14)</sup> , optional single quotes (`'`) may be inserted between the digits as a separator
- `{{spar` - filename|A sequence of one or more s-char﻿s (see )
- `{{spar` - pp-tokens|A sequence of one or more 

## Explanation

Expansions of the macro `__LINE__` beyond a `#line` directive will expand to *lineno* plus the number of actual source code lines encountered since. If *filename* is provided, expansions of the macro `__FILE__` from this point will produce filename.
If the decimal number specified by *lineno* is `0` or greater than <sup>(until C++11)</sup> `32767`<sup>(since C++11)</sup> `2147483647`, <sup>(until C++26)</sup> the behavior is undefined<sup>(since C++26)</sup> the program is ill-formed.

## Notes

This directive is used by some automatic code generation tools which produce C++ source files from a file written in another language. In that case, `#line` directives may be inserted in the generated C++ file referencing line numbers and the file name of the original (human-editable) source file.

## Example


### Example


**Output:**
```
test: test.cc:777: int main(): Assertion `2+2 == 5' failed.
```


## References


## See also


| cpp/utility/dsc source_location | (see dedicated page) |

