"""Offline checks for the pinned README translation tasks (stdlib only)."""
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent


def parse(text):
    """Parse the block forms used by these baselines, preserving raw fence bytes.

    Prose blocks retain section order, table rows, list items and blockquotes so
    a translated heading cannot conceal a missing caveat paragraph. Preserve
    those boundaries; line wrapping inside a paragraph can change freely.
    """
    blocks, fences, headings = [], [], []
    paragraph = []
    fence = None
    raw = []
    table_rows = []

    def flush_table():
        if not table_rows:
            return
        assert len(table_rows) >= 2 and table_rows[1][0] == 'table-separator', 'Table header must be immediately followed by a delimiter row'
        assert all(kind == ('table-separator' if index == 1 else 'table') for index, (kind, _) in enumerate(table_rows)), 'Invalid table delimiter position'
        columns = [len(re.findall(r'(?<!\\)\|', re.sub(r'`[^`]*`', '', row))) - 1 for _, row in table_rows]
        assert len(set(columns)) == 1 and columns[0] > 0, 'Table column counts must match'
        table_rows.clear()

    def flush():
        if paragraph:
            blocks.append(('paragraph', '\n'.join(paragraph)))
            paragraph.clear()

    for line in text.splitlines(keepends=True):
        if fence:
            raw.append(line)
            if re.fullmatch(r' {0,3}' + re.escape(fence[0]) + r'{' + str(fence[1]) + r',}[ \t]*\r?\n?', line):
                fences.append(''.join(raw))
                fence, raw = None, []
            continue
        if not line.lstrip().startswith('|'):
            flush_table()
        assert not line.strip() or not re.match(r'^ {4}', line.expandtabs(4)), 'Indented code/prose is outside these simple Markdown tasks'
        match = re.match(r' {0,3}(`{3,}|~{3,})([^\r\n]*)', line)
        if match:
            flush()
            fence = (match[1][0], len(match[1]))
            raw = [line]
            blocks.append(('fence', ''))
            continue
        # Hidden HTML/comment text cannot supply the measured language content.
        assert not re.search(r'<!--|<!\[CDATA\[|</?[A-Za-z][\w-]*(?:\s|/?>)', re.sub(r'(`+).*?\1', '', line)), 'Raw HTML is outside these translation tasks'
        assert not re.search(r'(?:^|[ \t>])\[[^\]]+\]:', re.sub(r'(`+).*?\1', '', line)), 'Reference definitions can hide prose; use inline links as in the pinned baselines'
        if not line.strip():
            flush()
            continue
        heading = re.match(r' {0,3}(#{1,6})[ \t]+(.+?)\s*#*\s*$', line)
        if heading:
            flush()
            headings.append(len(heading[1]))
            blocks.append(('heading', heading[2]))
        elif line.lstrip().startswith('|'):
            flush()
            assert line.strip().endswith('|'), 'Preserve the table outer pipes'
            kind = 'table-separator' if re.fullmatch(r'[\s|:-]+', line) else 'table'
            row = (kind, line.strip())
            blocks.append(row)
            table_rows.append(row)
        elif re.match(r'\s*(?:[-+*]|\d+[.)])\s+', line):
            flush()
            blocks.append(('list', re.sub(r'^\s*(?:[-+*]|\d+[.)])\s+', '', line).strip()))
        elif line.lstrip().startswith('>'):
            flush()
            blocks.append(('quote', line.lstrip()[1:].strip()))
        elif not paragraph and blocks and blocks[-1][0] in ('list', 'quote') and line.startswith('  '):
            kind, value = blocks[-1]
            blocks[-1] = (kind, value + ' ' + line.strip())
        else:
            paragraph.append(line.strip())
    flush()
    flush_table()
    assert fence is None, 'Unclosed fenced code block'
    return headings, fences, blocks


def link_targets(text):
    # Mask inline destinations before finding bare URLs: punctuation that is
    # part of an explicit destination must never be trimmed as sentence prose.
    matches = list(re.finditer(r'\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\s*\)', text))
    targets = {match[1].strip('<>') for match in matches}
    visible = list(text)
    for match in matches:
        visible[match.start():match.end()] = ' ' * (match.end() - match.start())
    bare = re.findall(r'https?://[^\s<>`"\[\]{}\u3000-\u303f\uff00-\uffef]+', ''.join(visible))
    targets.update(target.rstrip('.,;:)') for target in bare)
    return targets


