CC=gcc
CFLAGS = -I/. -I./alpha -I./beta -g

all: alpha/alpha-server.c alpha/alpha-client.c beta/beta-server.c beta/beta-client.c client.c server.c
	gcc -c $(CFLAGS) -fPIC alpha/alpha-server.c -o alpha-server.o
	gcc -c $(CFLAGS) -fPIC alpha/alpha-client.c -o alpha-client.o
	gcc -shared -o libalpha-client.so alpha-client.o
	gcc -shared -o libalpha-server.so alpha-server.o
	gcc -c $(CFLAGS) -fPIC beta/beta-server.c -o beta-server.o
	gcc -c $(CFLAGS) -fPIC beta/beta-client.c -o beta-client.o
	gcc -shared -o libbeta-client.so beta-client.o
	gcc -shared -o libbeta-server.so beta-server.o
	gcc -c $(CFLAGS) server.c -o server.o
	gcc -c $(CFLAGS) client.c -o client.o
	gcc -o server server.o -L. -lalpha-server -lbeta-client -lbeta-server -lmargo
	gcc -o client client.o -L. -lalpha-client -lmargo

clean:
	rm *.o *.csv *.trace client server core* *.so
