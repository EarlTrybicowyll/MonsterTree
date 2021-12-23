from battlers import Human, Bob
from battle import fight
from levels import level_data
from actions import BuyAction, StartLevelAction,TrainAction, RestAction, DisplayStatsAction, PreviewLevelAction
from shop import InvalidShopActionError
import time

def run(initial_inputs=[]):
    if len(initial_inputs) > 0:
        print(f"Fast-forwarding with {len(initial_inputs)} initial inputs")

    inputs = iter(initial_inputs)

    player = Human()
    level_score  = 0
    elapsed_time = 0
    total_score  = 0
    won = False

    # NO_COMMIT: scores per level, to summarize at the end?
    levels = level_data()
    level_scores = []
    for idx, level in enumerate(levels):
        result = fight(player, level.enemies, tick_pause_ms=10)

        total_score = level_score - elapsed_time

        if result:
            print(f"Player beat level {level.name}!\n")
        else:
            print(f"Player lost on level {level.name} :(")
            won = False
            break

        player._coins += level.reward
        level_score += level.score

        total_score = level_score - elapsed_time
        level_scores.append((level.name, level_score, elapsed_time, total_score))

        if idx == len(levels) - 1:
            won = True
            break

        shop = level.shop

        while True:
            total_score = level_score - elapsed_time
            print(f"--{player}")
            print(f"--Total Score: {level_score} (Levels) - {elapsed_time} (Time) = {total_score}\n")
            action = get_main_input(shop, inputs)

            if isinstance(action, StartLevelAction):
                break
            elif isinstance(action, DisplayStatsAction):
                print(player.stats_str())
            elif isinstance(action, PreviewLevelAction):
                print(levels[idx+1].preview_str)
            elif isinstance(action, BuyAction):
                try:
                    shop.purchase_item(player, action.item_name)
                    # NO_COMMIT: snarky responses
                    print(f"Great choice!")
                except InvalidShopActionError as e:
                    print(str(e))
            elif isinstance(action, RestAction):
                elapsed_time += action.duration
                player.rest(action.duration)


    level_score_strs = [f"{' '.join(str(i).ljust(10) for i in ls)}"
                        for ls in level_scores]
    level_score_str = '\n'.join(level_score_strs)
    print(f"\nSummary:\n"
          f"Level      LvlScore   TotTime    TotScore\n"
          f"---------  --------   --------   ---------\n"
          f"{level_score_str}")


def get_main_input(shop, inputs):
    action = None

    while action is None:
        # NO_COMMIT: Add save action
        print(shop)
        try:
            s = next(inputs)
        except StopIteration:
            s = input("Enter Command:\n"
                      "  buy_<item_name> - Purchase an item\n"
                      "  [c]ontinue      - begin the next level\n"
                      "  rest_<duration> - regain up to <duration>-1 health\n"
                      "  [i]inventory    - display detailed character stats\n"
                      "  [l]evel         - preview the next level\n"
                      "[--]")

        s = s.upper()

        if s in ["CONTINUE", "C"]:
            action = StartLevelAction()
        elif s in ["INVENTORY", "I"]:
            action = DisplayStatsAction()
        elif s in ["L", "LEVEL"]:
            action = PreviewLevelAction()
        elif "_" in s:
            parts = s.split("_")
            if len(parts) == 2:
                action_name, arg = parts
                if action_name == "BUY":
                    action = BuyAction(arg)
                elif action_name == "TRAIN":
                    action = TrainAction(arg)
                elif action_name == "REST":
                    action = RestAction(arg)

        if action is None:
            print(f"Unknown action {s}, please try again.\n")

    print("")

    return action
