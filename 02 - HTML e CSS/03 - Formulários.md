# Formulários

- O elemento ``<form>`` é utilizado para criar um formulário HTML para entrada do usuário.
- O atributo ``action`` define a ação a ser executada quando o formulário é submetido. Normalmente, os dados do formulário são enviados para um arquivo no servidor quando o utilizador clica no botão "submeter". No exemplo abaixo, os dados do formulário são enviados para um arquivo chamado "action_page.php". Este arquivo contém um script do lado do servidor que trata dos dados do formulário.
- O atributo ``method`` especifica o método HTTP a ser utilizado ao submeter os dados do formulário. 
- A tag ``<label>`` define uma etiqueta para os elementos de formulário.
- O atributo ``for`` da tag ``<label>`` deve ser igual ao atributo de ``id`` do elemento ``<input>`` para os unir.
- A tag ``<fieldset>`` é utilizada para agrupar elementos relacionados, desenhando uma caixa à volta dos mesmos.
- A tag ``<legend>`` é utilizada para definir uma legenda para o elemento ``<fieldset>``.

````html
<form action="/action_page.php" method="get">

    <fieldset>

        <legend>Elementos de Formulário</legend>

        <!-- Texto Básico -->
        <p>
            <label for="nome">Nome:</label>
            <!-- Input com Placeholder -->
            <input type="text" name="nome" id="nome" placeholder="Seu nome aqui">
            <!-- Input com Valor Padrão -->
            <input type="text" name="nome" id="nome" value="Silvio Santos">
            <!-- Input Desabilitado -->
            <input type="text" name="nome" id="nome" disabled>
        </p>

        <!-- Textarea -->
        <p>
            <label for="mensagem">Digite sua mensagem:</label>
            <textarea name="mensagem" id="mensagem" cols="30" rows="10"></textarea>
        </p>

        <!-- Checkbox -->
        <p>
            <label for="dev">Sou um Dev 1?</label>
            <input type="checkbox" id="dev1" name="dev1" value="sim" checked>
            <label for="dev">Sou um Dev 2?</label>
            <input type="checkbox" id="dev2" name="dev2" value="sim">
            <label for="dev">Sou um Dev 3?</label>
            <input type="checkbox" id="dev3" name="dev3" value="sim">
        </p>

        <!-- Radio -->
        <p>
            <!-- o atributo "name" irá agrupá-los, pois podemos ter apenas -->
            <!-- uma única resposta -->
            <input type="radio" id="feminino" name="genero" value="feminino">
            <label for="feminino">feminino </label>
            <input type="radio" id="masculino" name="genero" value="masculino">
            <label for="masculino">masculino </label>
            <input type="radio" id="indefinido" name="genero" value="indefinido">
            <label for="indefinido">indefinido </label>
        </p>

        <!-- Data e Hora -->
        <p>
            <label for="data">Data 1:</label>
            <input type="date" name="data" id="data">
            <!-- Data com Valor Padrão 23/02/2023 -->
            <label for="data2">Data 2:</label>
            <input type="date" name="data2" id="data2" value="2023-02-23">
            <!-- Datetime-local -->
            <label for="data3">Data 3:</label>
            <input type="datetime-local" name="data3" id="data3" value="2023-02-23T07:26">
            <!-- Time -->
            <label for="data">Hora:</label>
            <input type="time" name="hora" id="hora">
        </p>

        <!-- Cor -->
        <p>
            <label for="cor">Cor</label>
            <input type="color" name="cor" id="cor">
        </p>

        <!-- E-mail -->
        <p>
            <label for="email">E-mail:</label>
            <input type="email" name="email" id="email" placeholder="Seu e-mail aqui">
        </p>

        <!-- Senha -->
        <p>
            <label for="senha">Senha:</label>
            <input type="password" name="senha" id="senha" placeholder="Digite sua senha">
        </p>

        <!-- Upload de Arquivo -->
        <p>
            <label for="arquivo">Anexar Arquivo:</label>
            <input type="file" name="arquivo" id="arquivo">
            <!-- definindo o tipo de arquivo -->
            <label for="arquivo">Anexar PDF:</label>
            <input type="file" name="arquivo" id="arquivo" accept=".pdf,.svg,image/*">
            <!-- Selecionando Múltiplos Arquivos -->
            <label for="arquivo">Anexar Múltiplos Arquivos:</label>
            <input type="file" name="arquivo" id="arquivo" multiple>
        </p>

        <!-- Seletor de Número (quantidade) -->
        <p>
            <label for="numero">Número:</label>
            <input type="number" name="numero" id="numero">
            <!-- Definindo valor mínimo e máximo -->
            <label for="numero">Número:</label>
            <input type="number" name="numero" id="numero" min="10" max="15">
            <!-- Definildo os "saltos" de valores -->
            <label for="numero">Número:</label>
            <input type="number" name="numero" id="numero" step="5">
        </p>

        <!-- Range -->
        <p>
            <label for="points">Points (between 0 and 10):</label>
            <input type="range" id="points" name="points" min="0" max="10" step="1" value="8">
        </p>

        <!-- URL -->
        <p>
            <label for="url">URL:</label>
            <input type="url" name="url" id="url">
        </p>

        <!-- Search (pesquisa) -->
        <p>
            <label for="pesquisa">Pesquisa:</label>
            <input type="search" name="pesquisa" id="pesquisa">
        </p>

        <!-- Select -->
        <p>
            <label for="select">Selecionar uma opção:</label>
            <select name="select" id="select">
                <option value="arroz">Arroz</option>
                <option value="feijao" selected>Feijão</option> <!-- selecionada por padrão -->
                <option value="carne">Carne</option>
                <option value="batata" disabled>Batata</option> <!-- opção desabilitada -->
            </select>
        </p>

        <!-- Select com Agrupamento -->
        <p>
            <label for="select">Selecionar uma opção:</label>
            <select name="select" id="select">
                <optgroup label="Alimentos">
                    <option value="arroz">Arroz</option>
                    <option value="feijao" selected>Feijão</option> <!-- selecionada por padrão -->
                    <option value="carne">Carne</option>
                    <option value="batata" disabled>Batata</option> <!-- opção desabilitada -->
                </optgroup>
                <optgroup label="Ferramentas">
                    <option value="martelo">Martelo</option>
                    <option value="faca">Faca</option>
                    <option value="alicate">Alicate</option>
                    <option value="tesoura">Tesoura</option>
                </optgroup>
            </select>
        </p>

        <!-- Botões -->
        <p>
            <!-- Botão de Submit -->
            <button type="submit">Enviar</button>
            <!-- Botão de Reset -->
            <button type="reset">Resetar</button>
        </p>

    </fieldset>
</form>
````