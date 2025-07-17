import csv
from datetime import datetime,timezone

def convert_date(published_time):

    # Parse ISO8601 with timezone info
    dt = datetime.fromisoformat(published_time)

    # Convert to readable format (in UTC)
    readable = dt.strftime("%B %d, %Y %I:%M %p")

    return readable


def csvtoset():
        
    value_set = set()

    with open('data/verbs.csv', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for cell in row:
                cell = cell.strip()
                if cell:  # skip empty or whitespace-only cells
                    value_set.add(cell)

    return value_set




def is_probably_noun_based(name):
    name = name.lower().strip()
    words = name.split()

    # More comprehensive prepositions list
    prepositions ={
      "a",
      "abaft",
      "aboard",
      "about",
      "above",
      "absent",
      "across",
      "afore",
      "after",
      "against",
      "along",
      "alongside",
      "amid",
      "amidst",
      "among",
      "amongst",
      "an",
      "anenst",
      "apropos",
      "apud",
      "around",
      "as",
      "aside",
      "astride",
      "at",
      "athwart",
      "atop",
      "barring",
      "before",
      "behind",
      "below",
      "beneath",
      "beside",
      "besides",
      "between",
      "beyond",
      "but",
      "by",
      "circa",
      "concerning",
      "despite",
      "down",
      "during",
      "except",
      "excluding",
      "failing",
      "following",
      "for",
      "forenenst",
      "from",
      "given",
      "in",
      "including",
      "inside",
      "into",
      "lest",
      "like",
      "mid",
      "midst",
      "minus",
      "modulo",
      "near",
      "next",
      "notwithstanding",
      "of",
      "off",
      "on",
      "onto",
      "opposite",
      "out",
      "outside",
      "over",
      "pace",
      "past",
      "per",
      "plus",
      "pro",
      "qua",
      "regarding",
      "round",
      "sans",
      "save",
      "since",
      "than",
      "the",
      "through",
      "throughout",
      "till",
      "times",
      "to",
      "toward",
      "towards",
      "under",
      "underneath",
      "unlike",
      "until",
      "unto",
      "up",
      "upon",
      "versus",
      "via",
      "vice",
      "with",
      "within",
      "without",
      "worth"
    }
    # Extended verb list (common verbs + auxiliaries + modals)
    verbs = csvtoset()

    conjunctions = {
        "and", "or", "but", "so", "yet", "for", "nor", "although", "though", "because", "if", "when", "while", "unless", "where", "as"
    }

    articles = {"a", "an", "the"}

    pronouns = {
        "i", "you", "he", "she", "it", "we", "they",
        "me", "him", "her", "us", "them",
        "my", "your", "his", "its", "our", "their",
        "mine", "yours", "hers", "ours", "theirs",
        "this", "that", "these", "those", "who", "whom", "whose", "which"
    }

    # Combine all non-noun word types
    non_noun_words = prepositions | verbs | conjunctions | articles | pronouns

    for word in words:
        if word in non_noun_words:
            return False  # Contains a non-noun word
    return True
    

