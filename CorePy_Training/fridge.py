"""Demonstrate raiding a refrigerator."""

from contextlib import closing  # allow closing the class's methods implicitly


class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print(f"Finding {food}...")
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning!")
        print(f"Taking {food}")

    def close(self):
        print("Close fridge door.")


def raid(food):
    with closing(RefrigeratorRaider()) as r:    # automatically close the method after execution by the context manager
        r.open()
        r.take(food)
        #r.close()  # explicitly closing is then not necessary

