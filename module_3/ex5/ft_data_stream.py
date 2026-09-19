import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    names = [
        'bob', 'alice', 'dylan', 'charlie',
    ]
    acts = [
        'climb', 'run', 'grab', 'swim', 'sleep', 'move',
        'use', 'release'
    ]
    while True:
        r_name = random.choice(names)
        r_act = random.choice(acts)
        comb = (r_name, r_act)
        yield (comb)


def consume_event(
    gen_comb10: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while gen_comb10:
        chosen = random.choice(gen_comb10)
        gen_comb10.remove(chosen)
        yield (chosen)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    comb = gen_event()
    for i in range(1000):
        name, act = next(comb)
        print(f"Event {i}: Player {name} did action {act}")
    gen_comb10 = gen_event()
    comb_10 = [next(gen_comb10) for _ in range(10)]
    print(f"Built list of 10 events: {comb_10}")
    for event in consume_event(comb_10):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {comb_10}")
