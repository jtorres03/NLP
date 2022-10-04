from typing import List
from yake import KeywordExtractor


def get_keywords(text: str) -> List[str]:
    keys = KeywordExtractor(n=3, dedupLim=0.25, top=5).extract_keywords(text)
    return [phrase for phrase, _ in keys]


para = "Adopt responsibility for your own well-being, try to put your family together, try to serve your community, try to seek for eternal truth... That's the sort of thing that can ground you in your life, enough so that you can withstand the difficulty of life."

print(get_keywords(para))