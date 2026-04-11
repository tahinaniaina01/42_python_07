#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/11 07:33:32 by trakotos            #+#    #+#            #
#   Updated: 2026/04/11 12:44:27 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import Any
from ex2 import BattleStrategy, NormalStrategy, DefensiveStrategy, AggressiveStrategy
from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def battle(
    player1: tuple[Any, BattleStrategy], player2: tuple[Any, BattleStrategy]
) -> None:
    print("* Battle *")
    try:
        p1 = player1[0].create_base()
        p2 = player2[0].create_base()
        print(p1.describe())
        print(" vs.")
        print(p2.describe())
        print(" now fight!")
        player1[1].acte(p1)
        player2[1].acte(p2)
    except Exception as error:
        raise Exception(f"Battle error, aborting tournament: {error}")


def get_name(names: str) -> str:
    res: list[str] = []
    tmp = ""
    for n in names:
        if tmp != "" and n.isupper():
            res.append(tmp)
            tmp = n
        else:
            tmp += n
    if tmp != "":
        res.append(tmp)
    if len(res) == 0:
        return "None"
    return res[0]


def run_tournament(players: list[tuple[Any, BattleStrategy]]) -> None:
    participants: list[str] = []
    for creature, strategy in players:
        creature_name = get_name(creature.__class__.__name__)
        strategy_name = get_name(strategy.__class__.__name__)
        participants.append(f"({creature_name}+{strategy_name})")
    print(f"[ {', '.join(participants)} ]")
    print("*** Tournament ***")
    print(f"{len(players)} opponents involved\n")
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            try:
                battle(players[i], players[j])
                print()
            except Exception as error:
                print(error)
                print()
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    healing_factory = HealingCreatureFactory()
    aqua_factory = AquaFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    defensive_strategy = DefensiveStrategy()
    aggressive_strategy = AggressiveStrategy()
    tournaments = [
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (flame_factory, aggressive_strategy),
        (healing_factory, defensive_strategy),
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy),
    ]
    print("Tournament 0 (basic)")
    run_tournament(tournaments[:2])
    print("Tournament 1 (error)")
    run_tournament(tournaments[2:4])
    print("Tournament 2 (multiple)")
    run_tournament(tournaments[4:])
