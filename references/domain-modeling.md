# Sharpen the domain model only where it changes

Use when defining or changing domain terms, entity relationships, or responsibility boundaries. Reading familiar vocabulary alone does not require a modeling exercise. Keep the current outcome, scope, and permissions; do not turn a terminology question into a redesign.

## Resolve meaning against concrete cases

Read the relevant existing glossary or `CONTEXT.md`. If `CONTEXT-MAP.md` exists, follow it to the affected context rather than flatten different domains into one global vocabulary. Read the relevant behavior record and code to distinguish intended behavior from what is implemented.

Challenge overloaded terms with precise alternatives. For example, does "account" mean a person who signs in, or the organization that pays? Test the distinction with concrete cases such as two people sharing one customer, one person belonging to two customers, or an ownership transfer. Choose cases that expose this assignment's unresolved relationship, not a speculative future domain.

When conversation, glossary, and code disagree, make the discrepancy explicit. Apply an already-authorized decision; ask only if a material meaning, ownership rule, or behavior remains unresolved. Code is evidence of implementation, not authority to override the intended model.

## Capture the resolved vocabulary

For authorized documentation or implementation work, update the existing glossary as terms become settled. If none exists and the resolved domain language needs to persist, create a small `CONTEXT.md` in the affected context. A consultation-only or read-only request ends with the proposed definitions in the response, without writing files.

Use the project's format. When none exists, a context title, one-sentence purpose, and short definitions suffice:

```markdown
## Language

**Customer**: A person or organization that purchases the service.
_Avoid_: Account, client

**User**: A person identified within the service, distinct from the purchasing customer.
```

Keep each definition to one or two sentences, with misleading aliases only when useful. Include domain-specific concepts, not a dictionary of general programming terms. Do not overwrite an existing `CONTEXT.md`'s other established uses to force this format.

The glossary records meaning; behavior scenarios belong in the existing spec, and implementation plans stay in the existing change record. Do not copy them into the glossary or create a second requirements ledger. A newly discovered behavior delta still needs the root workflow's scope and acceptance handling.

## Record consequential decisions sparingly

Use an ADR only when the decision is costly to reverse, would surprise a future reader without context, and reflects a real trade-off. An obvious or easily reversible choice needs no ADR.

Reuse the project's ADR location and numbering. If a qualifying decision needs a record and no convention exists, create `docs/adr/0001-<decision>.md` lazily. A title and one short paragraph giving context, choice, and reason are enough; add alternatives or consequences only when they explain a material trade-off. Capture a settled, authorized decision without asking for approval again; keep unresolved choices marked as proposals.

Adapted from Matt Pocock's domain-modeling method and formats; attribution and license are in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
