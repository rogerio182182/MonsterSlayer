

from code.Entity import Entity
from code.Monster import Monster
from code.Player import Player


class EntityMediator:
    slimes_mortos = 0
    goblins_mortos = 0

    @staticmethod
    def resetar_contadores():
        EntityMediator.slimes_mortos = 0
        EntityMediator.goblins_mortos = 0

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
                    return 'game_over'
                if ent.name == "slime":
                    EntityMediator.slimes_mortos += 1
                elif ent.name == "goblin":
                    EntityMediator.goblins_mortos += 1

                entity_list.remove(ent)