from pathlib import Path
import uuid
import datetime


def main():
    'Main.'
    dr = Path('/Users/th/CODE/PORTFOLIO/hamada2029.github.io/content/articles')
    uid = str(uuid.uuid4()).split('-')[0]
    print(uid)
    nw = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    space2 = '  '
    s = f'''Title: {uid}
Date: {nw}
Category:
Tags:
Thumbnail: rect1.png
Slug: {uid}

![Alt Text]({{static}}/images/rect1.png){space2}


'''
    fp = dr / f'{uid}.md'
    fp.write_text(s)


if __name__ == '__main__':
    main()
