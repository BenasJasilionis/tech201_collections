story1 = {
    "start": "Sotark found his mind wandering to the strange events of the previous night as he was patrolling the cold, cobblestone streets of Sparta. The evening started as any other: He, alongside his fellow spartans was to take watch and guard Sparta and her people from the enemies which lurked in the dark. This is a task that Sotrak took seriously, and one that he had carried out countless nights before with little difficulty. At most, he may cross paths with a thief masquerading as a lowly beggar. On some rare occasions, a rogue raiding party may attempt to reach the city. Regardless of the threat, it never got within reach of the city. But yesterday was different... ",
    "middle": "A cloaked figure began approaching the spartans. Thinking this to be a another thief, one of Sotark's comrades went to swiftly deal with the unwanted guest, but before he could even raise his shield, the figure raised a bony arm and blasted the warrior with what seemed like the fires of Hades itself. The Spartans were shocked, but they were not dissuaded, for they knew what was at stake. Instinctively, the spartans raised their shields and began advancing, however the mysterious figure, snaked through their defences like no foe had before. 1 by 1 the spartans fell, and just as it seemed that Sotark was going to join his comrades in Elysium, something unexpected happened.",
    "end": "The clouds parted and the lightning of Zeus came crashing down into Sotark, but instead of turning him to ash, it empowered him. Sensing this, Sotark arose once more and aimed his spear at the enemy. Before the fiend could react, Sotark launched his spear with the power of Zeus and vanquished the foe."
}
print(story1)

print(type(story1))

print(story1.keys())

print(story1.values())

print(story1.get("start"))
print(story1.get("middle"))
print(story1.get("end"))

story1["hero"] = "Sotark"

print(story1.keys())