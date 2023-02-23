# Tabelas

## Propriedades CSS:

````css
table { 
    border-collapse: collapse; 
}

caption {
    caption-side: bottom; 
} 
````

## Atributos HTML:

````html
colspan="2" 
rowspan="2"  
````
    
## Tornando uma tabela responsiva no celular:

````css
.responsive-table{
    max-width: 100%;
    overflow-x: auto;
}
````


````html
<div class="responsive-table">
    <table>
        <caption>Descrição da Tabela</caption>
        <thead>
            <tr>
                <th>Titulo 1</th>
                <th>Titulo 2</th>
                <th>Titulo 3</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Conteúdo 1</td>
                <td>Conteúdo 2</td>
                <td>Conteúdo 3</td>
            </tr>
            <tr>
                <td colspan="2" rowspan="2">Conteúdo 1</td>
                <td>Conteúdo 3</td>
            </tr>
            <tr>
                <td>Conteúdo 3</td>
            </tr>
        </tbody>
        <tfoot>
            <tr>
                <td>Rodapé 1</td>
                <td>Rodapé 2</td>
                <td>Rodapé 3</td>
            </tr>
        </tfoot>
    </table>
</div>
````