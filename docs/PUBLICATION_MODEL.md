# Publication model

Public content is a curated derivative of a separately maintained canonical knowledge base. A canonical exporter selects approved rewritten material and keeps source provenance private. Private paths, customer evidence, proprietary contracts and runtime artifacts stay outside the release.

Install development dependencies from `requirements-dev.txt`, then run:

```text
python scripts/build_packages.py
python scripts/validate_public.py
python -m unittest discover -s tests
```

The build creates standalone skill references and GPT knowledge. Validation checks public-content boundaries and the generated SHA manifest; it does not verify PEKAT runtime behavior.

Publish the validated output after reviewing the diff and notices. Regenerate package files from maintained public sources rather than editing them independently.

After staging the reviewed files with Git, run `python scripts/validate_public.py --index`
to scan the exact publication blobs and confirm that the index matches the public
worktree. CI also performs this check. Ordinary worktree validation can run before
staging; neither validator pushes or changes Git state.
