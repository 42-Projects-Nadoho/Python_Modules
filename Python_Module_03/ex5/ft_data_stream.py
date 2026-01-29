def event_stream(num_events: int) -> object:
    """Generator that yields deterministically.

    Args:
        num_events (int): number of events

    Yields:
        Iterator of (index, player, level, action)
    """
    try:
        n = int(num_events)
    except Exception:
        n = 0
    if n <= 0:
        return

    players = ["alice", "bob", "charlie", "david", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]
    plen = len(players)
    alen = len(actions)
    for i in range(n):
        idx = i + 1
        player = players[i % plen]
        level = (i % 20) + 1
        action = actions[i % alen]
        yield (idx, player, level, action)


def filter_events(stream: object, action: str) -> object:
    """Filter generator: yield only events
    whose action equals the given action.
    If action is falsy (None or empty string), yield all events unchanged.
    """
    if not action:
        for ev in stream:
            yield ev
        return

    for event in stream:
        try:
            if len(event) >= 4 and event[3] == action:
                yield event
        except Exception:
            continue


def fib(n: int) -> object:
    """Yield first n Fibonacci numbers."""
    try:
        count = max(0, int(n))
    except Exception:
        count = 0
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def primes(n: int) -> object:
    """Yield first n prime numbers (simple trial division)."""
    try:
        target = max(0, int(n))
    except Exception:
        target = 0
    found = 0
    num = 2
    while found < target:
        is_prime = True
        d = 2
        while d * d <= num:
            if num % d == 0:
                is_prime = False
                break
            d += 1
        if is_prime:
            yield num
            found += 1
        num += 1


def ft_data_stream() -> None:
    """Main processing function for the data stream."""
    try:
        print("=== Game Data Stream Processor ===")
        total_events = 1000
        stream = event_stream(total_events)
        print(f"\nProcessing {total_events} game events...\n")

        preview = []
        preview_count = 3
        for _ in range(preview_count):
            try:
                ev = next(stream)
                preview.append(ev)
            except StopIteration:
                break
            except Exception:
                break

        for idx, player, level, action in preview:
            print(f"Event {idx}: Player {player} (level {level}) {action}")
        if total_events > preview_count:
            print("...")

        total = 0
        high_level = 0
        treasure = 0
        level_ups = 0

        for _, player, level, action in preview:
            total += 1
            if level >= 10:
                high_level += 1
            if action == "found treasure":
                treasure += 1
            if action == "leveled up":
                level_ups += 1

        for _, player, level, action in stream:
            total += 1
            if level >= 10:
                high_level += 1
            if action == "found treasure":
                treasure += 1
            if action == "leveled up":
                level_ups += 1

        print("\n=== Stream Analytics ===")
        print(f"Total events processed: {total}")
        print(f"High-level players (10+): {high_level}")
        print(f"Treasure events: {treasure}")
        print(f"Level-up events: {level_ups}")
        print("Memory usage: Constant (streaming)")
        print("Processing time: Constant-ish (no full storage)")

        print("\n=== Generator Demonstration ===")
        print("Fibonacci sequence (first 10): ", end="")
        print(", ".join(str(x) for x in fib(10)))

        print("Prime numbers (first 5): ", end="")
        print(", ".join(str(x) for x in primes(5)))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        ft_data_stream()
    except Exception as e:
        print(f"Fatal error: {e}")
