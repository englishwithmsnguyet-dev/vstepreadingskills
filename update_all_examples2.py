import re

html_file = '/Users/nguyetpham/Desktop/WEBSITE/B1 ONLINE/readinglesson/web-lesson/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

examples = [
    # T1 E1
    r"Desert ecosystems pose extreme challenges for plant life due to the scarcity of rainfall and intense heat. To adapt to these harsh conditions, some plants are <strong>succulent</strong>, such as cacti and aloe vera, which are able to store water in their thick, fleshy leaves. This unique adaptation allows them to survive prolonged periods of drought without perishing.",
    # T1 E2
    r"The delicate balance of an ecosystem relies heavily on the interactions between different species. In any food web, many <strong>predators</strong>, including lions, wolves, and eagles, hunt other animals for food to survive in the wild. Their hunting behaviors not only provide them with necessary nutrients but also help regulate the population of smaller herbivores, preventing overgrazing.",
    
    # T2 E1
    r"Animals have developed various behavioral patterns to avoid competition and extreme temperatures. For instance, while most birds forage for food in the morning sunlight, owls are strictly <strong>nocturnal</strong>, which means they are active during the night and sleep during the day. Their specialized eyesight and silent flight feathers make them highly effective hunters in complete darkness.",
    # T2 E2
    r"Following the devastating economic crisis, the country faced soaring inflation rates and massive budget deficits. In an urgent attempt to stabilize the economy, the government implemented a new policy of <strong>austerity</strong>, which means strict control over public spending to reduce national debt. Citizens were forced to accept significant cuts to healthcare, education, and public transportation funding.",

    # T3 E1
    r"Siblings raised in the exact same household can develop remarkably different personality traits as they grow up. Unlike her <strong>sociable</strong> older sister who loves going to noisy parties and making new friends, Mai is quite shy and prefers staying home with a good book. This striking contrast in their temperaments often surprises their relatives during family gatherings.",
    # T3 E2
    r"Maintaining a consistent sleep schedule is vital for overall well-being and daily productivity. Although Mary usually feels energetic in the morning and easily completes her early workouts, today she felt incredibly <strong>exhausted</strong> and struggled to get out of bed. The sudden change in her energy levels was likely caused by staying up late to finish a demanding project the previous night.",

    # T4 E1
    r"Engineers have recently developed a revolutionary synthetic fabric designed for high-performance athletic wear. Testing reveals that the material is incredibly <strong>resilient</strong>, as flexible and durable as rubber, able to bend and stretch repeatedly without breaking. This remarkable property ensures that athletes can perform intense movements without worrying about their garments tearing.",
    # T4 E2
    r"During the excavation of the lost city, the research team uncovered a beautifully decorated artifact buried beneath layers of sand. The ancient vase was as <strong>fragile</strong> as thin glass, requiring the archaeologists to handle it with extreme care. Even the slightest vibration or improper grip could have shattered the priceless relic into countless irreparable pieces.",

    # T5 E1
    r"The company had been preparing for the most critical presentation of the year, expecting a flawless execution from the marketing team. However, the manager was absolutely <strong>furious</strong> when he heard about the major data mistake on the final slides. His anger was visible on his face as he aggressively shouted at the staff, completely disrupting the previously calm office environment.",
    # T5 E2
    r"A balanced diet combined with regular physical activity forms the foundation of a healthy lifestyle. However, experts continuously emphasize that drinking plenty of water is <strong>essential</strong> for your health. Furthermore, this vital habit helps maintain your skin's moisture, regulates body temperature, and effectively flushes out accumulated toxins from your system."
]

# We are going to find all:
# <div style="background: #f8fafc; border-left: 4px solid #cbd5e1; border-radius: 8px; padding: 14px; margin-bottom: 14px; font-size: 1.05rem; line-height: 1.7; color: #1e293b;">
# ...
# </div>
# that follow the VÍ DỤ MINH HOẠ text.

pattern = re.compile(r'(VÍ DỤ MINH HOẠ [12]</div>\s*<div[^>]*border-left: 4px solid #cbd5e1[^>]*>)(.*?)(</div>)', re.DOTALL)

matches = pattern.finditer(content)

new_content = ""
last_end = 0
match_idx = 0

for match in matches:
    if match_idx < len(examples):
        new_content += content[last_end:match.start(2)]
        new_content += "\n            " + examples[match_idx] + "\n        "
        last_end = match.end(2)
        match_idx += 1
    else:
        break

new_content += content[last_end:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {match_idx} examples.")
