# C/C++

## Raw and Rough (dos command: edit, compile, and run)

Type out these commands on the terminal
```
echo #include ^<iostream^> > raw.cpp
echo int main(void){ >> raw.cpp
echo std^:^:cout ^<^< "It's raw!";} >> raw.cpp
type raw.cpp
g++ raw.cpp -o raw.exe
raw
```

## Create C Library

Steps
  * write a header file
  * write library functions
    * also, include the header file
  * write a main file
    * have the header file
  * compile
    * compile the library ```gcc -c -g <lib.c>```
    * compile the main file ```gcc -c -g <main.c>```
    * link ```gcc -o <main.exe> <main.o> <lib.o>```
    * the object file is ready for execution ```main.exe```

See [example](https://github.com/tatpongkatanyukul/Learn/blob/main/CCPP/clib.rar)

Learn more
  * [Create library in details](https://renenyffenegger.ch/notes/development/languages/C-C-plus-plus/GCC/create-libraries/index)
    * [its pdf](https://github.com/tatpongkatanyukul/Learn/blob/main/CCPP/create_library.pdf) (just in case)


## Create C++ Library

Steps is identical to C, but compile with ```g++```
```
g++ -c -g <lib.cpp>
g++ -c -g <main.cpp>
g++ -o <main.exe> <main.o> <lib.o>
main.exe
```

See [example of C++ static library](https://github.com/tatpongkatanyukul/Learn/blob/main/CCPP/cpplib1.tar)

See 
  * [microsoft: walkthrough creating C++ static library](https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-static-library-cpp?view=msvc-160)
  * [microsoft: walkthrough creating C++ dynamic link library](https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?redirectedfrom=MSDN&view=msvc-160)