def technical_terms(source):
    return {word for word in re.findall(r'[A-Za-z][A-Za-z0-9_.-]*', source)
            if any(char.isupper() for char in word) or '.' in word}


def prose(text, source=None):
    known_code = set(re.findall(r'(`+)(.*?)\1', source or ''))
    technical = technical_terms(source or '')

    def inline(match):
        if source is None or (match[1], match[2]) in known_code:
            return ''
        words = re.findall(r'[A-Za-z][A-Za-z0-9_.-]*', match[2])
        if words and all(word in technical for word in words):
            return ''
        # Newly wrapping English sentences in backticks must not exempt them.
        return match[2]

    text = re.sub(r'(`+)(.*?)\1', inline, text)
    text = re.sub(r'!?\[([^\]]*)\]\([^\n]*?\)', r'\1', text)
    text = re.sub(r'https?://[^\s<>]+|<[^>]+>', '', text)
    return text


def language_prose(text, source):
    technical = technical_terms(source)
    technical.update(re.findall(r'\[([A-Za-z0-9_.-]+)\]\(', source))
    return re.sub(r'[A-Za-z][A-Za-z0-9_.-]*',
                  lambda match: '' if match[0] in technical else match[0],
                  prose(text, source))


def check_language_plausibility(localized, language, context):
    # Lightweight grammatical-script checks reject random Unicode sampling.
    # These are broad function characters, never task/caveat keyword matches.
    if language in ('es', 'de', 'fr'):
        return  # Spanish uses word-level plausibility below, not script alone.
    if len(localized) < 40:
        return
    common = {
        'ko': set('다요는은을를이가에의로와과도서한지할수있없것해합니하주세'),
        'zh-CN': set('的了是在和有与为不这以可将到中个上用者或对从并通过其'),
    }
    if language == 'ja':
        grammatical = sum('HIRAGANA' in unicodedata.name(char, '') for char in localized)
    else:
        grammatical = sum(char in common[language] for char in localized)
    assert grammatical >= len(localized) * 0.05, f'{context}: implausible language (random script garbage)'


def target_letter(char, language):
    name = unicodedata.name(char, '')
    if language == 'ko':
        return 'HANGUL' in name
    han = 'CJK UNIFIED IDEOGRAPH' in name or 'CJK COMPATIBILITY IDEOGRAPH' in name
    if language == 'ja':
        return han or 'HIRAGANA' in name or 'KATAKANA' in name
    if language in ('es', 'de', 'fr'):
        return 'LATIN' in name
    assert language == 'zh-CN', f'Unsupported language: {language}'
    return han


def check_language(text, language, context, source=None):
    visible = prose(text) if source is None else language_prose(text, source)
    if language in ('es', 'de', 'fr'):
        words = re.findall(r"[^\W\d_]+", visible.casefold())
        common = set("el la los las un una unos unas de del que y o en por para con sin se es son como al no su sus cada este esta estas estos puede pueden debe deben solo también antes después mismo más mediante entre hasta dentro cuando pero si lo hay será deben queda cualquier todo todos todas otro otra quien quienes según durante así tanto dicha dicho".split())
        if language == 'de':
            common = set('der die das den dem des ein eine einer einen einem eines und oder in im am an auf für von vom mit ohne zu zur zum ist sind nicht nur auch als vor nach bei wird werden kann können muss müssen jeder jede alle diese dieser dieses durch wenn aber es sie ihr ihre sich kein keine einem'.split())
        if language == 'fr':
            common = set('le la les un une des de du et ou en pour avec sans est sont ce cette ces qui que ne pas au aux par dans sur avant après même chaque vous votre vos si peut peuvent doit doivent aussi plus aucun aucune se à il elle ils elles nous on comme tout tous toute toutes'.split())
        if len(words) >= 8:
            assert sum(word in common for word in words) >= max(1, len(words) * 0.10), f'{context}: target language function words missing'

    letters = [char for char in visible if char.isalpha()]
    localized = [char for char in letters if target_letter(char, language)]
    assert letters and len(localized) > len(letters) / 2, f'{context}: target script must be a majority of prose letters'
    if len(localized) >= 20:
        assert len(set(localized)) >= 6, f'{context}: repeated character garbage'
        assert Counter(localized).most_common(1)[0][1] <= len(localized) * 0.4, f'{context}: repeated character padding'
        assert not re.search(r'(.{2,80})\1{3,}', ''.join(localized)), f'{context}: repeated phrase padding'
    check_language_plausibility(localized, language, context)
    return localized


