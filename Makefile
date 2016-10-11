ALL:
	g++ -I/usr/include/python2.7 -I./evmjit/include -c -fPIC pyevmjit.cpp -o pyevmjit.o
	g++ -shared -o pyevmjit.so pyevmjit.o -lpython2.7 ./evmjit/build/libevmjit/libevmjit-static.a

clean:
	rm *.so *.o
