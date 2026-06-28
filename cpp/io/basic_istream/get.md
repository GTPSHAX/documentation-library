---
title: std::basic_istream::get
type: Input/output
source: https://en.cppreference.com/w/cpp/io/basic_istream/get
---


```cpp
dcl|num=1|
int_type get();
dcl|num=2|
basic_istream& get( char_type& ch );
dcl|num=3|
basic_istream& get( char_type* s, std::streamsize count );
dcl|num=4|
basic_istream& get( char_type* s, std::streamsize count, char_type delim );
dcl|num=5|
basic_istream& get( basic_streambuf& strbuf );
dcl|num=6|
basic_istream& get( basic_streambuf& strbuf, char_type delim );
```

Extracts character or characters from stream.
All versions behave as *UnformattedInputFunction*s. After constructing and checking the sentry object, these functions perform the following:
1. Reads one character and returns it if available. Otherwise, returns `Traits::eof()` and sets `failbit` and `eofbit`.
2. Reads one character and stores it to `ch` if available. Otherwise, leaves `ch` unmodified and sets `failbit` and `eofbit`. Note that this function is not overloaded on the types `signed char` and `unsigned char`, unlike the formatted character input operator>>.
3. Same as `get(s, count, widen('\n'))`, that is, reads at most `std::max(0, count - 1)` characters and stores them into character string pointed to by `s` until `'\n'` is found.
4. Reads characters and stores them into the successive locations of the character array whose first element is pointed to by `s`. Characters are extracted and stored until any of the following occurs:
* `count` is less than `1` or `count - 1` characters have been stored.
* end of file condition occurs in the input sequence (`setstate(eofbit)` is called).
* the next available input character `c` equals `delim`, as determined by `Traits::eq(c, delim)`. This character is not extracted (unlike ).
@@ In any case, if `count > 0`, a null character (`CharT()` is stored in the next successive location of the array.
5. Same as `get(strbuf, widen('\n'))`, that is, reads available characters and inserts them to the given `cpp/io/basic_streambuf` object until `'\n'` is found.
6. Reads characters and inserts them to the output sequence controlled by the given `cpp/io/basic_streambuf` object. Characters are extracted and inserted into `strbuf` until any of the following occurs:
* end of file condition occurs in the input sequence.
* inserting into the output sequence fails (in which case the character that could not be inserted, is not extracted).
* the next available input character `c` equals `delim`, as determined by `Traits::eq(c, delim)`. This character is not extracted.
* an exception occurs (in which case the exception is caught and not rethrown).
If no characters were extracted, calls `setstate(failbit)`.
All versions set the value of `gcount()` to the number of characters extracted.

## Parameters


### Parameters

- `ch` - reference to the character to write the result to
- `s` - pointer to the character string to store the characters to
- `count` - size of character string pointed to by `s`
- `delim` - delimiting character to stop the extraction at. It is not extracted and not stored
- `strbuf` - stream buffer to read the content to

## Return value

1. The extracted character or `Traits::eof()`.
@2-6@ `*this`

## Exceptions


## Example


### Example

```cpp
#include <iostream>
#include <sstream>

int main()
{
    std::istringstream s1("Hello, world.");
    char c1 = s1.get(); // reads 'H'
    std::cout << "after reading " << c1 << ", gcount() == " <<  s1.gcount() << '\n';

    char c2;
    s1.get(c2);         // reads 'e'
    char str[5];
    s1.get(str, 5);     // reads "llo,"
    std::cout << "after reading " << str << ", gcount() == " <<  s1.gcount() << '\n';

    std::cout << c1 << c2 << str;
    s1.get(*std::cout.rdbuf()); // reads the rest, not including '\n'
    std::cout << "\nAfter the last get(), gcount() == " << s1.gcount() << '\n';
}
```


**Output:**
```
after reading H, gcount() == 1
after reading llo,, gcount() == 4
Hello, world.
After the last get(), gcount() == 7
```


## Defect reports


## See also


| cpp/io/basic_istream/dsc read | (see dedicated page) |
| cpp/io/basic_istream/dsc operator_gtgt | (see dedicated page) |
| cpp/io/basic_istream/dsc operator_gtgt2 | (see dedicated page) |

