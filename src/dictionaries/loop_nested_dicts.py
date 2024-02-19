""" A script to read and loop through nested disctionaries.
"""

import json
from pathlib import Path

with open(f"{Path(__file__).parent}/context/sample.json") as conf:
    conf = json.load(conf)


def loop_nested_dicts():
    """A function to loop through nested disctionaries"""

    for root_k, root_v in conf.items():
        root_envs = root_k
        print("Root environments: '%s'" % root_envs)
        sub_envs = conf[root_k].items()
        print("Sub environments: '%s'" % sub_envs)
        for sub_k, sub_v in sub_envs:
            sub_env_value = conf[root_k][sub_k]["SAMPLE_KEY"]
            print(f"{sub_k}: SAMPLE_KEY: {sub_env_value}")


if __name__ == "__main__":
    loop_nested_dicts()
