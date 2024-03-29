import pygame 
import math


pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [0, 0, 255]
BLUE = [255, 0, 0]

screen = pygame.display.set_mode([930, 690])
screen.fill([255, 255, 255])

pygame.display.set_caption('function graph')

done = False

cos_points = []
sin_points = []


n = 6
a = 240

#the formula is correct but somehow line of the sine and line of the cosine
#are being drawn vice versa


for x in range(105, 826):
    y = int(math.cos((x + 76)/720 * n * math.pi) * a + 345)
    cos_points.append([x, y])

for x in range(105, 826):
    y = int(math.sin((x - 44)/720 * n * math.pi) * a + 345)
    sin_points.append([x, y])


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and key.type == pygame.K_ESCAPE:
            done = True

    #frame

    pygame.draw.rect(screen, BLACK, (75, 75, 780, 540), 3)

    #x-axis and y-axis

    pygame.draw.line(screen, BLACK, [75, 345], [855, 345], 3)
    pygame.draw.line(screen, BLACK, [465, 75], [465, 615], 3)

    #horizontal lines

    for y in range (105, 615, 60):
        pygame.draw.line(screen, BLACK, [75, y], [855, y], 1)

    #vertical lines
    for x in range (105, 885, 120):
        pygame.draw.line(screen, BLACK, [x, 75], [x, 615], 1)

    #vertical scale

    u, d = 105, 585
    i = 0
    while (u < d):
        if i % 2 == 0:
            pygame.draw.line(screen, BLACK, [75, u], [90, u], 1)
            pygame.draw.line(screen, BLACK, [840, u], [855, u], 1)
        else:
            pygame.draw.line(screen, BLACK, [75, u], [82, u], 1)
            pygame.draw.line(screen, BLACK, [848, u], [855, u], 1)
        i += 1
        u += 15

    #horizontal scale

    l1, r1 = 105, 835
    j = 0
    while (l1 < r1):
        if j % 2 == 0:
            pygame.draw.line(screen, BLACK, [l1, 75], [l1, 90], 1)
            pygame.draw.line(screen, BLACK, [l1, 600], [l1, 615], 1)
        elif j % 4 == 0:
            pygame.draw.line(screen, BLACK, [l1, 75], [l1, 97], 1)
            pygame.draw.line(screen, BLACK, [l1, 593], [l1, 615], 1)
        else:
            pygame.draw.line(screen, BLACK, [l1, 608], [l1, 615], 1)
            pygame.draw.line(screen, BLACK, [l1, 75], [l1, 82], 1)
        j += 1
        l1 += 15

    l2, r2 = 105, 835
    while (l2 < r2):
        pygame.draw.line(screen, BLACK, [l2, 75], [l2, 97], 1)
        pygame.draw.line(screen, BLACK, [l2, 593], [l2, 615], 1)
        l2 += 60

    #leftmost digits

    upper_coordinate, lower_coordinate = 105, 615
    digit = 1.00
    while (upper_coordinate < lower_coordinate):
        font = pygame.font.SysFont('Calibri', 25, False, False)
        text = font.render(str(digit), True, BLACK)
        if digit < 0:
            screen.blit(text, (15, upper_coordinate - 12))
        else:
            screen.blit(text, (25, upper_coordinate - 12))
        upper_coordinate += 60
        digit -= 0.25

    #radians

    left, right = 105, 830
    i = 0
    radians = ['-3pi', '-5pi', '-2pi', '-3pi', '-pi', '-pi', '0', 'pi', 'pi', '3pi', '2pi', '5pi', '3pi']
    while (left < right):
        font = pygame.font.SysFont('Times New Roman', 25, False, False)
        text = font.render(radians[i], True, BLACK)
        if radians[i]  != '0':
            screen.blit(text, (left - 19, 615))
        else:
            screen.blit(text, (left - 5, 615))
        i += 1
        left += 60
    
    #sine and cosine lines

    pygame.draw.lines(screen, BLUE, False, cos_points, 2)
    pygame.draw.lines(screen, RED, False, sin_points, 2)

    pygame.display.flip()

    

