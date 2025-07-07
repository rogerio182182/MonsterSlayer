

from code.Entity import Entity
from code.Monster import Monster
from code.Player import Player


class EntityMediator:

    @staticmethod
    def skill_collision(skill, entity_list: list[Entity]):
        if not skill.active:
            return
        for entidade in entity_list:
            if isinstance(entidade, Monster):
                if skill.rect.colliderect(entidade.rect):

                        entidade.hp -= skill.dano

                        print(f"{entidade.name} foi atingido por {skill.name} e perdeu {skill.dano} de HP.")

                        skill.active = False
                        break

    @staticmethod
    def monster_collision(entity_list, player, som_dano):
        for entidade in entity_list:
            if isinstance(entidade , Monster):
                if entidade.grid_pos == player.grid_pos:
                    if not player.invulneravel:
                        som_dano.play()
                        player.receber_dano(entidade.dano)

    @staticmethod
    def verify_hp(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.hp <= 0:
                if isinstance(ent, Player):
                    print("GAME OVER")
                    # Aqui você pode mostrar tela de derrota, pausar o jogo, etc.
                    continue  # não remove o player da lista ainda
                entity_list.remove(ent)