class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefixos = {}

        for string in strs:
            if len(string) > 1:
                prefixo = string[:2]
                if prefixo in prefixos:
                    prefixos[prefixo] += 1
                else:
                    prefixos[prefixo] = 1
            else:
                if string in prefixos:
                    prefixos[string] += 1
                else:
                    prefixos[string] = 1

        prefixo_que_mais_repete = {}

        for chave, valor in prefixos.items():
            if len(prefixo_que_mais_repete) != 0:
                chave_maior, valor_maior = prefixo_que_mais_repete.popitem()
                prefixo_que_mais_repete = {chave_maior: valor_maior}

            if len(prefixo_que_mais_repete) == 0:
                prefixo_que_mais_repete = {chave: valor}
            elif valor > valor_maior:
                prefixo_que_mais_repete = {chave: valor}
            else:
                prefixo_que_mais_repete = {chave_maior: valor_maior}

        for chave, valor in prefixo_que_mais_repete.items():
            if len(chave) == 1:
                return chave
            elif valor <= 1:
                return ''
            else:
                return chave


strs = ["flower", "flow", "flight"]
# strs = ["dog","racecar","car"]
# strs = ["a"]
prefixo = Solution()
prefixo_que_mais_repete = prefixo.longestCommonPrefix(strs)
print(prefixo_que_mais_repete)
