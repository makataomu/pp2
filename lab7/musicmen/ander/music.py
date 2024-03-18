import pygame
import sys
import os


pygame.init()

pygame.mixer.init()
clock = pygame.time.Clock()

# Define a smaller screen size
size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Music player')


image = pygame.image.load("img/6.jpeg")
image_rect = image.get_rect()  # Get rect object to handle image dimensions

music_dir = "ander"
music_files = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]

if not music_files:
    print("No music files found in the specified directory.")
    pygame.quit()
    sys.exit()


font = pygame.font.SysFont('Arial', 24)  # Adjusted font size for smaller screen


i = 0
vol = 1
begin = False
is_playing = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                begin = True
                pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
                pygame.mixer.music.play()
                is_playing = True

            if event.key == pygame.K_SPACE and begin:
                if is_playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                is_playing = not is_playing

            if event.key == pygame.K_RIGHT and begin:
                i = (i + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
                pygame.mixer.music.play()
                is_playing = True

            if event.key == pygame.K_LEFT and begin:
                i = (i - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_dir, music_files[i]))
                pygame.mixer.music.play()
                is_playing = True

            if event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(min(vol, 1.0))

            if event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(max(vol, 0.0))


    screen.fill((255, 255, 255))  # Fill screen with white background

    # Calculate position to center the image
    image_x = (size[0] - image_rect.width) // 2
    image_y = (size[1] - image_rect.height) // 2
    screen.blit(image, (image_x, image_y))

    if begin:
        s = font.render(music_files[i][:-4], True, 'black') 
        screen.blit(s, (300, 205))  # Adjusted position for smaller screen
    clock.tick(10)
    pygame.display.flip()
