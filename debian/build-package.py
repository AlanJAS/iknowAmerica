#!/usr/bin/env python3
"""Stage the architecture-independent Debian package without debhelper."""
import gzip
import hashlib
import shutil
import subprocess
from pathlib import Path

root = Path('debian/iknowamerica-pkg')
if root.exists():
    shutil.rmtree(root)
app = root / 'usr/share/iknowamerica'
app.mkdir(parents=True)
shutil.copy2('conozco.py', app)
shutil.copytree('recursos', app / 'recursos', ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
(app / 'activity').mkdir()
shutil.copy2('activity/activity.info', app / 'activity/activity.info')
for po in sorted(Path('po').glob('*.po')):
    dest = root / 'usr/share/locale' / po.stem / 'LC_MESSAGES/org.ceibaljam.conozcoamerica.mo'
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(['msgfmt', '-o', str(dest), str(po)], check=True)
(app / 'locale').symlink_to('../locale')
for src, dst in [
    ('debian/iknowamerica', 'usr/bin/iknowamerica'),
    ('debian/iknowamerica.desktop', 'usr/share/applications/iknowamerica.desktop'),
    ('activity/america.svg', 'usr/share/icons/hicolor/scalable/apps/iknowamerica.svg'),
    ('debian/copyright', 'usr/share/doc/iknowamerica/copyright'),
    ('README.md', 'usr/share/doc/iknowamerica/README.md'),
    ('LICENSE.md', 'usr/share/doc/iknowamerica/LICENSE.md'),
]:
    target = root / dst
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, target)
with (root / 'usr/share/doc/iknowamerica/changelog.Debian.gz').open('wb') as out:
    with gzip.GzipFile(filename='', fileobj=out, mode='wb', mtime=0) as gz:
        gz.write(Path('debian/changelog').read_bytes())
(root / 'DEBIAN').mkdir()
for path in root.rglob('*'):
    if not path.is_symlink():
        path.chmod(0o755 if path.is_dir() else 0o644)
(root / 'usr/bin/iknowamerica').chmod(0o755)
with (root / 'DEBIAN/md5sums').open('w') as out:
    for path in sorted((root / 'usr').rglob('*')):
        if path.is_file() and not path.is_symlink():
            out.write(f'{hashlib.md5(path.read_bytes()).hexdigest()}  {path.relative_to(root)}\n')
