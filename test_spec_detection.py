#!/usr/bin/env python3
"""Test script to diagnose SPEC.md detection bug."""

import re
from pathlib import Path

def is_spec_empty_or_template_CURRENT(content: str) -> bool:
    """Current implementation (buggy)."""
    content = content.strip()
    if not content:
        return True

    # Check for template placeholders
    template_markers = [
        '[Define your research question here]',
        '[One-sentence research question here]',
        '[Expand your research question here',
    ]
    for marker in template_markers:
        if marker in content:
            return True

    # Check if SPEC_BRIEF section exists and is filled in
    brief_match = re.search(r'## SPEC_BRIEF\s*\n(.*?)(?=\n---|\n## |\Z)', content, re.DOTALL)
    if brief_match:
        brief = brief_match.group(1).strip()
        brief = re.sub(r'<!--.*?-->', '', brief, flags=re.DOTALL).strip()
        if brief and len(brief) > 20:
            return False

    # Fallback: check if research question section is filled
    match = re.search(r'## Research Question.*?\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if match:
        question = match.group(1).strip()
        if question and len(question) > 20:
            return False

    return True  # <-- BUG: Falls through even with substantial content


def is_spec_empty_or_template_FIXED(content: str) -> bool:
    """Fixed implementation."""
    content = content.strip()
    if not content:
        return True

    # Check for template placeholders
    template_markers = [
        '[Define your research question here]',
        '[One-sentence research question here]',
        '[Expand your research question here',
        '[Constraint 1]',  # Added: common unfilled placeholder
    ]
    for marker in template_markers:
        if marker in content:
            return True

    # Remove HTML comments for content analysis
    clean_content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL).strip()

    # Check if SPEC_BRIEF section exists and is filled (with or without ## prefix)
    # Made regex more flexible: optional ## prefix
    brief_match = re.search(r'(?:^|\n)#*\s*SPEC_BRIEF\s*\n(.*?)(?=\n---|\n#|\Z)', clean_content, re.DOTALL | re.IGNORECASE)
    if brief_match:
        brief = brief_match.group(1).strip()
        if brief and len(brief) > 20:
            return False

    # Fallback: check if research question section is filled (with or without ## prefix)
    match = re.search(r'(?:^|\n)#*\s*Research Question[^\n]*\n(.*?)(?=\n#|\Z)', clean_content, re.DOTALL | re.IGNORECASE)
    if match:
        question = match.group(1).strip()
        if question and len(question) > 20:
            return False

    # NEW: Last resort - if cleaned content is substantial, consider it filled
    # This catches cases where the format is completely different
    if len(clean_content) > 500:  # More than ~100 words
        return False

    return True


# Test cases
test_cases = [
    ("Empty", ""),
    ("Template only", """# Research Specification

## SPEC_BRIEF
<!-- 12-20 LINES MAX. -->
[One-sentence research question here]

**Key constraints:**
- [Constraint 1]
"""),
    ("Valid SPEC_BRIEF (standard format)", """# Research Specification

## SPEC_BRIEF
What are the best practices for MCP server development?

**Key constraints:**
- Focus on security
- Anthropic official docs preferred

**Success = ** Summary of patterns

---

## Created
2026-02-02
"""),
    ("Valid but NO ## headers (probability-system format)", """Research Specification
Created

2026-02-02 19:11:18

Workspace

probability-system-research

Research Question

Can we design and validate a production-grade probability system that (1) produces calibrated true probabilities for single legs, (2) correctly estimates joint probabilities for parlays (including same-game parlays), and (3) constructs +EV parlay combinations in a way that is demonstrably achievable in practice?

Scope

In scope: Feasibility analysis, single-leg probability modeling, joint probability modeling, etc.
"""),
    ("Real smoke-test SPEC", """# Research Specification

## Created
2026-02-02 15:25:19

## Workspace
smoke-test

## Research Question
What are the current best practices for MCP (Model Context Protocol) server development?

## Scope
- **In scope:** MCP server architecture, tool design patterns, security considerations
- **Out of scope:** Client implementation details, non-Anthropic MCP variants
"""),
]

print("=" * 70)
print("SPEC.md Detection Bug Analysis")
print("=" * 70)

for name, content in test_cases:
    current = is_spec_empty_or_template_CURRENT(content)
    fixed = is_spec_empty_or_template_FIXED(content)
    
    status = "OK" if current == fixed else "BUG!"
    expected_empty = name in ["Empty", "Template only"]
    
    print(f"\nTest: {name}")
    print(f"  Current impl says empty: {current}")
    print(f"  Fixed impl says empty:   {fixed}")
    print(f"  Expected empty:          {expected_empty}")
    if current != expected_empty:
        print(f"  >>> CURRENT IMPLEMENTATION IS WRONG <<<")
    if fixed != expected_empty:
        print(f"  >>> FIXED IMPLEMENTATION IS WRONG <<<")

print("\n" + "=" * 70)
print("Regex Analysis")
print("=" * 70)

# Test the specific regex patterns
prob_spec = """Research Question

Can we design and validate a production-grade probability system?"""

print("\nTesting regex on content WITHOUT ## headers:")
print(f"Content sample: {prob_spec[:60]}...")

# Current regex (requires ##)
current_regex = r'## Research Question.*?\n(.*?)(?=\n##|\Z)'
match1 = re.search(current_regex, prob_spec, re.DOTALL)
print(f"\nCurrent regex: {current_regex}")
print(f"  Match: {match1}")

# Fixed regex (## optional)
fixed_regex = r'(?:^|\n)#*\s*Research Question[^\n]*\n(.*?)(?=\n#|\Z)'
match2 = re.search(fixed_regex, prob_spec, re.DOTALL)
print(f"\nFixed regex: {fixed_regex}")
print(f"  Match: {match2}")
if match2:
    print(f"  Captured: {match2.group(1)[:50]}...")
