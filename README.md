# SnipBank

Easily collect snippets and recall them later.

## Requirements

- Espanso 2.x or higher
- Python 3.0 or higher with Pip
    - PyYAML 5.x or higher (install with `pip3 install pyyaml`)

## Keyboard Shortcuts

- Use `,,..` (two commas, two dots) to add a snippet.
- Use `..,,` (two dots, two commas) to remove a snippet.

## Special: Pressing Tab and Enter

- Use `^TAB^` in a snippet for pressing the Tab key.
- Use `^ENTER^` in a snippet for pressing the Enter key.

## Paste/Silent Mode

When using `paste` mode (default), the snippet's replacement is printed. This
allows you to use `,,..` to add a new trigger and type at the same time, or 
`..,,` as the "paste" step of a disposable clipboard.

When using `silent` mode, nothing is printed. This is useful when you just want
to manage your snippets without writing them out.
