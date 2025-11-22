from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    for i in range(len(pattern) - 1): # Not including the last character becaause if it is mismatched we want to slide by pattern length
        table[pattern[i]] = len(pattern) - i - 1
    return table

class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, c: str) -> int:
        assert len(c) == 1
        if c in self.table:
            return self.table[c]
        return len(self.pattern)

    def search(self) -> int:
        pattern_len = len(self.pattern)
        text_len = len(self.text)
        
        # Start from the end of the pattern
        i = pattern_len - 1
        
        while i < text_len:
            # Compare pattern with text starting from the end of pattern
            j = pattern_len - 1
            
            while j >= 0 and self.pattern[j] == self.text[i]:
                i -= 1
                j -= 1
            
            # If we matched the entire pattern (j < 0), we found it
            if j < 0:
                return i + 1
            
            # Slide the pattern based on the mismatched character
            mismatch_char = self.text[i]
            slide_width = self.decide_slide_width(mismatch_char)
            i += max(1, slide_width)
        
        return -1
