import time

def fight(player, enemies, tick_pause_ms=50):
    """
    Returns whether the player survives the fight.
    """
    print("------------------------------ BATTLE! ------------------------------")
    lhs = f"{player} vs "
    pad = " " * len(lhs)
    rhs = f"\n{pad}".join(str(e) for e in enemies)
    print(f"{lhs}{rhs}\n")
    # NO_COMMIT: shuffle?
    battlers = list(enemies) + [player]

    remain_es = list(enemies)

    tick = 0
    while player.cur_hp > 0 and len(remain_es) > 0:
        enemy = remain_es[0]

        if tick % player.spd == 0:
            enemy_dies = damage(player, enemy)
        else:
            enemy_dies = False

        if tick % enemy.spd == 0:
            player_dies = damage(enemy, player)
        else:
            player_dies = False

        time.sleep(tick_pause_ms * 1e-3)

        if player_dies:
            return False

        if enemy_dies:
            remain_es = remain_es[1:]

        tick += 1

    return True


def damage(battler1, battler2):
    """
    Resolve **battler1** attacking **battler2**.

    Returns whether this killed **battler2**.
    """
    dmg = max(battler1.atk - battler2.dfn, 1)
    new_hp = max(battler2.cur_hp - dmg, 0)
    print(f"    {battler1.name} dealt {dmg} dmg to {battler2.name}: "
          f"[{battler2.cur_hp}->{new_hp}/{battler2.max_hp}]")

    # NO_COMMIT: settor
    battler2._cur_hp = new_hp

    return new_hp == 0
