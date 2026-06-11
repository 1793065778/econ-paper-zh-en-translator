# Markdown Output Templates

Produce two separate Markdown files by default. Do not combine Chinese source text, English draft, and review notes in one file.

For full manuscripts, produce these files by batching first. Read `long-output-batching.md`; write `draft_parts/` and `review_parts/`, then assemble the final two Markdown files only after all parts are complete.

## `英文全文成稿.md`

This file is the clean English manuscript draft.

Required structure:

```markdown
# <English Title>

## Abstract

<English abstract>

## <Section Heading>

<!-- S01-P001 -->
<English paragraph>

<!-- S01-P002 -->
<English paragraph>
```

Rules:

- Include only the English draft and stable paragraph IDs.
- Do not include Chinese source paragraphs.
- Do not include translation notes, doubts, or handling explanations.
- Preserve references, equations, variable symbols, statistics, and numeric results.
- Translate title, abstract, headings, body, footnotes, figure titles, figure notes, table titles, and table notes.

## `翻译审校说明.md`

This file centralizes review information.

Required structure:

```markdown
# 翻译审校说明

## 1. 术语、缩写与变量表

<terminology table>

## 2. 段落处理说明

### S01-P001

- Section:
- Key terms:
- Handling notes:
- Compression decision:
- Coverage retained:
- Readability revision:
- Translator-added connective or explanatory handling:
- Questions or confirmation needed:
- Protected items:

## 3. 译者补足/解释性处理清单

## 4. 疑问与待确认项

## 5. 保护项清单

## 6. 覆盖审计结果
```

Rules:

- Keep notes concise but traceable by paragraph ID.
- Record abstract or paragraph compression decisions when source sentences are consolidated.
- Record readability revisions when long Chinese sentences are split or reordered for clearer English.
- List every explanatory addition.
- List every unresolved terminology choice.
- Include coverage audit status when `translation_units.json` is available.
