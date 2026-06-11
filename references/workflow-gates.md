# Workflow Gates

Use these gates for long manuscripts, DOCX inputs, or any task where missing text, terminology drift, or target-journal style adaptation would create risk. A user may explicitly waive a gate, but do not infer waiver from urgency.

## Gate 1: Structure Confirmation

Show:

- detected sections and headings
- unit counts by type
- full-text structure map location
- JSON validity check result
- excluded table cell and non-empty table paragraph counts
- parts to translate
- parts to preserve
- ambiguous items
- units marked `needs_review=true`
- likely misclassified units
- items the script marked preserve but may need translation
- items the script marked translate but may need preservation

Wait for the user to confirm translation scope before translating at scale.

If the user thinks the structure map is incomplete, first check whether the map is full text or only a preview. Then verify the corresponding `source_text` in `translation_units.json` before deciding that extraction failed.

By default, Word table cells are excluded because regression tables and numeric table bodies are usually not translation targets. If the user's table titles or notes are inside table cells, report that limitation and ask whether to rerun extraction with `--include-table-cells`.

## Gate 2: Corpus And Style Card Confirmation

Show:

- user-provided examples included or excluded
- AI-found examples if the user did not provide enough examples
- why each example is relevant
- dynamic style cards
- transfer limits

Wait for approval before applying target-journal style.

## Gate 3: Terminology Confirmation

Show:

- initial terminology/acronym/variable table
- terms whose English rendering affects meaning
- abbreviations and first-use rules
- forbidden renderings
- unresolved items

Wait for confirmation when choices affect meaning or consistency.

## Gate 4: Trial Translation Confirmation

Show a first-chapter or first-core-section trial translation and compact review notes.

Ask the user to confirm:

- fidelity
- style fit
- terminology choices
- explanatory handling level
- causal and policy language strength

Do not translate the whole manuscript until the trial is approved unless the user waives this gate.

## Gate 5: Markdown Output Confirmation

Show or save:

- `英文全文成稿.md`
- `翻译审校说明.md`
- coverage audit status when available

Wait for confirmation before DOCX replacement.

## Gate 6: DOCX Confirmation

Generate an English replacement DOCX only after Gate 5. Report any formatting or replacement limits. Ask the user to confirm the final DOCX.
