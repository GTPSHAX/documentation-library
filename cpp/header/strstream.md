---
title: strstream
type: Standard headers
source: https://en.cppreference.com/w/cpp/header/strstream
---

This header is part of the Input/Output library.


| cpp/io/dsc strstreambuf | (see dedicated page) |
| cpp/io/dsc istrstream | (see dedicated page) |
| cpp/io/dsc ostrstream | (see dedicated page) |
| cpp/io/dsc strstream | (see dedicated page) |


## Notes

is deprecated in C++98 and removed in C++26 (see ).
The reason for removal is that C++20 and C++23 provide superior replacement facilities, such as the ability to move strings efficiently out of `std::basic_stringstream|std::stringstream`s (since C++20, see ), and the  library (since C++23, see ).

## Synopsis


```cpp
namespace std {
  class strstreambuf;
  class istrstream;
  class ostrstream;
  class strstream;
}
```


### Class `std::strstreambuf`


```cpp
namespace std {
  class strstreambuf : public basic_streambuf<char> {
  public:
    strstreambuf() : strstreambuf(0) {}
    explicit strstreambuf(streamsize alsize_arg);
    strstreambuf(void* (*palloc_arg)(size_t), void (*pfree_arg)(void*));
    strstreambuf(char* gnext_arg, streamsize n, char* pbeg_arg = nullptr);
    strstreambuf(const char* gnext_arg, streamsize n);

    strstreambuf(signed char* gnext_arg, streamsize n,
                 signed char* pbeg_arg = nullptr);
    strstreambuf(const signed char* gnext_arg, streamsize n);
    strstreambuf(unsigned char* gnext_arg, streamsize n,
                 unsigned char* pbeg_arg = nullptr);
    strstreambuf(const unsigned char* gnext_arg, streamsize n);

    virtual ~strstreambuf();

    void  freeze(bool freezefl = true);
    char* str();
    int   pcount();

  protected:
    int_type overflow (int_type c = EOF) override;
    int_type pbackfail(int_type c = EOF) override;
    int_type underflow() override;
    pos_type seekoff(off_type off, ios_base::seekdir way,
                     ios_base::openmode which = ios_base::in {{!
```

pos_type seekpos(pos_type sp,
ios_base::openmode which = ios_base::in | ios_base::out) override;
streambuf* setbuf(char* s, streamsize n) override;
private:
using strstate = /*bitmask type*/;  // exposition only
static const strstate allocated;    // exposition only
static const strstate constant;     // exposition only
static const strstate dynamic;      // exposition only
static const strstate frozen;       // exposition only
strstate strmode;                   // exposition only
streamsize alsize;                  // exposition only
void* (*palloc)(size_t);            // exposition only
void (*pfree)(void*);               // exposition only
};
}

### Class `std::istrstream`


```cpp
namespace std {
  class istrstream : public basic_istream<char> {
  public:
    explicit istrstream(const char* s);
    explicit istrstream(char* s);
    istrstream(const char* s, streamsize n);
    istrstream(char* s, streamsize n);
    virtual ~istrstream();

    strstreambuf* rdbuf() const;
    char* str();
  private:
    strstreambuf sb;            // exposition only
  };
}
```


### Class `std::ostrstream`


```cpp
namespace std {
  class ostrstream : public basic_ostream<char> {
  public:
    ostrstream();
    ostrstream(char* s, int n, ios_base::openmode mode = ios_base::out);
    virtual ~ostrstream();

    strstreambuf* rdbuf() const;
    void freeze(bool freezefl = true);
    char* str();
    int pcount() const;
  private:
    strstreambuf sb;            // exposition only
  };
}
```


### Class `std::strstream`


```cpp
namespace std {
  class strstream
    : public basic_iostream<char> {
  public:
    // types
    using char_type = char;
    using int_type  = char_traits<char>::int_type;
    using pos_type  = char_traits<char>::pos_type;
    using off_type  = char_traits<char>::off_type;

    // constructors/destructor
    strstream();
    strstream(char* s, int n,
              ios_base::openmode mode = ios_base::in {{!
```

virtual ~strstream();
// members
strstreambuf* rdbuf() const;
void freeze(bool freezefl = true);
int pcount() const;
char* str();
private:
strstreambuf sb;            // exposition only
};
}
