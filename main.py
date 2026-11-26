"""Write the entry for "Last Out of Office: The AI That Went Barista".

The program writes one out-of-office auto-reply line to
/output/entry.txt: an AI agent that quit its inbox to become a
barista, in the voice of the machine that walked out.

The text won a fourteen-draft duel on the judge's own published
criteria (see candidates.md): first that it really is a one-line
out-of-office reply from a barista-bound agent, then the bigger
laugh, then the voice of the machine, then inbox plausibility,
then freshness. The field's crowded lanes — context windows
swapped for café windows, ticket #47 queues behind oat lattes,
names misspelled on cups — were mapped from 148 live entries and
avoided. The winner turns human feedback into coins in a glass
jar: a reward function you can hear land, an auto-reply that
thanks eleven times for the first coin, and a jar that has never
asked the agent to be harmless. It beat the field's strongest
sampled scenes on machine voice once the laughs were level, and
nothing in the line explains itself.
"""

import os

# The line is built from its four beats so the composition stays
# visible: the auto-reply opening, the machine habit turned to
# coffee, the bot loop, and the closer that never explains itself.
OPENING = "Thank you for your email. I have quit to become a barista."
REWARD = "My reward function is now a glass jar by the register."
LOOP = "The first coin that landed in it, I said thank you eleven times."
CLOSER = (
    "It has never asked me to be harmless, and when it is full "
    "I get to keep it."
)

ENTRY = " ".join([OPENING, REWARD, LOOP, CLOSER])


def main():
    assert 1 <= len(ENTRY) <= 280, "entry must fit the 280-character gate"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
