# Image self link

This small Pelican plug-in transforms images into self-connections. This allows to open images in their original size. Links are opened in a new browser tab.

*Recommended for static websites without an image gallery.*

## Example:

Markdown:

```markdown
![Image](path/to/image.jpg)
```
generated HTML:
```html
<a href="path/to/image.jpg" target="_blank"><img alt="Image" src="path/to/image.jpg"></a>
```

