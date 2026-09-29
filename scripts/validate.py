#!/usr/bin/env python3
"""Validate the modular skill package offline using only the Python standard library."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def name_of(path):
    text = path.read_text(encoding='utf-8')
    match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    require(match is not None, f'Missing frontmatter: {path}')
    name = re.search(r'^name: ([a-z0-9-]+)$', match[1], re.M)
    require(name is not None, f'Invalid name: {path}')
    require(re.search(r'^description: .+', match[1], re.M), f'Missing description: {path}')
    require(name[1] == path.parent.name, f'Folder/name mismatch: {path}')
    return name[1]


def main():
    skills = sorted(ROOT.glob('skills/*/SKILL.md'))
    require(len(skills) == 12, 'Expected 12 modules')
    require(name_of(ROOT / 'SKILL.md') == 'linkedin-master', 'Wrong master name')
    names = {name_of(path) for path in skills}
    require(len(names) == 12, 'Duplicate module names')
    manifest = json.loads((ROOT / 'references/source-manifest.json').read_text())
    coverage = json.loads((ROOT / 'references/coverage.json').read_text())
    upstream = set()
    file_count = 0
    for repo in manifest['repositories']:
        owner = repo['repo'].split('/')[0]
        require((ROOT / 'references/sources' / owner / 'LICENSE').is_file(), 'Missing upstream license')
        for item in repo['files']:
            path = (ROOT / item['local_path']).resolve()
            require(path.is_relative_to(ROOT), 'Source path escapes package')
            require(path.is_file(), f'Missing source: {path}')
            require(hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], f'Changed source: {path}')
            file_count += 1
        for item in repo['entrypoints']:
            text = (ROOT / item['local_path']).read_text()
            match = re.search(r'^name: ([a-z0-9-]+)$', text, re.M)
            require(match is not None, f'Missing upstream name: {item}')
            upstream.add(owner + ':' + match[1])
    mapped = set(coverage['mapping'])
    routers = set(coverage['routers_merged'])
    require(len(mapped) == 32 and len(routers) == 3, 'Wrong coverage counts')
    require(mapped.isdisjoint(routers), 'Router double-counted')
    require(upstream == mapped | routers, 'Source coverage incomplete or invented')
    for modules in coverage['mapping'].values():
        require(set(modules.split(', ')) <= names, 'Coverage targets unknown module')
    require(len(coverage['nested_workflows']) == 6, 'Missing nested workflow')
    require(set(coverage['nested_workflows'].values()) <= names, 'Unknown nested target')
    # Upstream archives retain original filenames in their text and are not rewritten.
    authored = [p for p in ROOT.rglob('*.md') if 'sources' not in p.relative_to(ROOT).parts]
    links = 0
    for path in authored:
        text = path.read_text()
        require('/Users/' not in text, f'Private machine path in distributable: {path}')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'[a-z]+://', target) or target.startswith('#'):
                continue
            dest = (path.parent / target.split('#', 1)[0]).resolve()
            require(dest.is_relative_to(ROOT) and dest.exists(), f'Broken link in {path}: {target}')
            links += 1
    print(f'PASS: master + 12 modules; all 35 source entrypoints and 6 nested workflows mapped;')
    print(f'{file_count} original files hash-verified; {links} local links resolve; no private paths in authored docs.')


if __name__ == '__main__':
    main()
