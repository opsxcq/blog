+++
title = "How to use Org Mode and Hugo for a better scientific blogging"
author = ["OPSXCQ"]
date = 2022-01-15
draft = false
+++

Small overview on the usage of `Org-Mode` for blogging leveraging all features
that `Emacs` can give, as an interactive and literate code development environment
where you have access to bibliographic tools for easy reference and a
comfortable editor.

<!--more-->

The whole stack for being able to archive this:

-   Debian Linux or any other distribution
-   Emacs
-   Spacemacs
-   Org-More along with other packages (org-ref, org-roam, etc...)
-   Python environment (poetry, python and Spacemacs layers)
-   Git
-   Hugo
-   Travis and GitHub


## Hugo Structure {#hugo-structure}


### Summary {#summary}

Any text at the beginning of the document is considered a summary until it
reaches the max allowed characters or the tag `#+hugo: more` is found.


### Generating color schemes for syntax highlight {#generating-color-schemes-for-syntax-highlight}

```bash
hugo gen chromastyles --style=monokoi > themes/strm/static/css/syntax.css
```


## Spacemacs configuration {#spacemacs-configuration}


### Layers {#layers}

Check out the official `Org-Mode` layer documentation on Spacemacs for further
reference. Bellow an example

```emacs-lisp
     (org :variables
          org-enable-epub-support t
          org-enable-org-journal-support t
          org-fontify-whole-heading-line t
          org-fontify-quote-and-verse-blocks t
          org-fontify-done-headline t
          org-pretty-entities t
          org-projectile-file "projectile.org"
          org-projectile-todo-files "todo.org"
          org-journal-dir "~/studies/journal/"
          org-journal-file-format "%Y-%m-%d"
          org-journal-date-prefix "#+TITLE: "
          org-journal-date-format "%A, %B %d %Y"
          org-journal-time-prefix "* "
          org-journal-time-format ""
          org-babel-python-command "python3"
          org-confirm-babel-evaluate nil
          org-use-property-inheritance t
          org-enable-roam-support t
          org-download-image-dir "~/Pictures/org/"
          org-enable-hugo-support t
          )
```

And append the following to your `dotspacemacs-additional-packages` to make your
life easier.

```emacs-lisp
dotspacemacs-additional-packages '(
                                  ob-async
                                  ob-go
                                  py-autopep8
                                  (py-docformatter :location (recipe :fetcher github :repo "humitos/py-docformatter.el"))
                                  pyimport
                                  org-roam-bibtex
                                  org-noter
                                  org-noter-pdftools
                                  (org-fragtog :location (recipe :fetcher github :repo "io12/org-fragtog"))
                                  )
```


### General Writing tips {#general-writing-tips}

`Write-room` mode will improve your focus by removing everything else from the
screen and centering your buffer, use with `SPC w C C`. More focus can be obtained
with `org-narrow-to-subtree` which will remove everything else from the document
except the current sub-tree, there are a few alternatives:

-   `, s n` : org narrow to sub-tree
-   `SPC n w`: widen back to normal
-   `, '` : open a source code block to be edited on the specialized editor.
-   `SPC S l` : Enable and use `langtool`

