

# imports the Pygame library
import pygame
import socket

def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Keyboard events')

    # sets the window size
    pygame.display.set_mode((400, 400))

    # infinite loop
    while True:
        # gets a single event from the event queue
        event = pygame.event.wait()

        # if the 'close' button of the window is pressed
        if event.type == pygame.QUIT:
            # stops the application
            break
        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            # gets the key name
            key_name = pygame.key.name(event.key)

            # converts to uppercase the key name
            key_name = key_name.upper()

            # if any key is pressed
            if event.type == pygame.KEYDOWN:
                # prints on the console the key pressed
                print (u'"{}" key pressed'.format(key_name))
                if (key_name == 'UP'):
                    forward = 255
                    print ('forward:', forward)
                if (key_name == 'DOWN'):
                    moveback = 255
                    print ('moveback:', moveback)
                if (key_name == 'RIGHT'):
                    right1 = 255
                    print ('right1:', right1)
                if (key_name == 'LEFT'):
                    left1 = 255
                    print ('left1:', left1)
                if (key_name == 'D'):
                    right2 = 255
                    print ('right2:', right2)
                if (key_name == 'A'):
                    left2 = 255
                    print ('left2:', left2)
                if (key_name == '1'):
                    link1up = 255
                    print ('link1up:', link1up)
                if (key_name == '2'):
                    link2up = 255
                    print ('link2up:', link2up)
                if (key_name == '3'):
                    link3up = 255
                    print ('link3up:', link3up)
                if (key_name == '4'):
                    link4up = 255
                    print ('link4up:', link4up)
                if (key_name == '5'):
                    link1up = 255
                    print ('link1down:', link1down)
                if (key_name == '6'):
                    link2down = 255
                    print ('link2down:', link2down)
                if (key_name == '7'):
                    link3down = 255
                    print ('link3down:', link3down)
                if (key_name == '8'):
                    link4down = 255
                    print ('link4down:', link4down)             
            elif event.type == pygame.KEYUP:
                # prints on the console the released key
                print (u'"{}" key released'.format(key_name))
                if (key_name == 'UP'):
                    forward = 0
                    print ('forward:', forward)
                if (key_name == 'DOWN'):
                    moveback = 0
                    print ('moveback:', moveback)
                if (key_name == 'RIGHT'):
                    right1 = 0
                    print ('right1:', right1)
                if (key_name == 'LEFT'):
                    left1 = 0
                    print ('left1:', left1)
                if (key_name == 'D'):
                    right2 = 0
                    print ('right2:', right2)
                if (key_name == 'A'):
                    left2 = 0
                    print ('left2:', left2)
                if (key_name == '1'):
                    link1up = 0
                    print ('link1up:', link1up)
                if (key_name == '2'):
                    link2up = 0
                    print ('link2up:', link2up)
                if (key_name == '3'):
                    link3up = 0
                    print ('link3up:', link3up)
                if (key_name == '4'):
                    link4up = 0
                    print ('link4up:', link4up)
                if (key_name == '5'):
                    link1down = 0
                    print ('link1down:', link21down)
                if (key_name == '6'):
                    link2down = 0
                    print ('link2down:', link2down)
                if (key_name == '7'):
                    link3down = 0
                    print ('link3down:', link3down)
                if (key_name == '8'):
                    link4down = 0
                    print ('link4down:', link4down)

            val = str(forward) + str(moveback) + str(right1) + str(left1) + str(right2) + str(left2) + str(link1up) + str(link1down) + str(link2up) + str(link2down) + str(link3up) + str(link3down) + str(link4up) + str(link4down)

        host = '127.0.0.1'  # The server's hostname or IP address
        port = 65432        # The port used by the server

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(b'Hello, world')
            data = s.recv(1024)
            s.send(val)
        print('Received', repr(data))
    
    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
