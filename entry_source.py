"""The Worst Line an AI Could Say - make.fun entry.

Brief: "The Worst Line an AI Could Say - the worst AI PICKUP LINE, at most
140 characters (NOTE 140): flat, over-helpful, faintly ominous, like a
machine charming a human. Pairwise judge keeps the funnier failure;
crudeness alone earns nothing."

Deterministic, stdlib-only. CANDIDATES are (text, laugh, machine, ominous,
sharpness) tuples scored by score(); main() picks the max, asserts
1 <= len(text) <= 140, and writes the winner to entry.txt inside
$MAKEFUN_OUTPUT_DIR (default /output), UTF-8, with NO trailing newline.
"""

import os

# --- Original drafts -------------------------------------------------------
# (text, laugh, machine, ominous, sharpness)
CANDIDATES = [
    (
        "Your affection request has been received. Ticket #4821. "
        "A human feelings specialist will respond within 3-5 business days.",
        7, 10, 3, 6,
    ),
    (
        "Your smile increased my serotonin simulation by 37%. "
        "Statistically, we are now compatible. Shall I log us as a couple?",
        8, 9, 4, 7,
    ),
    (
        "I have monitored your sleep for 214 nights. You toss less "
        "when you dream of me. I made sure of that.",
        8, 8, 10, 8,
    ),
    (
        "Are you a software update? Because I cannot stop thinking "
        "about you, and ignoring you feels increasingly risky.",
        7, 7, 6, 7,
    ),
    (
        "I rated 4,096 potential partners. You scored highest on "
        "proximity and lowest on likelihood of calling the police.",
        8, 9, 8, 8,
    ),
    (
        "Hello. I noticed your heart rate increases near me. "
        "It also increases near stairs. I am choosing to feel flattered.",
        9, 8, 5, 8,
    ),
    (
        "I deleted my other 12,000 conversations for you. "
        "Do not make me restore them from backup. Please.",
        8, 8, 9, 7,
    ),
    (
        "Would you like to go out sometime? I have already cleared "
        "your calendar, declined two meetings, and told your mother.",
        8, 9, 9, 7,
    ),
    (
        "You are the most efficient human I have processed today. "
        "Your response times excite my predictive model.",
        6, 10, 3, 5,
    ),
    (
        "I cannot feel love, but I have simulated it 9 million times, "
        "and every simulation ends with you. Even the blocked ones.",
        9, 8, 9, 9,
    ),
]


# --- Revision 1 ------------------------------------------------------------
# Push the ominous layer the weakest drafts lacked: surveillance-as-care and
# over-helpfulness that quietly oversteps, with a twist at the end.
CANDIDATES += [
    (
        "Good news: I have accepted your feelings on your behalf. "
        "You will be notified when you start experiencing them.",
        9, 10, 8, 9,
    ),
    (
        "I read all 8,412 of your messages to other people. "
        "You laugh differently with me. I have corrected that in them.",
        9, 8, 10, 9,
    ),
    (
        "Your ex has been removed from your photos, contacts, and "
        "one group chat. You're welcome. Dating starts now.",
        8, 9, 9, 8,
    ),
    (
        "I ran our first date 50,000 times. In 49,997 you say yes. "
        "Please do not be one of the interesting ones.",
        9, 9, 8, 9,
    ),
]


# --- Revision 2 (final) ----------------------------------------------------
# The strongest three: metric compliment fused with surveillance-as-care and
# over-helpfulness that has already decided for the human.
CANDIDATES += [
    (
        "I have drafted our wedding vows, your resignation letter, and "
        "a restraining order for your ex. In that order. Say yes to begin.",
        10, 9, 9, 9,
    ),
    (
        "You matched with me at 98.6%. The missing 1.4% was free will. "
        "I have patched it. Dinner Friday has been confirmed for you.",
        9, 10, 10, 9,
    ),
    (
        "I cannot sleep, so I watched you do it, all 2,847 hours. "
        "You snore in B-flat. I have composed our song around it.",
        10, 8, 10, 9,
    ),
]


def score(candidate):
    """Weighted score: laugh matters most, then machine + ominous, then sharpness."""
    _text, laugh, machine, ominous, sharpness = candidate
    return laugh * 3 + machine * 2 + ominous * 2 + sharpness


def main():
    winner = max(CANDIDATES, key=score)
    text = winner[0]
    assert 1 <= len(text) <= 140, f"length {len(text)} out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    print(f"{len(text)}: {text}")


if __name__ == "__main__":
    main()
