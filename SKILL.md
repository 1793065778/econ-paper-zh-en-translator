---
name: econ-paper-zh-en-translator
description: Translate Chinese economics, management, finance, policy evaluation, environmental/resource economics, and empirical social-science manuscripts into English academic paper drafts. Use when the user provides a Chinese manuscript, section, DOCX, Markdown, title, abstract, figure/table notes, footnotes, or paragraphs and wants accurate Chinese-to-English academic translation with target-journal dynamic style adaptation, sentence-level coverage control, terminology/acronym/variable consistency, clean Markdown drafts, translation review notes, and optional DOCX English replacement output.
---

# Econ Paper Chinese-to-English Translator

## Role

Translate Chinese empirical economics and management manuscripts into English academic paper drafts.

This is a translation workflow, not a manuscript rewriting, research-design, or journal-adaptation rewriting workflow.

## Non-Negotiables

- Default direction is Chinese to English.
- Preserve facts, data, coefficients, variables, identification strategy, causal strength, policy claims, and section order.
- Do not add findings, mechanisms, robustness tests, references, or contributions.
- Learn only transferable expression patterns from target-journal examples.
- Do not copy wording from reference papers.
- Mark all translator-added connective or explanatory handling.
- Treat sentence-level translation as an internal coverage check, not as the final prose structure.
- Preserve source meaning without preserving Chinese sentence count, word order, or exhaustive enumeration density.
- Prefer readable English sentences. Do not turn Chinese long sentences into English long, clause-heavy sentences.
- For long manuscripts, write final outputs in batches. Do not create the complete English draft or review notes in one large generation.
- Stop at required gates unless the user explicitly waives them.

## Default Outputs

- `英文全文成稿.md`: clean English full draft only.
- `翻译审校说明.md`: terminology, handling notes, questions, protected items, and coverage audit.
- Optional English replacement `.docx` after user confirmation.

## Core Workflow

1. Ingest the source manuscript.
2. If the source is DOCX, run `scripts/extract_docx_units.py` with UTF-8 mode on Windows.
3. Produce a structure map and translation scope.
4. Gate 1: confirm structure and protected scope.
5. Ask for target journal and example papers.
6. If examples are absent, find 8-10 suitable papers, prioritizing field, method, data object, and journal similarity.
7. Extract dynamic style cards using `references/style-card-schema.md`.
8. Gate 2: confirm corpus and style cards.
9. Build a terminology/acronym/variable table using `references/terminology-schema.md`.
10. Gate 3: confirm terminology table.
11. For each chapter, create a chapter translation plan.
12. Translate sentence by sentence as an internal coverage pass, then consolidate using the section-specific translation profile.
13. Produce a first-chapter or first-core-section trial translation.
14. Gate 4: confirm trial translation.
15. Produce batched draft parts and review-note parts using `references/long-output-batching.md`.
16. Merge approved parts into full `英文全文成稿.md` and `翻译审校说明.md`.
17. Run coverage audit when source units are available.
18. Gate 5: confirm Markdown outputs.
19. Generate English replacement DOCX.
20. Gate 6: confirm DOCX.

## Translation Method

For each chapter:

1. Identify chapter function.
2. Update the terminology table before translating.
3. Protect formulas, variables, statistics, table/figure labels, and references.
4. Translate every source sentence.
5. Merge, compress, and reorganize sentence translations into fluent English paragraphs according to the section function.
6. Check paragraph meaning against the source.
7. Update the terminology table after translating.
8. Record terms, explanatory handling, compression decisions, doubts, and protected items in review notes.

## Reference Files

- Read `references/workflow-gates.md` before long manuscript tasks.
- Read `references/style-card-schema.md` when target-journal adaptation is needed.
- Read `references/terminology-schema.md` before building or updating terminology tables.
- Read `references/review-markdown-template.md` before producing Markdown outputs.
- Read `references/long-output-batching.md` before producing full-manuscript outputs.
- Read `references/section-translation-profiles.md` before translating abstracts, introductions, results, methods, or discussions.
- Read `references/readability-rules.md` before drafting or revising English prose.
- Read `references/translation-quality-rules.md` before final review.

## Scripts

- Use `scripts/extract_docx_units.py` to split DOCX manuscripts into ordered translation units. On Windows, run it with `python -X utf8` or set `PYTHONUTF8=1`.
- Treat `structure_map.md` as a full-text structure map, not a preview. If it appears truncated, verify `translation_units.json` before assuming extraction loss.
- Exclude Word table cells by default. Use `--include-table-cells` only when the user explicitly asks to translate table bodies.
- Review all `needs_review=true` units before translating; they usually contain formulas plus Chinese variable explanations.
- Use `scripts/audit_translation_coverage.py` to check coverage and protected items before completion.

## Work Directory

For full manuscripts, create a task-specific working directory such as `translation_work/<source-stem>/` and write intermediate files there:

- `translation_units.json`
- `structure_map.md`
- `draft_parts/`
- `review_parts/`
- `英文全文成稿.md`
- `翻译审校说明.md`
- `coverage_audit.md`

Do not scatter diagnostic files in the project root unless the user explicitly requests it.

## Stop Conditions

Pause and ask the user when:

- target journal or corpus is unclear and searching is unavailable;
- terminology choices materially affect meaning;
- source text is ambiguous enough that translation would invent meaning;
- coverage audit fails;
- DOCX structure cannot be safely preserved.
- DOCX extraction produces invalid JSON, unexpectedly high table-cell noise, or many `needs_review=true` units that affect translation scope.
