# Synthetic transfer service

This tiny service exists only to demonstrate exact-revision incident
investigation. All identifiers and ledger events in the companion fixtures are
generated examples. It must not be connected to a real bank, payment rail,
customer account, or production ledger.

The demo intentionally contains two historical revisions so First Signal can
retrieve the code that an affected instance actually ran and compare it with
the previous deployed revision. The repository does not contain a later fix or
an incident-resolution answer.
