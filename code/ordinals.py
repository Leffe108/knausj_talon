from talon import Context, Module, actions, app, ui

# Instead of upstream ordinals, use "X repeat" which repeats last
# command the number of times as stated.
ordinal_numbers = {}
ordinal_small = {}
for n in range(1, 100):
    word = str(n) + ' repeat'
    if n <= 20:
        ordinal_small[word] = n + 1
    ordinal_numbers[word] = n + 1

mod = Module()
ctx = Context()
mod.list("ordinals", desc="list of ordinals")
mod.list("ordinals_small", desc="list of ordinals small (1-20)")

ctx.lists["self.ordinals"] = ordinal_numbers.keys()
ctx.lists["self.ordinals_small"] = ordinal_small.keys()


@mod.capture(rule="{self.ordinals}")
def ordinals(m) -> int:
    """Returns a single ordinal as a digit"""
    return int(ordinal_numbers[m[0]])


@mod.capture(rule="{self.ordinals_small}")
def ordinals_small(m) -> int:
    """Returns a single ordinal as a digit"""
    return int(ordinal_numbers[m[0]])
