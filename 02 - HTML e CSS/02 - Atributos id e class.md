# Atributos id e class

``id`` é um identificador único em uma página. Não podemos ter duas ou mais tags com o mesmo ``id``.   

``class`` é um identificador que pode ser incluido em mais de uma tag em uma mesma página. 

### HTML

```html
<h1 id="cabecalho-um" class="fundo-vermelho borda-esquerda">
     Cabeçalho 1
</h1>

<h2 id="cabecalho-dois" class="fundo-vermelho">
    Cabeçalho 2
</h2>
```

### CSS

```css
/* Seletor de Tag */
h2 {
    border-bottom: 30px solid salmon;
}

/* Seletor de Id */
#cabecalho-um {
    border-top: 50px solid green;
}

/* Seletor de Classe */
.fundo-vermelho {
    background-color: red;
}

.borda-esquerda {
    border-left: 20px solid blue;
}
```