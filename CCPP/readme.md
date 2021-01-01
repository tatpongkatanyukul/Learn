# C/C++

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

See 
  * [microsoft: walkthrough creating C++ static library](https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-static-library-cpp?view=msvc-160)
  * [microsoft: walkthrough creating C++ dynamic link library](https://docs.microsoft.com/en-us/cpp/build/walkthrough-creating-and-using-a-dynamic-link-library-cpp?redirectedfrom=MSDN&view=msvc-160)

