---
title: std::sprintf
type: Input/output
source: https://en.cppreference.com/w/cpp/io/c/fprintf
---


```cpp
**Header:** `<`cstdio`>`
dcl|num=1|
int printf( const char* format, ... );
dcl|num=2|
int fprintf( std::FILE* stream, const char* format, ... );
dcl|num=3|
int sprintf( char* buffer, const char* format, ... );
dcl|num=4|since=c++11|
int snprintf( char* buffer, std::size_t buf_size, const char* format, ... );
```

Loads the data from the given locations, converts them to character string equivalents and writes the results to a variety of sinks.
1. Writes the results to `stdout`.
2. Writes the results to a file stream `stream`.
3. Writes the results to a character string `buffer`.
4. Writes the results to a character string `buffer`. At most `buf_size - 1` characters are written. The resulting character string will be terminated with a null character, unless `buf_size` is zero. If `buf_size` is zero, nothing is written and `buffer` may be a null pointer, however the return value (number of bytes that would be written not including the null terminator) is still calculated and returned.
If a call to `sprintf` or `snprintf` causes copying to take place between objects that overlap, the behavior is undefined (e.g. `sprintf(buf, "%s text", buf);`).

## Parameters


### Parameters

- `stream` - output file stream to write to
- `buffer` - pointer to a character string to write to
- `buf_size` - up to `buf_size - 1` characters may be written, plus the null terminator
- `format` - pointer to a null-terminated multibyte string specifying how to interpret the data
- `...` - arguments specifying data to print. If any argument after  is not the type expected by the corresponding conversion specification (the expected type is the promoted type or a compatible type of the promoted type), or if there are fewer arguments than required by `format`, the behavior is undefined. If there are more arguments than required by `format`, the extraneous arguments are evaluated and ignored

## Return value

@1,2@ Number of characters written if successful or a negative value if an error occurred.
3. Number of characters written if successful (not including the terminating null character) or a negative value if an error occurred.
4. Number of characters that would have been written for a sufficiently large buffer if successful (not including the terminating null character), or a negative value if an error occurred. Thus, the (null-terminated) output has been completely written if and only if the returned value is nonnegative and less than `buf_size`.

## Notes

Calling `std::snprintf` with zero `buf_size` and null pointer for `buffer` is useful (when the overhead of double-call is acceptable) to determine the necessary buffer size to contain the output:

```cpp
auto fmt = "sqrt(2) = %f";
int sz = std::snprintf(nullptr, 0, fmt, std::sqrt(2));
std::vector<char> buf(sz + 1); // note +1 for null terminator
std::sprintf(buf.data(), fmt, std::sqrt(2)); // certain to fit
```


## Example


### Example

```cpp
#include <cinttypes>
#include <cstdint>
#include <cstdio>
#include <limits>

int main()
{
    const char* s = "Hello";
    std::printf("Strings:\n"); // same as std::puts("Strings:");
    std::printf("\t[%10s]\n", s);
    std::printf("\t[%-10s]\n", s);
    std::printf("\t[%*s]\n", 10, s);
    std::printf("\t[%-10.*s]\n", 4, s);
    std::printf("\t[%-*.*s]\n", 10, 4, s);

    std::printf("Characters:\t%c %%\n", 'A');

    std::printf("Integers:\n");
    std::printf("\tDecimal:    \t%i %d %.6i %i %.0i %+i %i\n",
                                  1, 2,   3, 0,   0,  4,-4);
    std::printf("\tHexadecimal:\t%x %x %X %#x\n",
                                  5,10,10,  6);
    std::printf("\tOctal:      \t%o %#o %#o\n",
                                 10, 10,  4);

    std::printf("Floating point:\n");
    std::printf("\tRounding:\t%f %.0f %.32f\n", 1.5, 1.5, 1.3);
    std::printf("\tPadding:\t%05.2f %.2f %5.2f\n", 1.5, 1.5, 1.5);
    std::printf("\tScientific:\t%E %e\n", 1.5, 1.5);
    std::printf("\tHexadecimal:\t%a %A\n", 1.5, 1.5);
    std::printf("\tSpecial values:\t0/0=%g 1/0=%g\n", 0.0/0.0, 1.0/0.0);

    std::printf("Variable width control:\n");
    std::printf("\tright-justified variable width: '%*c'\n", 5, 'x');
    int r = std::printf("\tleft-justified variable width : '%*c'\n", -5, 'x');
    std::printf("(the last printf printed %d characters)\n", r);

    std::printf("Fixed-width types:\n");
    std::uint32_t val = std::numeric_limits<std::uint32_t>::max();
    std::printf("\tLargest 32-bit value is %" PRIu32 " or %#" PRIx32 "\n",
                                                 val,            val);
}
```


**Output:**
```
Strings:
	[     Hello]
	[Hello     ]
	[     Hello]
	[Hell      ]
	[Hell      ]
Characters:	A %
Integers:
	Decimal:    	1 2 000003 0  +4 -4
	Hexadecimal:	5 a A 0x6
	Octal:      	12 012 04
Floating point:
	Rounding:	1.500000 2 1.30000000000000004440892098500626
	Padding:	01.50 1.50  1.50
	Scientific:	1.500000E+00 1.500000e+00
	Hexadecimal:	0x1.8p+0 0X1.8P+0
	Special values:	0/0=-nan 1/0=inf
Variable width control:
	right-justified variable width: '    x'
	left-justified variable width : 'x    '
(the last printf printed 41 characters)
Fixed-width types:
	Largest 32-bit value is 4294967295 or 0xffffffff
```


## See also


| cpp/io/c/dsc fwprintf | (see dedicated page) |
| cpp/io/c/dsc vfprintf | (see dedicated page) |
| cpp/io/c/dsc fputs | (see dedicated page) |
| cpp/io/c/dsc fscanf | (see dedicated page) |
| cpp/utility/dsc to_chars | (see dedicated page) |
| cpp/io/dsc print | (see dedicated page) |
| cpp/io/dsc println | (see dedicated page) |

