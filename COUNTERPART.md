# Production counterpart identity

This test repository does not currently have an admitted production counterpart owner/repository mapping.

Do **not** infer a production owner by stripping `-test` from `r2g-test`. The GitHub account `r2g` is a separate user account, and the `r2g-test/.github` relationship registry currently declares no cross-organization edge that authorizes this repository to treat that account as its production source.

Until an explicit counterpart is added to reviewed machine-readable governance, this repository may run its local deterministic upgrade-compatibility suite and shared public dependency canaries, but it must not crawl, certify, or make promotion claims about another GitHub owner.

A future counterpart declaration must bind at least:

- production GitHub owner and owner type;
- stable owner ID when available;
- one or more admitted source repositories or a reviewed discovery scope;
- the governing relationship-registry entry;
- access mode for private sources;
- the exact-head evidence policy used by this sibling test repository.

Once that declaration exists, counterpart workflows should read it directly. Filename conventions and suffix stripping are hints at most; they are never trust anchors.