You can use [this site](https://alldocs.app/convert-markdown-to-emacs-org-mode) to easily convert from `markdown` to `Org-Mode`.


### Auto Export on save {#auto-export-on-save}


### Langtool {#langtool}


### Bibtex references {#bibtex-references}

References are handled by `org-ref`, they are exported from `Zotero` and `Calibre`,
for paper and books respectively. To make sure that they will be reachable add
to the section of the document which you want to have the section `bibliography`
rendered the following piece of text:

```text
bibliography:../../library.bib,../../references.bib
```

Remember that this is a relative path from your document to the project's root.
After this is done, references can be added with the key combination `SPC m i c`.

A paper reference will look like this (<diffie_new_1976>) while a book
reference will be rendered like this (<StuartScott745>).


### footnotes {#footnotes}

Sometimes the text gets too clumsy and some explanations are not required for
some reader, but are for others&nbsp;[^fn:1] , to add a footnote use `, i f.`


## Math and LaTeX {#math-and-latex}

_LaTeX_ is rendered using `Katex` if `math` variable is set to `true` on page or site
level. On emacs inline _LaTeX_ rendering can be achieved using [org-fragtog](https://github.com/io12/org-fragtog) .

Not all functions are supported, take a look at [Katex limitations](https://katex.org/docs/supported.html) to check it
out before using. Also, if an expression or function is not supported, with
Emacs you can directly export the `png` file which is automatically generated.

Here some inline expression \\(a^2=b\\) and \\( b=2 \\), then the solution must be
either \\[ a=+\sqrt{2} \\] or \\[ a=-\sqrt{2} \\]

Here a multi-line example using Nash Equilibrium to illustrate:

\\[
u\_i(s\_i^\*, s\_{-i}^\*) \geq u\_i(s\_i, s\_{-i}^\*) \\;\\;{\rm for \\; all}\\;\\; s\_i \in S\_i
\\]


## Literate programming {#literate-programming}

One of the greatest advantages of using `Org-Mode` for writing documents is
leveraging of [literate programming](https://en.wikipedia.org/wiki/Literate_programming) to write a more reproducible research, along
with features like [Tangle](https://orgmode.org/manual/Extracting-Source-Code.html) which allows you to extract source from your documents.

Comparing it with alternatives like `Jupyter` you have all the advantages of your
keybindings, I for example use `Vim` keybindings on `Emacs`, being able to use
several programming environments, references, a brain dump if you use
`Org-Roam`. Along with it, you can start sessions and jump right to it, separate
your sessions, so your variables don't get messed up.

`Org` files work better with `Git` in general, so version control is much easier.
`Emacs` supports `Jupyter` and `IPython`, but given the power of `Org-Mode` simply using
`Python` you can archive everything and more.

One thing that is lost is the capability of having inline `Plotly` plots, which
are interactive due to the usage of web technology. But if you are executing
`Emacs` on your desktop you can still use it and plots will open in a browser.

This makes `Org-Mode` quite superior to any other environment of interactive
development and for a local user which can leverage even further of `Bibtex`,
`Org-Roam` and all babel executors there is no other alternative with such power.


### Python and Plots {#python-and-plots}

The given code bellow is a demonstration of the usage of Python.

```python
import seaborn as sns
sns.set_theme(style="ticks")

dots = sns.load_dataset("dots")

# Define the palette as a list to specify exact values
palette = sns.color_palette("rocket_r")

# Plot the lines on two facets
sns.relplot(
    data=dots,
    x="time", y="firing_rate",
    hue="coherence", size="choice", col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
).savefig('./demo-plot.png')
```

{{< figure src="/ox-hugo/demo-plot.png" >}}

If the image above is not displayed in your `Emacs` use `org-toggle-inline-images`
with the shortcut `, T i`.


### Org Mode tweaks {#org-mode-tweaks}

To avoid re-evaluating the code every time that it is exported, add the
following property at the beginning of the document.

```text
#+PROPERTY: header-args :eval never-export
```


## Org Mode examples {#org-mode-examples}

Bellow just some random `Org-Mode` markup to show how it renders.

> To buy books would be a good thing if we could also buy the time to read them;
> but the purchase of books is often mistaken for the assimilation and mastering
> of their contents. -- Arthur Schopenhauer

Some inline styling: `Verbatim` **bold** _italic_

Table rendering:

| A | b | c | d | e |
|---|---|---|---|---|
| 1 | 1 | 3 | 1 | 2 |
| 1 | 1 | 3 | 1 | 2 |
| 1 | 1 | 3 | 1 | 2 |
| 1 | 1 | 3 | 1 | 2 |
| 1 | 1 | 3 | 1 | 2 |

```text
Example
```


## Including external content {#including-external-content}

`Hugo` offers what is called `shortcodes`, which are mere functions which wrap a
more elaborated rendering pipeline of data. Bellow some examples how to include
external content using `shortcodes`.

The `shortcodes` have to be wrapped around double `@@ .. @@`, when using a
markdown `shortcode`, include the prefix `md:` before the actual code.


### Twitter {#twitter}

Using the `shortcode` bellow is possible to render a tweet:

{{&lt; tweet user="officialmcafee" id="1405918427663982594" &gt;}}

 {{< tweet user="officialmcafee" id="1405918427663982594" >}}


### Gist {#gist}

Same applies for a `Gist` from `GitHub`:

{{&lt; gist opsxcq f5b3ba08f45d70f998a4cc8a25bf57a3 &gt;}}

 {{< gist opsxcq f5b3ba08f45d70f998a4cc8a25bf57a3 >}}


### YouTube {#youtube}

The inclusion of external videos is also possible

{{&lt; youtube pctYu1Wz514 &gt;}}

 {{< youtube id="pctYu1Wz514" >}}


## Templates {#templates}


### Posts {#posts}


### Studies {#studies}


### Projects {#projects}


### Malware {#malware}

<../../library.bib,../../references.bib>

[^fn:1]: Not everyone is equal