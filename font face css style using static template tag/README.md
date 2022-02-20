# font face css style using static template tag

### Method 1 - ( `using style tag` )

- [Reference Link](https://developer.mozilla.org/en-US/docs/Web/API/FontFace/FontFace)

```html
@font-face { font-family: MorganChalk; src: url("{% static
'core/fonts/MorganChalk.ttf' %}"); } .ex1 { font-family: MorganChalk; }
```

### Method 2 - ( `using script tag` )

- [Reference Link](https://stackoverflow.com/questions/21346045/django-new-fonts)

```html
<script>
  async function loadFonts() {
    const AlexBrushFont = new FontFace(
      "AlexBrush",
      `url("{% static 'core/fonts/AlexBrush.ttf' %}")`
    );
    // wait for font to be loaded
    await AlexBrushFont.load();
    // add font to document
    document.fonts.add(AlexBrushFont);
    // enable font
    const ex2 = document.querySelector(".ex2");
    ex2.style.fontFamily = "AlexBrush";
  }
  loadFonts();
</script>
```

## Output- 

![image](https://user-images.githubusercontent.com/63374020/154851121-c3155133-f7c3-4516-ae76-a3ff55ed6111.png)
