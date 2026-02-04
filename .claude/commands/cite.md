---
name: cite
description: Quick citation lookup with OA and retraction status
user_prompt: true
---

# /cite {DOI}

Quick citation lookup utility that retrieves metadata, open access status, and retraction status for a given DOI.

## Instructions

### Step 1: Validate DOI Format

Check that the input is a valid DOI format:
- Must start with `10.` followed by registrant code
- Contains a `/` separator
- Examples: `10.1038/nature12373`, `10.1145/3292500.3330701`

If invalid format:
```
ERROR: Invalid DOI format

Expected format: 10.XXXX/YYYY
Examples:
  - 10.1038/nature12373
  - 10.1145/3292500.3330701
  - 10.48550/arXiv.2301.00001

Tip: Remove any URL prefix (https://doi.org/)
```
**Stop.**

### Step 2: Query Crossref for Metadata

Use `mcp__crossref__getWorkByDOI` to retrieve:
- Title
- Authors
- Publication year
- Journal/venue
- Type (journal-article, conference-paper, preprint, etc.)
- Citation count (if available)
- **Retraction status** (check for "update-to" or "retracted" flags)

If DOI not found:
```
ERROR: DOI not found in Crossref

DOI: {doi}
Status: Not registered or invalid

Suggestions:
- Verify the DOI is correct
- Check if it's a preprint (try arXiv ID instead)
- Some recent papers may not be indexed yet
```
**Stop.**

### Step 3: Query Unpaywall for Open Access Status

Use WebFetch to query:
```
https://api.unpaywall.org/v2/{doi}?email=research@example.com
```

Extract from response:
- `is_oa`: true/false
- `oa_status`: gold | green | hybrid | bronze | closed
- `best_oa_location.url`: Best open access URL
- `best_oa_location.version`: published | accepted | submitted

### Step 4: Determine Tier

Based on metadata, assign tier:

| Tier | Criteria |
|------|----------|
| **1** | Peer-reviewed journal (IF known), major conference proceedings |
| **2** | arXiv/preprint, patents, technical reports |
| **3** | Other (book chapters, datasets, etc.) |

### Step 5: Format APA Citation

Generate APA 7th edition citation:

**Journal Article:**
```
Author, A. A., & Author, B. B. (Year). Title of article. Journal Name, Volume(Issue), Page–Page. https://doi.org/xxxxx
```

**Conference Paper:**
```
Author, A. A. (Year). Title of paper. In Proceedings of Conference Name (pp. Page–Page). Publisher. https://doi.org/xxxxx
```

**Preprint:**
```
Author, A. A. (Year). Title of preprint. arXiv. https://doi.org/xxxxx
```

### Step 6: Output Citation Report

```
## Citation Report

### Formatted Citation (APA 7)
{formatted_citation}

---

### Metadata
| Field | Value |
|-------|-------|
| Title | {title} |
| Authors | {authors} |
| Year | {year} |
| Venue | {journal/conference} |
| Type | {type} |
| DOI | {doi} |
| Tier | {1/2/3} |

---

### Open Access Status
| Field | Value |
|-------|-------|
| Is OA | {Yes/No} |
| OA Type | {gold/green/hybrid/bronze/closed} |
| Version | {published/accepted/submitted} |
| Best URL | {url or "N/A"} |

**OA Type Meanings:**
- **Gold**: Published in OA journal
- **Green**: Self-archived (repository)
- **Hybrid**: OA article in subscription journal
- **Bronze**: Free to read but no license
- **Closed**: Paywalled

---

### Retraction Status
| Field | Value |
|-------|-------|
| Status | {Active/Retracted/Concern} |
| Retraction Date | {date or "N/A"} |
| Reason | {reason or "N/A"} |

{If retracted:}
⚠️ WARNING: This paper has been retracted. Do not cite.

{If expression of concern:}
⚠️ CAUTION: Expression of concern exists. Review before citing.

---

### Quick Copy

**BibTeX:**
```bibtex
@article{{key,
  author = {{{authors}}},
  title = {{{title}}},
  journal = {{{venue}}},
  year = {{{year}}},
  doi = {{{doi}}}
}}
```

**Markdown:**
[{short_title}]({best_url})
```

### Step 7: Handle Edge Cases

**arXiv DOIs (10.48550/arXiv.*):**
- Also query arXiv API for additional metadata
- Check if peer-reviewed version exists
- Note: "Preprint - check for published version"

**No Unpaywall data:**
```
### Open Access Status
Unable to retrieve OA status from Unpaywall.
- DOI may be too new
- Try searching Google Scholar for OA versions
```

**Multiple versions:**
If Unpaywall shows multiple locations, list top 3:
```
### Available Versions
1. {version1} - {url1}
2. {version2} - {url2}
3. {version3} - {url3}
```

---

## Tool Reference

### Required Tools
1. `mcp__crossref__getWorkByDOI` - Primary metadata source
2. `WebFetch` - Query Unpaywall API

### Optional Tools (for enhanced lookup)
- `mcp__arxiv__search_papers` - For arXiv preprints
- `mcp__openalex__get_work` - Alternative metadata source

---

## Examples

### Example 1: Standard Journal Article
```
/cite 10.1038/nature12373
```

### Example 2: arXiv Preprint
```
/cite 10.48550/arXiv.2301.00001
```

### Example 3: Conference Paper
```
/cite 10.1145/3292500.3330701
```

---

## Error Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid DOI format | Missing `10.` prefix or `/` | Check DOI format |
| DOI not found | Not registered in Crossref | Verify DOI, try alternate sources |
| Unpaywall timeout | API unavailable | Retry or skip OA check |
| Retracted paper | Paper was retracted | Do not cite, find alternative |
