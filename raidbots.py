#!/usr/bin/python3

import json
import subprocess
import sys

import requests

HEADERS = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "cookie": "raidsid=s%3A6202799922610176%3Ao4dC9ff6jbByvcN23772Jt.4R5c%2BIvfTA2hzvJqcsDujyiyrJaWtgBWWzGjEG%2Bk4Bc",
    "origin": "https://www.raidbots.com",
    "referer": "https://www.raidbots.com/simbot/advanced",
    "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

PAYLOAD = {
    "type": "advanced",
    "text": "",
    "baseActorName": "",
    "reportName": "Advanced Sim",
    "armory": {"region": "us", "realm": "", "name": ""},
    "email": "",
    "sendEmail": False,
    "spec": "",
    "gearsets": [],
    "talents": None,
    "talentSets": [],
    "droptimizer": {
        "equipped": {},
        "instance": 1200,
        "difficulty": "raid-mythic",
        "warforgeLevel": 0,
        "gem": None,
        "faction": "horde",
        "offSpecItems": True,
        "includeConversions": True,
    },
    "droptimizerItems": None,
    "simcVersion": "nightly",
    "iterations": "smart",
    "smartHighPrecision": True,
    "fightStyle": "Patchwerk",
    "fightLength": 300,
    "enemyCount": 1,
    "enemyType": "FluffyPillow",
    "reportDetails": False,
    "apl": "",
    "ptr": False,
    "frontendHost": "www.raidbots.com",
    "frontendVersion": "def35d5031050a601dc342f09c01444929179469",
    "blueSilkenLining": 70,
    "rubyWhelpShellTraining": "sleepy_ruby_warmth:6",
    "primalRitualShell": "flame",
    "whisperingIncarnateIconRoles": "dps/heal/tank",
    "temporaryEnchant": "",
    "enableDominationShards": False,
    "soleahStatType": "haste",
    "ocularGlandUptime": 100,
    "enableRuneWords": False,
    "stoneLegionHeraldryInParty": 0,
    "cabalistsHymnalInParty": 0,
    "disableIqdExecute": False,
    "iqdStatFailChance": 0,
    "unboundChangelingStatType": "",
    "nazjatar": False,
    "worldveinAllies": 0,
    "loyalToTheEndAllies": 0,
    "covenantChance": 100,
    "undulatingTides": 100,
    "nyalotha": True,
    "aberration": False,
    "voidRitual": False,
    "surgingVitality": 0,
    "symbioticPresence": 22,
}


def sim(build, apl):
    payload = PAYLOAD
    payload["advancedInput"] = "\n".join([build, apl])

    try:
        del HEADERS["accept-encoding"]
    except KeyError:
        pass

    r = requests.post(
        "https://www.raidbots.com/sim", data=json.dumps(payload), headers=HEADERS
    )
    simId = r.json()["simId"]
    url = f"https://www.raidbots.com/simbot/report/{simId}"

    subprocess.run(["wslview", url])


if __name__ == "__main__":
    try:
        with open(sys.argv[1]) as f:
            build = f.read()

        with open(sys.argv[2]) as f:
            apl = f.read()

        sim(build, apl)
    except:
        pass
