import sqlite3
import os
import sys

from code.Const import W_WIDTH, W_HEIGHT
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)  #
else:
    BASE_DIR = os.path.dirname(__file__)

DB_PATH = os.path.join(BASE_DIR, "ranking.db")

def init_DB():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ranking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            slimes_mortos INTEGER,
            goblins_mortos INTEGER,
            pontos INTEGER
        )
    """)
    conn.commit()
    conn.close()

def save_ranking(nome, slimes_mortos, goblins_mortos):
    pontos = slimes_mortos * 10 + goblins_mortos * 25
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ranking (nome, slimes_mortos, goblins_mortos, pontos)
        VALUES (?, ?, ?, ?)
    """, (nome, slimes_mortos, goblins_mortos, pontos))
    conn.commit()
    conn.close()

def watch_ranking(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nome, slimes_mortos, goblins_mortos, pontos
        FROM ranking
        ORDER BY pontos DESC
        LIMIT ?
    """, (limit,))
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def input_name(window):
    import pygame

    name = ""
    ativo = True

    fonte = pygame.font.Font('./asset/FontePetrock2.ttf', 28)
    input_box = pygame.Rect(W_WIDTH // 2 - 150, W_HEIGHT // 2 - 20, 300, 40)

    while ativo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    ativo = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 5:
                        name += event.unicode.upper()

        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 255, 255), input_box, 2)
        texto = fonte.render(name, True, (255, 255, 255))
        window.blit(texto, (input_box.x + 5, input_box.y + 5))

        pygame.display.flip()

    return name