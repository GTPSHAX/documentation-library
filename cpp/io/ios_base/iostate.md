---
title: std::ios_base::iostate
type: Input/output
source: https://en.cppreference.com/w/cpp/io/ios_base/iostate
---


```cpp
dcl|
typedef /*implementation defined*/ iostate;
dcl|1=
static constexpr iostate goodbit = 0;
dcl|1=
static constexpr iostate badbit  = /* implementation defined */
static constexpr iostate failbit = /* implementation defined */
static constexpr iostate eofbit  = /* implementation defined */
```

Specifies stream state flags. It is a *BitmaskType*, the following constants are defined:

### The eofbit

The eofbit is set by the following standard library functions:
* The string input function `std::getline` if it completes by reaching the end of the stream, as opposed to reaching the specified terminating character.
* The numeric input overloads of  if the end of the stream was encountered while reading the next character, on Stage 2 of  processing. Depending on the parsing state, `failbit` may or may not be set at the same time: for example, `1=int n; istringstream buf("1"); buf >> n;` sets `eofbit`, but not `failbit`: the integer `1` was successfully parsed and stored in `n`. On the other hand, `1=bool b; istringstream buf("tr"); buf >> boolalpha >> b;` sets both `eofbit` and `failbit`: there was not enough characters to complete the parsing of the boolean `true`.
* The character extraction overloads of `cpp/io/basic_istream/operator_gtgt2|operator>>, if the end of the stream is reached before the limit (if any) on the number of characters to be extracted.
* The `std::get_time` I/O manipulator and any of the `std::time_get` parsing functions: , , , etc., if the end of the stream is reached before the last character needed to parse the expected date/time value was processed.
* The `std::get_money` I/O manipulator and  function, if the end of the stream is reached before the last character needed to parse the expected monetary value was processed.
* The  constructor, executed at the beginning of every formatted input function: unless the `skipws` bit is unset (e.g. by issuing `std::noskipws`), sentry reads and discards the leading whitespace characters. If the end of the input stream is reached during this operation, both `eofbit` and `failbit` are set, and no input takes place.
* The I/O manipulator `std::ws`, if it reaches the end of the stream while consuming whitespace (but, unlike the formatted input sentry, it does not set `failbit` in this case).
* The unformatted input functions , , , , , and , when reaching the end of the stream.
* The discard input function , when reaching the end of the stream before reaching the specified delimiter character.
* The immediate input function , if  returns `-1`.
The following functions clear `eofbit` as a side-effect:
*
*
*
Note that in nearly all situations, if eofbit is set, the failbit is set as well.

### The failbit

The failbit is set by the following standard library functions:
* The  constructor, executed at the beginning of every input function, if either `eofbit` or `badbit` is already set on the stream, or if the end of stream is encountered while consuming leading whitespace.
* The  constructor, executed at the beginning of every output function, under implementation-defined conditions.
* `cpp/string/basic_string/operator_ltltgtgt|operator>> if the function extracts no characters from the input stream.
* `cpp/numeric/complex/operator_ltltgtgt|operator>> if the function fails to extract a valid complex number.
* The character array and single character overloads of `cpp/io/basic_istream/operator_gtgt2|operator>>` if they fail to extract any characters.
* The streambuf overload of  if the streambuf argument is a null pointer or if no characters were inserted into the streambuf.
* The streambuf overload of  if the function inserts no characters.
* `cpp/utility/bitset/operator_ltltgtgt2|operator>> if the function extracts no characters from the input stream.
* `std::getline` if the function extracts no characters or if it manages to extract  characters from the input stream.
* The numeric, pointer, and boolean input overloads of  (technically, the overloads of  they call), if the input cannot be parsed as a valid value or if the value parsed does not fit in the destination type.
* The time input manipulator `std::get_time` (technically,  it calls), if the input cannot be unambiguously parsed as a time value according to the given format string.
* The currency input manipulator `std::get_money` (technically,  it calls), if the input cannot be unambiguously parsed as a monetary value according to the locale rules.
* The extraction operators of all *RandomNumberEngine*s, if bad input is encountered.
* The extraction operators of all *RandomNumberDistribution*s, if bad input is encountered.
* The unformatted input functions  if they fails to extract any characters.
* , if it extracts no characters, if it fills in the provided buffer without encountering the delimiter, or if the provided buffer size is less than 1.
* , if the end-of-file condition occurs on the input stream before all requested characters could be extracted.
*  on failure
*  on failure
* The constructors of `std::basic_fstream`, `std::basic_ifstream`, and `std::basic_ofstream` that takes a filename argument, if the file cannot be opened.
* , , and  if the file cannot be opened.
* , , and  if the file cannot be closed.

### The badbit

The badbit is set by the following standard library functions:
*  if it fails to insert a character into the output stream, for any reason.
*  if it fails to insert a character into the output stream, for any reason.
* Formatted output functions operator<<, `std::put_money`, and `std::put_time`, if they encounter the end of the output stream before completing output.
*  when called to initialize a stream with a null pointer for `rdbuf()`.
*  and  when called on a stream with a null `rdbuf()`.
*  when a null pointer is passed as the argument.
*  and  if `rdbuf()->sputbackc()` or `rdbuf()->sungetc()` return `traits::eof()`.
* , , and every output function on a `unitbuf` output stream, if `rdbuf()->pubsync()` returns `-1`.
* Every stream I/O function if an exception is thrown by any member function of the associated stream buffer (e.g. `sbumpc()`, `xsputn()`, `sgetc()`, `overflow()`, etc).
*  and  on failure (e.g. failure to allocate memory).

## Example


## See also


| cpp/io/basic_ios/dsc rdstate | (see dedicated page) |
| cpp/io/basic_ios/dsc setstate | (see dedicated page) |
| cpp/io/basic_ios/dsc clear | (see dedicated page) |

