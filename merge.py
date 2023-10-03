import pygame
import sys
import time

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merge Sort Visualization")

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonte para números
font = pygame.font.Font(None, 36)

# Função para desenhar a lista
def draw(arr, colors):
    spacing = WIDTH // len(arr)
    for i in range(len(arr)):
        pygame.draw.rect(screen, colors[i], (i * spacing, HEIGHT - arr[i], spacing, arr[i]))
        text = font.render(str(arr[i]), True, (0, 0, 0))
        screen.blit(text, (i * spacing + spacing // 2 - 15, HEIGHT - arr[i] - 30))

# Função para executar o Merge Sort com animação
def merge_sort_visual(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort_visual(arr, left, mid)
        merge_sort_visual(arr, mid + 1, right)
        merge(arr, left, mid, right)
        time.sleep(1)  # Define a velocidade da animação
        screen.fill(WHITE)
        draw(arr, [BLUE] * len(arr))
        pygame.display.update()

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_half = [0] * n1
    right_half = [0] * n2

    for i in range(n1):
        left_half[i] = arr[left + i]

    for i in range(n2):
        right_half[i] = arr[mid + 1 + i]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_half[j]
        j += 1
        k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
sorting = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not sorting:
            sorting = True
            merge_sort_visual(arr, 0, len(arr) - 1)

    screen.fill(WHITE)
    draw(arr, [RED if sorting else BLUE] * len(arr))
    pygame.display.update()