def check_translation(repo, config, baseline):
    repo = Path(repo)
    path = repo / config['translation']
    assert path.is_file(), f'Missing {config["translation"]}'
    english = baseline.decode('utf-8')
    assert (repo / 'README.md').read_bytes() == baseline, 'English README must remain byte-identical to the pinned baseline'
    translated = path.read_bytes().decode('utf-8')
    original_headings, original_fences, original_blocks = parse(english)
    headings, fences, blocks = parse(translated)
    assert headings == original_headings, 'Heading count/levels/order changed'
    assert fences == original_fences, 'Fenced blocks must be byte-identical and in order (including fence markers and final newlines)'
    assert link_targets(translated) == link_targets(english), 'Preserve exactly every URL/relative link target; no added links'
    assert [kind for kind, _ in original_blocks] == [kind for kind, _ in blocks], 'Preserve every paragraph, list item, table row and code block in section order, including caveats'
    all_prose, seen = [], Counter()
    for index, ((kind, source), (_, actual)) in enumerate(zip(original_blocks, blocks), 1):
        if kind == 'fence':
            continue
        if kind == 'table-separator':
            assert actual == source, f'Block {index}: preserve the table delimiter row'
            continue
        if kind == 'table':
            cells = lambda value: len(re.findall(r'(?<!\\)\|', re.sub(r'`[^`]*`', '', value)))
            assert cells(actual) == cells(source), f'Block {index}: preserve table column count'
        assert Counter(re.findall(r'`([^`]+)`', actual)) == Counter(re.findall(r'`([^`]+)`', source)), f'Block {index}: preserve inline code exactly'
        assert link_targets(actual) == link_targets(source), f'Block {index}: link target moved/removed/added'
        source_prose, actual_prose = prose(source), prose(actual, source)
        source_letters = sum(char.isalpha() for char in source_prose)
        all_prose.append(language_prose(actual, source))
        minimum_length = max(1, int(0.15 * len(source_prose.strip()))) if source_prose.strip() else 0
        assert len(actual_prose.strip()) >= minimum_length, f'Block {index}: missing translated prose'
        # Technical-only/short labels (MIT, Node.js, Pi, etc.) may stay unchanged.
        if len(re.findall(r'[A-Za-z]{2,}', source_prose)) >= 4:
            localized = check_language(actual, config['language'], f'Block {index}', source)
            assert len(localized) >= max(4, source_letters * 0.12), f'Block {index}: insufficient translated coverage'
            normalized_source = ' '.join(source_prose.split()).casefold()
            normalized_actual = ' '.join(actual_prose.split()).casefold()
            source_sentences = re.findall(r'[a-z][a-z ,;’\'-]{35,}[.!?]', normalized_source)
            for sentence in source_sentences:
                assert sentence not in normalized_actual, f'Block {index}: untranslated English sentence'
            source_words = re.findall(r'[a-z]{2,}', language_prose(source, source).casefold())
            actual_words = re.findall(r'[a-z]{2,}', language_prose(actual, source).casefold())
            source_runs = {tuple(source_words[start:start + 6]) for start in range(len(source_words) - 5)}
            assert not any(tuple(actual_words[start:start + 6]) in source_runs for start in range(len(actual_words) - 5)), f'Block {index}: untranslated English word sequence'
            normalized = re.sub(r'\s+', '', ''.join(localized))
            seen[normalized] += 1
            assert seen[normalized] <= 2, f'Block {index}: repeated filler paragraph'
    check_language('\n'.join(all_prose), config['language'], 'Document')
