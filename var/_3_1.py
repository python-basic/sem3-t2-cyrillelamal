def my_zip(*iterables):
    # Build next row
    while True:
        try:
            yield (next(it) for it in iterables)
        except StopIteration:
            break
