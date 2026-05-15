# ca-joe-yang.github.io

Personal academic website for Chiao-An Yang, built with [Jekyll](https://jekyllrb.com/) and hosted on GitHub Pages.

## High-level structure

The homepage ([index.html](index.html)) is a single page with four stacked sections — bio, research, teaching, awards — each rendered from an include and driven by a YAML data file.

```
_config.yml             Jekyll config
index.html              Homepage — pulls in the four sections below
CNAME, robots.txt       GitHub Pages hosting config

_data/                  Content (YAML) — edit here to update the site
  info.yaml               Name, bio, links (Scholar / GitHub / email / ...)
  research.yaml           Papers (title, venue, authors, teaser, paper/code/project links)
  teaching.yaml           TA / teaching history
  awards.yaml             Awards and honors
  affiliations.yaml       Institutions with logos

_includes/              HTML partials rendered by index.html
  header.html, footer.html
  main.html               Top section (photo, bio, affiliations)
  research.html, teaching.html, awards.html
  bio.html
  project_header.html     Header used by per-project pages

_layouts/
  default.html            Layout for the homepage
  project_layout.html     Layout for per-project pages

css/                    Stylesheets (bootstrap + theme variants: nvidia, purdue, merl, amber)
logos/                  Institution / affiliation logos
resource/
  photo.jpg, favicon.ico, ...
  projects/               One subfolder per project (4D_RGPT, RwSA, LISA, ...)
                          each with its own index.html + assets/
site.js                 Small client-side script
pdf2png.py              Helper to convert paper PDFs to PNG teasers
```

## Editing content

- **Add/update a paper**: edit [_data/research.yaml](_data/research.yaml). For a paper with its own project page, drop the page under `resource/projects/<NAME>/` and point `project:` at it.
- **Update bio / contact links**: [_data/info.yaml](_data/info.yaml).
- **Awards, teaching, affiliations**: their respective YAML files in [_data/](_data/).
- **Change theme**: swap the stylesheet in [css/](css/) (e.g. `nvidia.css`, `purdue.css`). New themes can be generated at https://themestr.app/.

## Build locally

```bash
jekyll build              # generates _site/
jekyll serve -l -H localhost   # live-reload dev server
```

## Deploy

GitHub Pages builds from this repo directly. The custom domain is set in [CNAME](CNAME).
